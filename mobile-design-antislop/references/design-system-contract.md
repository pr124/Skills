# Mobile anti-slop: design-system contract

Use this reference for a new app, a substantial redesign, or a project where multiple screens will be generated over time. The goal is to make design decisions durable in the repository so later work does not drift.

## Discover before creating

Search first for `DESIGN.md`, design tokens, theme files, component libraries, typography declarations, icon dependencies, and motion helpers. If a system exists, use it as the boundary. Update it only when the requested work genuinely expands the design language.

Do not create a document for a tiny isolated edit or overwrite an established system with a generic template.

## Recommended `DESIGN.md` content

Record concrete project decisions, not design theory:

```markdown
# Product design contract

## Premise
- Product and audience
- Primary task / core loop
- Target platforms and minimum OS versions
- Voice and counter-trait
- Product-specific signature
- Explicit anti-patterns for this product

## Platform behavior
- Navigation model and back behavior
- iOS / Android differences
- Safe-area, keyboard, sheet, and system-bar behavior
- Phone, tablet, foldable, and orientation strategy

## Foundations
- Typography families, text styles, weights, scaling behavior, numeral styles
- Spacing scale and named layout gaps/insets
- Semantic color tokens for light, dark, and high-contrast appearances
- Radius/shape tokens and continuous-corner policy
- Border, separator, and elevation tokens
- Icon family and filled/outline state policy

## Components
- Buttons, fields, rows, cards, navigation, sheets, alerts, feedback
- Variants and every reachable state
- Rules for native controls versus custom components

## Motion and haptics
- Duration/spring tokens and their roles
- Gesture behavior and interruptibility
- Haptic events and intensity roles
- Reduced-motion behavior

## Accessibility and content
- Touch-target floor, text scaling, contrast, screen-reader grouping
- Localization and long-content expectations
- Empty, loading, offline, error, success, and permission states

## Verification
- Representative devices and themes
- Critical flows and edge cases
- Required visual, accessibility, and build checks
```

## Token discipline

- Use a coherent base spacing unit—commonly 4 or 8—then define named steps. Allow an exception only when platform geometry or optical alignment requires it.
- Components consume semantic color tokens, not hardcoded hex values. A small system may begin with background, surface, separator, primary text, secondary text, brand/action, focus, success, warning, and destructive roles; add roles when the product needs them rather than chasing a fixed count.
- Define a small shape scale and assign shapes by component role. Consistency matters, but a compact field, card, circular icon button, and full-width sheet do not need one identical radius.
- Use one coherent icon family per platform surface and a small elevation scale tied to real layer changes.
- Store interaction states beside component definitions so default, pressed, focused, disabled, loading, error, and selected behavior cannot drift.
- Keep primitive values separate from semantic roles when the system supports themes or multiple platforms.

## Research without imitation

When reference material is available, study several respected apps in the same category and the same flow. Extract relationships—density, navigation, disclosure, proof, input sequence, and feedback—not pixels or branded assets. Compare references with current platform guidance and the actual product constraints.

The output must remain specific to this product. Category conventions provide a usability baseline; the product premise and signature provide identity.

## Drift audit

For an established app, periodically inspect representative high-value screens for:

- arbitrary spacing, colors, radii, shadows, icons, or typography outside the contract
- missing pressed, disabled, loading, empty, error, success, offline, or permission states
- screen-specific custom controls that duplicate a platform or system component
- outdated platform structure or safe-area behavior
- low-contrast small text, clipped accessibility text, unstable numerals, or undersized targets
- generic decorative patterns that are not supported by the product direction

Fix root tokens or shared components before patching the same inconsistency screen by screen.
