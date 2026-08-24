# Web anti-slop: interaction and quality

## Interaction states

Every interactive element needs the states its behavior can reach:

- default, hover where supported, keyboard focus, active/pressed, and disabled
- loading or pending for asynchronous work
- success and error feedback where an outcome is not otherwise obvious
- selected, expanded, checked, dragged, or current when the control has that state

Feedback should be immediate and proportional. Preserve context after mutations, explain destructive consequences, and make recovery possible when practical.

## Motion

- Animate to confirm feedback, preserve spatial continuity, reveal relationships, or direct attention to a change.
- High-frequency interactions should feel immediate. Keep ordinary hover and press feedback short and restrained.
- Use transform and opacity when they express the transition; avoid animating layout-heavy properties casually.
- Entrances can carry more emphasis than exits. Do not stagger every list or replay theatrical page entrances during routine navigation.
- Interactive motion must be interruptible. Gesture-driven movement should respond to velocity and settle predictably.
- Never use `transition: all`.
- Respect `prefers-reduced-motion`; retain a static cue so motion is never the only feedback channel.

## Responsive and input quality

- Design for available space, content, and input capability—not device labels alone.
- Test narrow phone, intermediate/tablet, standard desktop, and a wide viewport when relevant.
- Use pointer and hover capability queries where interaction differs. Touch may exist on large screens.
- Maintain comfortable touch targets and spacing for coarse pointers without making mouse-oriented dense tools unnecessarily sparse.
- Avoid hover-only disclosure for essential information or actions.
- Check portrait and landscape where the product is likely to be used both ways.

## Accessibility floor

- Prefer semantic HTML and native controls. Add ARIA only when semantics are genuinely missing.
- Complete the primary flow with a keyboard. Focus order must follow visual and logical order.
- Make focus clearly visible and not obscured by sticky UI.
- Every control must expose a useful name, role, and state. Every form error must identify the field and recovery path.
- Meet contrast requirements for text, controls, states, and focus indicators. Do not encode status by color alone.
- Support zoom, text resizing, reflow, reduced motion, and forced-colors/high-contrast behavior as appropriate.

## Browser verification

For non-trivial work, render the actual implementation and inspect it. At minimum:

1. Verify the main route at representative narrow and wide widths.
2. Exercise the primary user path and keyboard path.
3. Inspect loading, empty, error, long-content, and overflow states that can occur.
4. Check hierarchy at a glance, then slow down and inspect alignment, radius, icon centering, wrapping, and motion.
5. Fix missing assets, layout shifts, unreadable text, clipped content, accidental scrollbars, and generic composition.
6. Run the project's relevant build, typecheck, lint, and tests.

Automated checks provide defect evidence, not taste. A page is complete only after the rendered result has been reviewed.
