# Web anti-slop: craft and systems

## Typography

- Choose type for the product's voice and reading conditions, not because it is a fashionable default. Preserve established fonts during ordinary redesigns.
- Use one capable family well, or pair families with clearly different jobs. A decorative display face must not leak into dense controls.
- Create visible hierarchy through meaningful jumps in size, weight, space, and measure. Tiny differences create visual mud.
- Keep body text comfortably readable, headings balanced, and paragraphs to a sensible measure. Prevent orphaned single words when practical.
- Use tabular numerals for columns, timers, prices, and changing metrics. Align numbers by meaning and units.
- Do not make secondary text so faint or small that hierarchy becomes illegibility.
- Check long labels, localization expansion, user-supplied content, and browser zoom.

## Color

- Derive color from brand, domain, imagery, materials, or product meaning. Do not reach for generic purple, cyan, or warm sand by reflex.
- Define semantic roles such as canvas, surface, text, muted text, border, action, focus, success, warning, and danger. Components consume roles rather than raw color values.
- Use color to encode action, state, category, or hierarchy. Never use color as the only carrier of meaning.
- Keep the dominant palette restrained unless a committed, colorful brand direction is part of the premise.
- For new web systems, OKLCH is useful for perceptually even ramps. Check real rendered contrast; mathematical harmony does not guarantee usability.
- Dark mode is its own composition. Establish depth through surface lightness and tuned chroma rather than inverting light mode or adding heavy shadows.

## Surfaces and depth

- Not every group needs a card. Try spacing, alignment, typography, and a single divider first.
- Match nested radii: the outer radius should account for the inner radius and padding. Do not mix unrelated radius values on one surface.
- Use borders for containment, shadows for elevation, and background shifts for grouping. Do not apply all three without a reason.
- Keep shadows chromatically related to the environment and subtle enough that the surface still belongs to the page.
- Avoid glassmorphism when translucency has no spatial or brand logic.
- Add texture or image treatment only when it reinforces the chosen world. One well-directed material is stronger than many stock effects.

## Icons, imagery, and data

- Use one coherent icon family and stroke language per surface. Prefer familiar symbols for familiar actions.
- Give icon-only controls accessible names and tooltips where discovery matters. Nudge optically asymmetric glyphs when geometric centering looks wrong.
- Use imagery with a consistent subject, crop, color treatment, and point of view. Generic stock images make a custom layout feel generic.
- Keep aspect ratios stable so content does not shift while media loads.
- Label charts directly when possible. Use appropriate scales, units, baselines, and empty states; never fabricate data to beautify a dashboard.

## Copy

- Write labels as actions or clear nouns. Avoid vague buttons such as "Explore" when a precise action exists.
- Keep only text that helps users understand, decide, navigate, act, or recover.
- Empty and error states should explain what happened and provide the next useful action without forced cheerfulness.
- Do not repeat the same idea in navigation, eyebrow, title, lead, and card copy.

## System integrity

- Reuse existing tokens and primitives before introducing new ones.
- Keep primitive values separate from semantic tokens when creating a system from scratch.
- Make exceptions explicit and rare. A design feels authored when recurring decisions have a reason and one-off decisions are intentional.
- Do not install a component library or replace the user's stack solely to achieve a visual direction.
