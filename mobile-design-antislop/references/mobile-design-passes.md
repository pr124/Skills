# Mobile anti-slop: design-pass router

Use the smallest pass that matches the user's intent. These are disciplines inside this skill, not separate skills the user must name.

| User intent or evidence | Pass | Primary job |
| --- | --- | --- |
| New feature or unclear flow | Shape | Define user, job, sequence, states, platform behavior, and success before styling |
| "Is this good?" or design review | Critique | Evaluate hierarchy, comprehension, cognitive load, trust, platform fit, and task success |
| Too safe, bland, or generic | Bolder | Strengthen proportion, contrast, pacing, product signature, and commitment without adding random effects |
| Too loud, busy, or game-like | Quieter | Reduce competing emphasis while preserving hierarchy and useful feedback |
| Too much UI or too many steps | Distill | Remove or combine non-essential elements, copy, screens, and decisions without hiding core capability |
| Type feels weak or inconsistent | Typeset | Repair text styles, hierarchy, measure, weights, numerals, scaling, and localization resilience |
| Palette feels default or muddy | Colorize | Establish semantic roles and a product-specific color logic with accessible light/dark behavior |
| Spacing or composition feels off | Layout | Repair grouping, rhythm, reachability, density, insets, and phone/tablet composition |
| Moving across phone, tablet, or OS | Adapt | Preserve the task while changing navigation, structure, controls, and platform conventions |
| Interaction feels dead or unclear | Animate | Add only purposeful, interruptible motion and appropriate feedback; verify runtime performance |
| Product is competent but forgettable | Delight | Add one earned moment of personality after the baseline interaction is stable |
| Labels or states are confusing | Clarify | Rewrite actions, permissions, errors, empty states, and helper copy for the next decision |
| Real data will break the screen | Harden | Stress long text, large values, missing data, offline, permissions, errors, interruptions, and recovery |
| First-run or activation is weak | Onboard | Get users to first value with contextual education, honest permissions, progress, skip/recovery paths |
| Scrolling, startup, or gesture is slow | Optimize | Profile before changing; reduce work, media cost, overdraw, and thread contention without degrading UX |
| Near release | Polish | Inspect system consistency, every reachable state, accessibility, platform conformance, and device evidence |

## Pass rules

- Diagnose before applying a pass. "Make it better" normally starts with Critique, then routes findings to one or two focused passes.
- Do not run every pass. More transformations do not produce more taste.
- Preserve the design contract. Bolder, Colorize, Delight, and Animate strengthen documented language; they do not silently invent a second system.
- Bolder is usually for acquisition, onboarding, paywalls, feature moments, and consumer content—not dense settings or long-session operational screens.
- Delight follows clarity. Never add celebration, streaks, haptics, or playful copy to conceal weak flow or missing feedback.
- Distill removes friction and repetition, not required functionality, accessibility labels, recovery, legal text, or user control.
- Adapt changes structure and conventions rather than scaling pixels or hiding inconvenient features.
- Polish does not redesign. If the premise or information architecture is wrong, return to Shape.

## Critique output

For a review, report evidence and priority rather than taste adjectives. Use:

- **P0:** blocks task completion, safety, accessibility, or release
- **P1:** materially harms comprehension, trust, conversion, platform behavior, or frequent use
- **P2:** noticeable inconsistency or resilience gap
- **P3:** fine craft improvement

Evaluate the rendered flow on:

1. task and navigation clarity
2. hierarchy and cognitive load
3. platform convention and native feel
4. design-system consistency and product identity
5. accessibility and reachability
6. state completeness and real-data resilience
7. motion, gesture, haptic, and runtime quality

Do not score merely to look systematic. Each finding needs a location, observed problem, user consequence, and concrete repair.

## Harden stress set

Exercise only relevant cases, but do not stop at the happy path:

- longest plausible localized title, name, unit, currency, date, and button label
- empty, one-item, many-item, partially loaded, stale, and offline content
- permission denied, authentication expired, payment failure, server error, retry, and cancellation
- keyboard open, accessibility text size, screen reader, reduced motion, dark mode, high contrast
- background/foreground interruption, orientation or window-size change, low-end device, slow network

The pass is complete when failure remains understandable, recoverable, and visually part of the same product.
