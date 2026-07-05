#!/usr/bin/env python3
"""PPP-localize an App Store subscription's prices via the asc CLI.

For one subscription: pick the US price point matching --target-us-price,
fetch Apple's equalized local price points for it, and schedule those points
in the given territories. Handles the known asc/ASC API failure modes:
  - approved subs require a future --start-date (>= 2 days out)
  - some territories (BR MX TR TH IN ID VN) allow only ONE future price
    record, and a failed create may still write the record -> delete + re-set

Usage:
  ppp_localize.py --subscription-id 123 --target-us-price 4.99 \
      --territories BRA,MEX,TUR --start-date 2026-07-07 [--dry-run] [--apply]

Run --dry-run first, show the plan to the user, then re-run with --apply.
Exit code 0 = all requested territories verified scheduled.
"""
import argparse, base64, json, subprocess, sys
from datetime import date, timedelta


def asc(*args):
    r = subprocess.run(["asc", *args], capture_output=True, text=True)
    return r.returncode, r.stdout, r.stderr


def asc_json(*args):
    rc, out, err = asc(*args)
    if rc != 0:
        sys.exit(f"asc {' '.join(args)} failed: {err or out}")
    return json.loads(out)


def decode_id(b64id):
    return json.loads(base64.b64decode(b64id + "=="))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--subscription-id", required=True)
    p.add_argument("--target-us-price", required=True,
                   help="US customer price selecting the point, e.g. 4.99")
    p.add_argument("--territories", required=True,
                   help="comma-separated alpha-3 codes, e.g. BRA,MEX,IND")
    p.add_argument("--start-date",
                   default=str(date.today() + timedelta(days=2)),
                   help="YYYY-MM-DD, must be >= 2 days out (default: +2 days)")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--apply", action="store_true")
    a = p.parse_args()
    if not (a.dry_run or a.apply):
        sys.exit("pass --dry-run to preview or --apply to execute")
    terrs = [t.strip().upper() for t in a.territories.split(",") if t.strip()]

    # 1. US price point matching the target price
    pts = asc_json("subscriptions", "pricing", "price-points", "list",
                   "--subscription-id", a.subscription_id,
                   "--territory", "USA", "--paginate")["data"]
    match = [x["id"] for x in pts
             if x["attributes"]["customerPrice"] == a.target_us_price]
    if not match:
        avail = sorted({x["attributes"]["customerPrice"] for x in pts}, key=float)
        sys.exit(f"no US price point {a.target_us_price}; nearest grid: {avail[:40]}...")
    us_point = match[0]

    # 2. Apple's equalized local points for that US point
    eq = asc_json("subscriptions", "pricing", "price-points", "equalizations",
                  "--price-point-id", us_point, "--paginate")["data"]
    eqmap = {decode_id(x["id"])["t"]: (x["id"], x["attributes"]["customerPrice"])
             for x in eq}

    plan, missing = [], []
    for t in terrs:
        (plan.append((t, *eqmap[t])) if t in eqmap else missing.append(t))
    print(f"US point {a.target_us_price} USD -> {len(plan)} territories, "
          f"start {a.start_date}")
    for t, _, local in plan:
        print(f"  {t}: {local}")
    if missing:
        print(f"  SKIPPED (no App Store storefront / no equalization): {missing}")
    if a.dry_run:
        print("dry run - nothing applied")
        return

    # 3. Apply, with delete+re-set recovery for single-future-record territories
    failed = []
    for t, ppid, local in plan:
        rc, out, err = asc("subscriptions", "pricing", "prices", "set",
                           "--subscription-id", a.subscription_id,
                           "--price-point", ppid, "--start-date", a.start_date)
        if rc == 0:
            continue
        msg = err or out
        if "more than one future price" in msg:
            # a future record exists (possibly written by a failed create, or
            # Apple-scheduled) - delete every future record, then re-set
            recs = asc_json("subscriptions", "pricing", "prices", "list",
                            "--subscription-id", a.subscription_id,
                            "--territory", t)["data"]
            futures = [x["id"] for x in recs
                       if (x["attributes"].get("startDate") or "") >= str(date.today())]
            for fid in futures:
                asc("subscriptions", "pricing", "prices", "delete",
                    "--price-id", fid, "--confirm")
            rc, out, err = asc("subscriptions", "pricing", "prices", "set",
                               "--subscription-id", a.subscription_id,
                               "--price-point", ppid, "--start-date", a.start_date)
        if rc != 0:
            failed.append((t, (err or out).strip()[:200]))

    # 4. Verify: exactly one record per territory at the start date
    # (the CLI's --territory filter accepts alpha-3, so query per territory
    # rather than joining alpha-2 record ids against alpha-3 inputs)
    ok = 0
    for t, ppid, local in plan:
        recs = asc_json("subscriptions", "pricing", "prices", "list",
                        "--subscription-id", a.subscription_id,
                        "--territory", t)["data"]
        n = sum(1 for x in recs
                if x["attributes"].get("startDate") == a.start_date)
        if n == 1:
            ok += 1
        else:
            print(f"VERIFY FAIL {t}: {n} records scheduled for {a.start_date}")
    for t, msg in failed:
        print(f"SET FAIL {t}: {msg}")
    print(f"verified {ok}/{len(plan)} territories scheduled for {a.start_date}")
    sys.exit(0 if ok == len(plan) and not failed else 1)


if __name__ == "__main__":
    main()
