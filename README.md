# AI agent skills

Personal skills synced across machines. Each skill is a directory containing a
`SKILL.md` file plus any scripts or assets it needs. The format is intentionally
plain-text so it can be used by Claude Code, Codex, or any other LLM/agent
runtime that can read local instruction files.

## Install

### Codex

Clone into Codex's skills directory:

```bash
git clone https://github.com/pr124/Skills ~/.codex/skills
```

### Claude Code

Clone into Claude Code's skills directory:

```bash
git clone https://github.com/pr124/Skills ~/.claude/skills
```

### Other LLM agents

Clone this repository anywhere your agent can read it, then point the agent at
the skill directory you want to use. A portable skill directory has this shape:

```text
skill-name/
  SKILL.md
  scripts/
  assets/
```

Agents should read the full `SKILL.md` before acting. Relative paths mentioned
inside a skill should be resolved from that skill's directory.

## Skills

| Skill | Purpose |
|---|---|
| [codex-ui](codex-ui/) | Keep UI hierarchy clear and remove decorative microcopy by default |
| [localize-prices](localize-prices/) | PPP price localization for App Store subscriptions/IAPs via the `asc` CLI |
