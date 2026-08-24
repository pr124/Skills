---
name: codex-ui-mobile
description: Design, implement, redesign, or review distinctive native mobile app interfaces for iOS and Android, including SwiftUI, UIKit, Jetpack Compose, React Native, Expo, and Flutter. Use when screens, flows, navigation, gestures, or motion must feel platform-aware and avoid generic AI app aesthetics. Do not use for mobile websites.
---

# Codex UI — Mobile

Create an app that feels designed for a hand, a platform, and a real task—not a desktop layout squeezed into a phone frame or a gallery of fashionable mobile components.

## Working posture

- Preserve the user's framework, product requirements, brand assets, and existing design system.
- Identify the target: iOS, Android, or intentionally adaptive. Do not silently impose iOS patterns on Android or vice versa.
- Inspect current screens, navigation, platform components, tokens, typography, insets, and interaction behavior before redesigning an existing app.
- If the project contains `DESIGN.md`, design tokens, or an established component library, read and follow them. Strengthen the existing language before expanding it.
- Infer a coherent direction from the product and audience. Ask only when a missing platform or product choice would materially change the result.
- Use native controls and conventions as the baseline, then customize where it creates product identity or improves the task.
- Never invent customer proof, health/financial claims, metrics, or product capabilities.

## Read the relevant guidance

- For any new screen or flow, read [references/mobile-direction-and-structure.md](references/mobile-direction-and-structure.md).
- For typography, color, surfaces, safe areas, and component craft, read [references/mobile-craft.md](references/mobile-craft.md).
- For gestures, motion, haptics, accessibility, and device verification, read [references/mobile-interaction-and-quality.md](references/mobile-interaction-and-quality.md).
- For new apps, substantial redesigns, or recurring UI work, read [references/design-system-contract.md](references/design-system-contract.md) and create or update the project's design contract when it will prevent drift.
- For a tiny edit, preserve the existing direction and read only the relevant reference.

## Core workflow

1. **Gather evidence.** Identify the user, primary task, frequency, context of use, target platforms, framework, and existing design language.
2. **Choose a native direction.** Define the app's voice, density, navigation model, color and type logic, and one product-specific signature. State which platform conventions remain native.
3. **Lock the system.** Reuse or establish semantic tokens for type, spacing, color, shape, elevation, icons, motion, and haptics. Record decisions when the project will receive more UI work.
4. **Structure the flow.** Design the route, back behavior, keyboard behavior, interruptions, permissions, offline/loading/error paths, and empty states before decorating screens.
5. **Build complete screens.** Respect safe areas, system bars, dynamic text, touch targets, themes, input modes, and relevant component states.
6. **Verify on device-sized renders.** Exercise the primary path and edge states on representative iOS and/or Android sizes. For interaction or performance work, use a real device or release-like build when available.

## Anti-generic gate

Treat these as warning signs when they appear without product or platform evidence:

- a huge gradient welcome header, floating glass cards, glowing blobs, or purple/cyan accents used as instant "premium"
- every group wrapped in a rounded card, every control made a pill, or every screen beginning with an oversized title and generic subtitle
- a desktop dashboard shrunk to one column, tiny low-contrast text, hover-dependent actions, or hamburger navigation copied from the web
- arbitrary progress rings, streaks, emoji decoration, fake achievements, or charts unrelated to the core task
- custom versions of standard sheets, pickers, switches, alerts, or navigation that are less usable than the platform control
- motion and haptics on every tap, or decorative gestures with no visible alternative

These patterns are not universally forbidden. They need a clear relationship to the brand, task, or platform rather than being selected by reflex.

## Copy discipline

Let a clear screen title stand alone. Add supporting copy only when it improves orientation, decision-making, error prevention, permissions, onboarding, or recovery. Use concise action labels and platform-familiar terminology. Do not add friendly filler to make sparse screens feel designed.

## Completion standard

The app should feel native to its target platform while remaining recognizably its own product. It must be usable one-handed where appropriate, resilient to text and content variation, clear in every reachable state, accessible, and smooth on realistic hardware.
