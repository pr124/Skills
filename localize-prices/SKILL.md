---
name: localize-prices
description: Use when setting country-specific App Store prices (PPP pricing, regional pricing, cheaper prices in Brazil/India/emerging markets) for subscriptions or in-app purchases via the asc CLI, or when asked to "localize prices like we did before".
---

# Localize App Store Prices (PPP tiers via asc)

## Overview

Apple auto-equalizes every price from the US base — that is FX conversion, **not** purchasing-power pricing. "Localizing prices" means scheduling *lower* Apple price points in cheaper markets. Always verify current state first: if all territories match the US point's equalizations, no custom pricing exists yet (this fooled us once — a past "localization" turned out to be plain equalization).

## Default tiers (override per app)

| Tier | Target | Countries (alpha-3) |
|---|---|---|
| 2 (~50% of US) | nearest .49/.99 point | BRA MEX TUR POL HUN CZE ROU BGR HRV SRB GRC CHL COL PER MYS THA ZAF CHN KAZ |
| 3 (~33% of US) | nearest .49/.99 point | IND IDN VNM PHL EGY NGA PAK LKA KEN GHA MAR DZA TUN UZB UKR ARG |

BGD has no App Store storefront. Keep US/EU/UK/JP/AU/CA at default equalization.

## Subscriptions workflow

Per subscription × tier, use `scripts/ppp_localize.py` (does point lookup → equalizations → set → delete/re-set recovery → verification):

```bash
scripts/ppp_localize.py --subscription-id SUB_ID --target-us-price 4.99 \
  --territories BRA,MEX,TUR --start-date YYYY-MM-DD --dry-run   # then --apply
```

1. `asc subscriptions list --app APP_ID` → sub IDs and current US bases (`pricing summary`).
2. Compute tier targets from the US base (e.g. $9.99 → T2 $4.99, T3 $3.49; keep monthly:yearly ratio consistent).
3. **Dry-run every sub, show the user the full plan (local prices), get approval** — live-store price changes must never be applied unseen.
4. `--apply`, then confirm the script reports all territories verified.

## One-time IAPs (e.g. lifetime)

IAPs use **price schedules**, not per-territory price records:

```bash
asc iap pricing price-points list --iap-id IAP_ID            # find US point
asc iap pricing price-points equalizations --id PRICE_POINT_ID
asc iap pricing schedules create --iap-id IAP_ID --base-territory USA \
  --prices "US_POINT_ID,BR_POINT_ID:START_DATE,IN_POINT_ID:START_DATE"
asc iap pricing schedules view --iap-id IAP_ID               # verify
```

`--prices` entries are `PRICE_POINT_ID[:START_DATE[:END_DATE]]`; creating a schedule replaces the whole schedule, so include the base US point plus every custom territory point in one call. For a brand-new IAP, `asc iap setup` can set the initial price, then add the schedule.

## Gotchas (all hit in production 2026-07)

| Symptom | Cause / fix |
|---|---|
| `Initial price cannot be created again after subscription is approved` | Approved subs need `--start-date` |
| `Invalid startDate … must be on or after <date>` | Earliest allowed is ~2 days out; use the date from the error |
| `You cannot create more than one future prices for territory = X` (BR MX TR TH IN ID VN) | These territories hold ONE future record — **and the failed create may still have written it**. List `prices list --territory X`, delete future records (`prices delete --price-id … --confirm`), re-set. The script automates this. |
| Territory missing from equalizations | No storefront (e.g. BGD) — skip |
| zsh: `set -- $var` doesn't split | zsh doesn't word-split; loop in Python instead |

Price *decreases* apply to new and existing subscribers automatically; no review needed; fully reversible by deleting the scheduled record before its start date.
