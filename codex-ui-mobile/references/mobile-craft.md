# Mobile craft

## Typography

- Prefer platform text styles or a token system that scales with the user's text-size settings.
- Start simple: one versatile family and a restrained set of weights is often enough for an app. Add a second family or more weights only when they have a defined role and remain coherent across screens.
- Choose custom fonts for a real brand reason and verify weights, scripts, numerals, and accessibility scaling. Keep system UI legible if the display face is expressive.
- Create hierarchy through position, space, weight, and meaningful size contrast. Do not rely on tiny gray labels.
- Avoid fixed-height text containers. Test long names, localization expansion, multiline labels, and the largest supported accessibility sizes.
- Use tabular numerals for timers, measurements, prices, and changing values.
- Prevent iOS/web-view input zoom and platform-specific text clipping when the chosen framework makes those relevant.

## Color and themes

- Derive the palette from brand, domain, imagery, or semantic state. Do not default to purple/cyan gradients or generic beige.
- Separate semantic roles from raw colors: background, elevated surface, primary text, secondary text, separator, action, focus, success, warning, danger.
- Support light and dark appearances deliberately. Dark mode needs tuned surfaces and chroma, not simple inversion.
- Respect platform high-contrast settings and avoid color-only status cues.
- System bars, keyboard areas, sheets, and overscroll regions should belong to the same color world as the screen.

## Safe areas and device geometry

- Apply safe-area insets at the correct container level. Avoid double-padding nested safe-area components.
- Keep important content and controls clear of notches, Dynamic Island/cutouts, home indicators, gesture regions, rounded corners, and system bars.
- Edge-to-edge imagery can extend behind insets; interactive and readable content still needs protection.
- Handle keyboard appearance intentionally: focused fields remain visible, actions stay reachable, and content does not jump unpredictably.

## Touch and controls

- Maintain at least the platform's comfortable target size—commonly 44×44 points on iOS and 48×48 dp on Android—even when the visible icon is smaller.
- Leave enough separation to avoid accidental activation. Dense lists can have large row targets without oversized visuals.
- Prefer native controls for switches, pickers, dates, text input, menus, sheets, and alerts unless custom behavior clearly improves the product.
- Make destructive, disabled, loading, selected, pressed, and error states unmistakable.
- Icon-only actions need accessible labels; unfamiliar actions also need visible affordance or contextual explanation.
- Every interactive element must react in a way appropriate to its state. A pressed treatment is baseline; add haptic or motion feedback only when it communicates something useful.

## Surfaces, icons, and media

- Use cards for genuine containment or independent objects, not as the default wrapper for every group.
- Use a small, named radius scale rather than arbitrary values. Coordinate nested radii with padding and device geometry; continuous/squircle curves are appropriate on Apple platforms when the framework supports them. Avoid both a different radius on every component and one radius forced onto controls with different geometry.
- Use elevation sparingly and according to platform conventions. Borders and background shifts often communicate grouping more quietly.
- Use one icon language with platform-appropriate symbols where users expect them. Do not mix outline, filled, emoji, and illustration styles arbitrarily.
- Give imagery a consistent crop, treatment, and subject. Design placeholders, loading, failure, and permission-denied states for user media.
- Use a small elevation system tied to actual layers (for example, content, floating control, modal) rather than decorating components with unrelated shadows.

## Product identity

- Express identity through a few durable decisions: type voice, color relationship, content treatment, motion character, and one signature component.
- Keep platform behavior familiar while customizing proportions, hierarchy, imagery, and product-specific components.
- A branded app is not one where every control is custom. It is one where the whole system makes consistent, product-specific choices.
