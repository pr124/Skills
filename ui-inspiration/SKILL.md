---
name: ui-inspiration
description: Use when designing, redesigning, or visually polishing an application interface and external component or interaction references could improve the result. Do not use for non-visual coding work.
---

# UI Inspiration

Use the reference shelf to find a strong starting point, then adapt it to the application's existing design language. Inspiration should make the interface more intentional, not turn it into a collage.

## Apply lightly

1. Inspect the existing components, design tokens, framework, platform conventions, and nearby screens first.
2. Consult only the sources relevant to the task; do not browse every site or delay a tiny change for unnecessary research.
3. Choose patterns that suit the product and combine into one coherent direction.
4. Adapt them to the project's primitives, accessibility requirements, responsive behavior, interaction states, and performance constraints.

## Reference shelf

| Need | Sources |
| --- | --- |
| Components and visual patterns | [Beautiful UI](https://beautifului.dev), [BeUI](https://beui.dev), [Rare UI](https://rareui.com), [shadcn/ui](https://ui.shadcn.com), [COSS UI](https://coss.com/ui), [ReUI](https://reui.io/components) |
| Transitions and interaction motion | [Transitions](https://transitions.dev), [You Don't Need Animations](https://emilkowal.ski/ui/you-dont-need-animations) |
| Design-system and quality checks | [UI Skills](https://ui-skills.com), [Design System Checklist](https://designsystemchecklist.com) |

Prefer one to three relevant sources. Use the application's own design system as the primary source of truth.

## Boundaries

- For native mobile or desktop apps, treat web examples as visual or interaction inspiration only; preserve native controls and platform behavior.
- Before copying source code, verify its license, dependencies, and compatibility. Otherwise recreate the underlying pattern. Do not copy branding, content, or proprietary assets.
- Reject attractive patterns that conflict with the product, established system, or user task.
- Do not activate this skill for backend work, API bugs, tests, infrastructure, or other requests without a visual interface decision.

## Common mistakes

- Browsing the entire shelf instead of selecting a relevant source.
- Installing a component library for one small pattern.
- Mixing unrelated aesthetics across a single interface.
- Copying a demo literally instead of adapting its hierarchy, states, and behavior.

Example: for an existing settings page, inspect its form primitives first, compare only relevant settings or navigation patterns, then implement the chosen idea with the project's current tokens and components.
