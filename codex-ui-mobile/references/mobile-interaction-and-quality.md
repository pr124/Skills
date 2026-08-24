# Mobile interaction and quality

## Gestures and feedback

- Make direct manipulation track the finger continuously. Gestures should be interruptible and settle from current position and velocity.
- Define activation thresholds, direction locking, cancellation, and conflict with scrolling or system gestures.
- Provide a visible alternative for swipe, drag, long-press, and other hidden gestures when the action is essential.
- Press feedback should be immediate. Use platform-appropriate highlight, opacity, scale, ripple, or state change without making every tap theatrical.
- Preserve spatial continuity when elements move between screens, sheets, or expanded states.

## Motion

- Animate to confirm, orient, preserve continuity, or explain cause and effect.
- Do not animate elements that should respond instantly or whose movement distracts from repeated work.
- Use platform motion primitives and keep frame-by-frame work off overloaded application threads. In React Native/Expo, gesture-linked animation belongs on the UI runtime when the stack supports it.
- Prefer transforms and opacity over expensive layout or blur animation when they communicate the same transition.
- Keep exits shorter or quieter than entrances. Avoid automatic stagger on every list and repeated hero animation on routine navigation.
- Respect reduced-motion settings and keep a static feedback cue.

## Haptics

- Use haptics for meaningful confirmation, selection boundaries, errors, or physical transitions—not every tap.
- Match intensity to consequence and platform convention. A destructive confirmation should not feel like a light picker tick.
- Do not use haptics as the only feedback channel, and respect device/user settings.

## Accessibility

- Every control exposes a concise name, correct role, value/state, and logical traversal order.
- Support screen readers, switch/keyboard input where applicable, text scaling, bold text, increased contrast, reduced motion, and color-vision differences.
- Group related content for useful announcements; do not force users through every decorative icon.
- Announce important asynchronous outcomes and focus the next useful element after modal transitions or validation failures.
- Keep targets comfortable and do not disable platform text scaling to protect a fragile layout.

## Performance and resilience

- Judge scroll and gesture quality on realistic hardware and a release-like build when possible. Simulator smoothness is not sufficient evidence.
- Avoid unnecessary re-rendering during gestures, oversized media, unbounded effects, and long blocking work on the main/UI thread.
- Design skeletons only when structure is stable; otherwise use honest progress or a quiet loading state.
- Preserve useful cached content and communicate stale/offline state instead of replacing the entire app with a spinner.
- Handle app backgrounding, rotation, interruptions, and process restoration where the workflow can lose meaningful work.

## Device verification

For non-trivial work:

1. Run the primary path on representative small and large phone sizes for each target platform.
2. Test the real keyboard, safe-area behavior, back gesture/button, sheets, tabs, and system bars.
3. Exercise loading, offline, empty, error, permission-denied, long-content, and accessibility-text states that can occur.
4. Test with a screen reader and reduced motion; inspect contrast in light and dark appearance.
5. Slow interactions down mentally or with tooling and fix discontinuities, clipped layers, incorrect hit areas, and gesture conflicts.
6. Run the project's relevant build, static analysis, lint, and tests.

Automated checks expose defects but do not prove the app feels native or authored. Inspect the rendered screens and the complete interaction path.
