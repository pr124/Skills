# Portable AI agent skills

Reusable skills for LLMs and coding agents. They are not tied to Codex, Claude,
or any other model provider. Each skill is a plain-text instruction package that
can be discovered by a compatible agent or explicitly supplied to any LLM that
can read Markdown files.

## Portable format

A skill directory has this shape:

```text
skill-name/
  SKILL.md
  references/       optional detailed guidance
  scripts/          optional reusable automation
  assets/           optional output resources
  agents/           optional runtime-specific metadata
```

`SKILL.md` is the portable entrypoint. Agents should read it completely before
acting, then load only the referenced files relevant to the current request.
Relative paths resolve from the skill directory.

Files under `agents/` improve presentation or invocation in a particular
runtime. They are optional and other runtimes can ignore them.

## Install

Clone the collection anywhere your agent can read:

```bash
git clone https://github.com/pr124/Skills.git
```

Then either register the individual skill directories with your agent or copy
them into its skills directory. Common locations include:

- Codex: `~/.codex/skills/`
- Claude Code: `~/.claude/skills/`
- Other agents: use the runtime's skill, rule, context, or instruction directory

If a runtime has no native skill system, tell the LLM to read the chosen
`SKILL.md` and follow its linked references before completing the task.

## Invoke

Use the exact skill name. Some runtimes use a `$` or `/` prefix; ordinary chat
prompts can name the skill directly.

```text
Apply mobile-design-antislop before designing this onboarding flow.
Use mobile-design-antislop to harden and polish this app for release.
Review this landing page with web-design-antislop.
```

The anti-slop design skills are useful throughout the lifecycle:

1. **Before creation:** establish direction, platform behavior, tokens, and the
   design contract before generating screens.
2. **During implementation:** keep new screens and components inside the same
   system and route work to the relevant design pass.
3. **Before release:** audit, harden, and polish accessibility, responsive or
   device behavior, edge states, real content, and visual consistency.
4. **After release:** critique weak journeys using feedback, screenshots, task
   evidence, or funnel evidence, then apply the smallest corrective pass.

The entire skill does not need to run for every tiny change. Its entrypoint
routes the request to the smallest relevant reference or design pass.

## Skills

| Skill | Purpose |
|---|---|
| [mobile-design-antislop](mobile-design-antislop/) | Design native-feeling iOS and Android interfaces with platform-aware interaction and visual craft |
| [web-design-antislop](web-design-antislop/) | Design distinctive, production-grade websites and web apps without generic AI aesthetics |
| [ui-inspiration](ui-inspiration/) | Consult curated component, motion, and design-system references during interface design work |
| [localize-prices](localize-prices/) | PPP price localization for App Store subscriptions/IAPs via the `asc` CLI |
