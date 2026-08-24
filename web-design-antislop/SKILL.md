---
name: web-design-antislop
description: Design, implement, redesign, or review distinctive websites and web apps with production-grade visual craft. Use for landing pages, marketing sites, SaaS products, dashboards, portals, and responsive web interfaces when the result must avoid generic AI aesthetics. Do not use for native iOS or Android apps.
---

# Web Design Anti-Slop

Create a specific interface for this product, audience, and domain. Do not make a merely attractive arrangement of familiar AI-generated patterns.

## Working posture

- Preserve the user's stack, requirements, brand assets, and established design system.
- For an existing product, inspect representative screens, tokens, components, type, color, density, and interaction patterns before changing its visual language.
- For new work, infer a defensible direction from the product and content. Ask only when a missing choice would materially change the result.
- Make real decisions. Do not present a menu of vague styles unless the user requested exploration.
- Use real content when available. Never invent customers, metrics, testimonials, awards, or product capabilities.

## Route by surface

- **Persuade — marketing, pricing, launch, conversion:** prioritize narrative, proof, memorable composition, and action.
- **Operate — SaaS, dashboard, admin, tool:** prioritize task flow, information hierarchy, density, state clarity, and consistency.
- **Read — docs, guides, help, editorial:** prioritize comprehension, navigation, typography, code/media treatment, and long-form rhythm.
- **Experience — portfolio, gallery, showcase:** let the artifact lead while navigation, transitions, and controls recede.
- For any of these, read [references/direction-and-composition.md](references/direction-and-composition.md) using the matching register.
- **Any non-trivial build or redesign:** also read [references/craft-and-systems.md](references/craft-and-systems.md) and [references/interaction-and-quality.md](references/interaction-and-quality.md).
- **Small, isolated UI edit:** preserve the existing direction and read only the reference relevant to the edit.

## Core workflow

1. **Gather evidence.** Inspect the current product, content, assets, and constraints. Identify the primary user, task, and action.
2. **Choose a direction.** Define the visual premise, type voice, color logic, density, composition, and one product-specific signature. Name the generic defaults being rejected.
3. **Build the system.** Establish a small set of semantic tokens and reusable primitives. Let content and hierarchy determine components, not the other way around.
4. **Implement the full state.** Include responsive behavior and relevant hover, focus, active, loading, empty, error, success, disabled, and overflow states.
5. **Verify in the browser.** Inspect representative desktop and mobile widths and the primary interaction path. Fix visual and functional defects before handoff.

## Anti-generic gate

Treat these as warning signs when they appear without product evidence:

- purple-blue gradients, gradient text, glass panels, glowing blobs, or generic warm cream used as instant "premium"
- a pill-shaped eyebrow above every heading, followed by a large title and generic supporting sentence
- every section placed in a rounded card, or every landing page reduced to a hero plus a three-card grid
- interchangeable SaaS copy, fake social proof, decorative charts, or metrics that do not belong to the product
- arbitrary huge type, excessive rounded pills, uniform center alignment, and repeated icon-plus-heading-plus-copy tiles
- animation used to compensate for weak hierarchy or to make ordinary content feel "alive"

These patterns are not universally forbidden. They must be earned by the brand, content, interaction, or design system rather than selected by reflex.

## Copy discipline

Default page headers to `clear title + required navigation or action`. Add an eyebrow, subtitle, helper line, or metadata only when it provides orientation, meaning, decision support, error prevention, or required context. Do not narrate the obvious or fill space with reassuring adjectives.

## Completion standard

The result should have a coherent point of view, a recognizable relationship to its domain, a clear primary action, resilient states, accessible interaction, and no obvious template seams. A clean build is not proof of good design; inspect the rendered interface.
