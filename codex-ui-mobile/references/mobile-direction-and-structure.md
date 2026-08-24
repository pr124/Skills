# Mobile direction and structure

## Establish the premise

Write a compact internal brief before styling:

```text
Product:      what the app enables
User/context: who uses it, where, how often, and with which hand/input
Platform:     iOS, Android, or intentionally adaptive
Core loop:    the action users repeat and the feedback it needs
Voice:        2–3 precise traits, with an explicit counter-trait
Signature:    one product-specific visual or interaction element
Rejecting:    3 likely mobile-template defaults and the alternative
```

Good signatures emerge from the job: a tactile ingredient timeline, a live training interval rail, a location-aware field card, or a compare gesture that reduces real work. Avoid a signature that is merely a decorative shape applied to every screen.

## Platform register

### iOS

- Follow iOS expectations for navigation hierarchy, back behavior, safe areas, sheets, tab bars, pickers, context menus, typography scaling, and system materials.
- Preserve edge-swipe back and system gestures when the navigation model supports them.
- Use large titles, translucent materials, and springy physical motion only when appropriate to the content and app structure—not as compulsory iOS decoration.
- For iOS 26-era work, prefer current system structures and controls so the platform supplies the new appearance naturally. Treat Liquid Glass as a functional control/navigation layer above content, not as a texture for every card. Use custom glass sparingly for important interactive elements, keep glass layers coherent, and preserve legibility over changing content. See Apple's [Liquid Glass design guidance](https://developer.apple.com/videos/play/wwdc2025/219/) and [SwiftUI adoption guidance](https://developer.apple.com/videos/play/wwdc2025/323/).

### Android

- Follow Android expectations for system back, predictive back where supported, top app bars, navigation bars/rails, sheets, snackbars, switches, typography scaling, and edge-to-edge layout.
- Respect dynamic system bars and keyboard/inset behavior.
- Use Material components as reliable interaction primitives without making the app look like an untouched starter theme.

### Adaptive

- Share product identity, information architecture, and semantic tokens while allowing navigation, controls, spacing, and motion to follow each platform.
- Do not force pixel-identical screens when platform-native behavior differs.
- Document intentional differences so they remain consistent.

## Flow before screen

- Map entry, primary action, confirmation, interruption, cancellation, error, recovery, and return path.
- Define back behavior at each level. Users should know whether back dismisses, steps backward, or leaves the task.
- Keep the core task close to the natural entry point. Avoid ornamental onboarding before users see value.
- Ask for permissions in context, after explaining the benefit. Design denial and later recovery paths.
- Preserve drafts and user input across interruptions when the task warrants it.
- Plan offline, stale, loading, and partial-data behavior for network-dependent flows.

## Prioritize by value and trust

Polish is not evenly valuable. Identify where users make trust and commitment decisions, then spend the strongest art direction and validation there.

- For a consumer subscription app, this often means the store icon and screenshots, onboarding, paywall, first successful use, and the core loop.
- For a utility or productivity app, prioritize the repeated task, data entry, recovery, and the moment a result becomes useful.
- For a regulated or high-trust app, prioritize identity, permissions, explanations, confirmation, error prevention, and recovery.
- Use funnel or task evidence when available. Do not beautify a paywall while leaving the path into it incoherent.
- Keep low-value settings consistent and clear; they do not need the same visual spectacle as the product's defining moment.

## Navigation

- Use tabs for a small set of peer destinations users switch between frequently. Do not use a tab for a one-off action or hide deep hierarchy inside tabs.
- Use navigation stacks for drill-down and a sheet for a focused temporary task. A sheet should not become an entire parallel app.
- Keep the primary action reachable, but do not turn every screen into a floating-action-button composition.
- On tablets and foldables, adapt structure: split views, navigation rails, persistent secondary panes, and useful multi-column layouts can replace stretched phone screens.
- Never make essential functionality discoverable only by gesture.

## Screen composition

- Design around thumb reach, content priority, and keyboard occupation—not just the empty device frame.
- Group with spacing and alignment before adding cards. Mobile cards consume scarce width and often create nested-container clutter.
- Use one dominant scroll direction. Nested scrolling needs a clear interaction reason.
- Keep persistent chrome modest so content has room. Avoid stacking a system bar, huge title, segmented control, banner, and floating card before the first useful item.
- Use density appropriate to frequency: repeated operational work can be compact; occasional guided tasks can be spacious.
- Consider landscape, tablets, foldables, and accessibility text sizes when they are plausible contexts, not afterthoughts.
