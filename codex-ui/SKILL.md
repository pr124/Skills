---
name: codex-ui
description: Use when building, redesigning, or reviewing a web, mobile, desktop, or dashboard interface that risks decorative eyebrow labels, stacked subtitles, generic helper copy, or an overly verbose visual hierarchy.
---

# Codex UI

## Core rule

Make the important thing clear first. Treat every small text element as content that needs a job, not decoration added to make a screen feel designed.

Default header composition: `title + required navigation or action`. Do not automatically add an eyebrow, kicker, subtitle, lead paragraph, or helper sentence.

## Use less copy

- Let a clear title stand alone.
- Treat `small label → large heading → small description` as a smell, not a template.
- Add small text only when omitting it would block understanding or action, prevent an error, or provide required navigation/metadata.
- “Premium,” “reassuring,” “editorial,” “friendly,” and “comprehensive” are not reasons to add a sentence.
- Use spacing, type scale, grouping, and interaction to create hierarchy before adding words.

Bad: `FOOD LABEL GUIDE` above `How to Read a Food Ingredient List`.

Bad: `FOOD, LABELS, AND EVERYDAY HEALTH` above `Blog` plus a generic lead.

Preferred: the clear title (`How to Read a Food Ingredient List` or `Blog`) with only required navigation or action.

For page headers, content indexes, and empty states, write the title and action first. Treat requests for “any supporting copy” as optional, not as a requirement to invent one. Accuracy, brand voice, benefit claims, and broader content scope are not sufficient reasons.

## Small-text decisions

| Element | Keep when | Remove when |
| --- | --- | --- |
| Eyebrow / overline | Required taxonomy, status, or orientation | It restates the title or adds atmosphere |
| Subtitle / lead | Omission blocks understanding or action | It fills space or repeats the title |
| Helper text | It enables a control or prevents an error | It narrates the obvious |
| Breadcrumb / metadata | It changes orientation or a decision | It is decorative or boilerplate |

Accessibility content, form labels, validation messages, essential navigation, legal/regulatory copy, and domain terminology are valid exceptions.

## Final UI pass

1. Read each heading without nearby small text. If it still works, delete the line unless its job is clear.
2. Scan repeated cards, sections, and pages for boilerplate labels or descriptions.
3. Check whether navigation, category labels, headings, and descriptions repeat one idea.
4. Keep only copy that helps the user understand, decide, navigate, act, or recover from an error.

When in doubt, omit the line and let the content earn its place.
