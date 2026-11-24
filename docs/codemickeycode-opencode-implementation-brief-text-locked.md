# OpenCode implementation brief — codemickeycode.com homepage

## Goal

Update the **existing** personal website's homepage to match the **visual direction** of the attached reference image (`codemickeycode-editorial-reference-v2.png`): warm, spacious editorial design, with industrial-café atmosphere and subtle pen-and-ink illustrations representing my interests.

This is a **VISUAL-ONLY redesign** of the existing site. **DO NOT edit, rewrite, shorten, paraphrase, correct, delete, insert, or regenerate any existing website text.** The reference image provides styling and composition ideas only; its words are not replacement copy. Treat the live repository's existing text as locked.

The desired experience is a personal third space: **a place where visitors can settle in, reflect, think deeply, and find inspiration**. The design should be **intentional, purposeful, unhurried, clean, and personal**. My primary visitors are friends, people I meet at PyCon and other events, and potential employers.

## First: inspect before editing

1. Inspect the existing project, including `index.html`, `css/styles.css`, `js/site-chrome.js`, `js/main.js`, and any assets. Confirm the actual paths and how the website is built before choosing the implementation.
2. Check the current Git state and avoid overwriting unrelated edits. Prefer the current native stack (HTML/CSS/JS) rather than adding a frontend framework or unnecessary dependencies.
3. Use `codemickeycode-editorial-reference-v2.png` **only as a visual reference**. Do **not** turn the screenshot into a background, embed the whole image as a webpage, or extract blurry text from it.
4. Treat the **current checked-out repository files as the source of truth for ALL text**. Preserve all textual material exactly. You may move existing text blocks in the DOM only when necessary for layout, but their wording, punctuation, capitalization, formatting intent, headings, ordering within a block, and destinations must remain unchanged. Prefer a CSS-only solution when feasible.
5. Before modifying anything, record a baseline of visible text and link destinations in each file you plan to touch, so they can be compared against the result. The brief and the mockup must never override the site's actual copy.

## Visual direction

**Editorial minimalism × cozy industrial café × personal field journal.** The look should be closer to a beautifully laid-out independent journal than a cartoon-themed webpage or corporate tech portfolio.

- Warm ivory/paper background, espresso text, small terracotta and muted teal accents.
- Large, expressive **Instrument Serif** headings; legible **DM Sans** body/navigation; **Caveat** only for brief handwritten accents.
- Spacious layout, restrained decoration, thoughtful typography, comfortable reading measure, fine borders/rules, subtle natural-paper texture.
- Prefer a restrained **ink-etched / vintage editorial illustration** style (thin hand-drawn strokes, subtle hatching, muted washes), **not** the earlier brightly colored watercolor-cartoon style.
- Keep the page light and airy. Decorative art must frame content, not compete with or overlap it.

### Existing palette (reuse where possible)

| Token | Hex | Role |
| --- | --- | --- |
| Warm Paper | `#F6F1E8` | Main background |
| Espresso | `#3B302B` | Main text / outlines |
| Brick Terracotta | `#A65F49` | Warm accent / fine dividers |
| Ocean Teal | `#4E7C82` | Secondary accent / links |
| Warm Oak | `#C6A98C` | Soft warmth / highlights |
| Sea Glass | `#D6EAE5` | Optional soft background |

Aim for ~80% neutral surfaces with sparing accent color. Do not introduce a new bright palette.

## Non-negotiable: ALL website text is locked

**This request is for layout and decorative illustrations ONLY. Do not modify ANY existing website text.** This instruction overrides any other wording in this brief and any text visible in the reference image.

- Preserve **every** existing heading, paragraph, blockquote, label, button/CTA text, navigation label, footer line, and other visible text **verbatim**. Preserve punctuation, capitalization, numbers, names, taglines, and existing line breaks where they are intentionally authored.
- Specifically preserve the existing **Micaela Reyes** name, the exact tagline **“Code. Passion. Freedom. Making a Difference.”**, the existing professional positioning, the actual multi-paragraph introduction (including the sentence about turning organizational ambitions into working programs, systems, and communities), **all** existing wording in **“My why”**, the complete contact invitation, and existing footer copy.
- Keep **all** existing content, including the current section count. Do not add explanatory copy, subheadings, shortened intros, placeholder text, captions, lifestyle claims, project descriptions, or any replacement text simply to imitate the reference.
- Preserve text in navigation and working link destinations, image alt text, ARIA labels, document titles, meta descriptions, and other existing text-bearing attributes. Do not change link targets, even if the reference uses different labels.
- **Do not copy, transcribe, or adapt any text shown in the generated reference image.** The image is not a content specification. Its “Home / About / Blog / Projects / Notes,” the “My why” excerpt, and any other display wording are not instructions to edit the website. Use current repository text instead.
- If styling appears to require shortening, splitting, or simplifying the text, **modify the visual layout, line wrapping, size, or spacing instead**. CSS line wrapping is okay; editing actual HTML words or inserting manual `<br>` to force different phrasing is not.
- If a proposed design cannot work without changing copy, keep the original copy and report that design trade-off. Ask before making any copy changes in a separate task.
- Treat **content parity as a strict acceptance gate**: compare existing and updated text after implementation, not just the visual screenshot. If text changes unintentionally, restore it.

## Homepage composition

Use the reference as a **direction, not a pixel-perfect specification**. Adapt to current real content and responsive constraints.

1. **Header**: clean and quiet; retain existing site brand and actual navigation labels/links. Keep it functional on mobile. Do not replace the wordmark with an image or an unapproved logo.
2. **Hero**: visually emphasize the **existing** name, tagline, professional positioning, **all currently authored introduction paragraphs**, and the existing work CTA, using serif typography and a spacious editorial composition. **Do not condense the introduction or change the CTA text.**
3. **My why**: visually restyle the existing section as an editorial reflection, with a fine horizontal rule and optional handwritten styling on its **existing label**. **Retain its complete text, including the blockquote, kicker, and supporting paragraph, verbatim.** The current dark full-width panel can be adapted to a warm-paper treatment if the resulting contrast is accessible.
4. **Contact**: retain the **exact current invitation text and contact link label**, changing only appearance or positioning. Avoid a visually heavy CTA if it compromises the calm mood.
5. Do **not** add fabricated project cards, blog posts, social links, or entire new sections just to fill the reference's visual space.

## Four illustrated corner motifs (important)

Create or integrate **four separate, high-quality, lightweight illustration assets** that share one coherent ink-drawing style. Use assets as independent image/SVG elements, not as part of a flattened page screenshot. Prefer original SVG/transparent illustrations that scale cleanly, with a small number of muted colors and appropriate detail for website sizes.

1. **Top left — greenery + brick**: trailing leafy vine partly overlaying a lightly faded, warm terracotta brick accent. Keep the brick area small and visually quiet.
2. **Top right — pottery + greenery + brick**: a small wooden industrial-style wall shelf with two or three handmade ceramic pieces and a few trailing leaves, against a subtle terracotta-brick accent. **No hanging lamp or light fixture.**
3. **Bottom left — ThinkPad + books + coffee + pottery**: a recognizable **black ThinkPad-style laptop** beside a short stack of books, a handmade ceramic coffee mug, and a small pottery/tool cup. Convey reading, coding, coffee, and pottery while keeping the arrangement compact and not overlapping text.
4. **Bottom right — travel and ocean exploration**: a compact **orange Deuter-style cycling backpack** (not a generic blue travel pack), snorkeling mask and snorkel, an open travel journal or small folded map, and perhaps a small handmade ceramic cup. **Do not include a camera.** Keep logos/brand marks out unless an authorized asset is provided.

**Art direction:** delicate brown/charcoal linework, light cross-hatching, small faded teal/terracotta/amber fills, and a restrained vintage editorial feel. Avoid emojis, flat clip-art icons, huge cartoon stickers, brightly saturated watercolor, and stock-image collages.

**Important feasibility boundary:** If you cannot produce quality illustrations with available tools/assets, do not substitute generic icons or approximate brand logos. Implement the layout with clearly named replaceable illustration slots, use simple stylistically appropriate SVGs only if they genuinely look good, and report which assets still need illustration work. Do not claim visual fidelity without reviewing the actual output. Decorative images should have no embedded user-visible copy or invented captions.

## Responsive and accessible design

- At approximately **1440px**: use a generous editorial layout with enough edge space for the four motifs, without letting them sit on top of text.
- At approximately **768px**: simplify illustration size and placement, prioritizing readability and navigation.
- At approximately **375px**: show at most one or two small decorative motifs, or omit decorative art entirely; the name, tagline, links, and reflections must remain readable. No sideways scrolling.
- Use fluid type sizes and spacing (`clamp()` where appropriate), consistent max-width containers, and accessible heading hierarchy.
- New decorative illustrations must have empty `alt` text / `aria-hidden` where appropriate. If any **new** meaningful image is added, use descriptive alt text. **Do not change alt text on existing images.**
- Maintain sufficient text contrast; visible keyboard focus; functional mobile menu; readable tap targets.
- Respect `prefers-reduced-motion`. Avoid parallax, fixed decorative overlays during scroll, slow effects, or unnecessary animation.
- Optimize asset sizes and preserve quick static-site loading.

## Implementation boundaries

- Keep the site lightweight; use HTML/CSS/JS already in the repository unless a dependency is demonstrably necessary.
- Make focused changes. Preserve unaffected pages (`work.html`, `cv.html`, blog links, etc.) and existing behavior.
- Do not hard-code decorative art with absolute positioning that breaks at other viewport widths. Anchor it to logical sections, test overflow, and keep it out of the reading path.
- Do not modify public-facing facts, add unverifiable claims, or silently publish.
- Do not push or deploy automatically. Prepare implementation for my review.

## Verification and acceptance criteria

1. On desktop, the layout feels clearly inspired by the supplied **updated** reference: spacious large serif name, expressive styling of existing tagline, quiet editorial hierarchy, subtle brick/café atmosphere, and four corner motifs **without a lamp or camera**.
2. **Text parity is exact**: no website copy or text-bearing attribute was altered in any changed file; the site still has all original headings, intro paragraphs, tagline, blockquote, supporting paragraphs, CTA labels, navigation, footer, and links. Reference-image text was ignored.
3. It looks like **my actual existing website**, not a generic re-created template, and preserves all existing link destinations.
4. The illustrations are stylistically consistent and **visually subordinate** to content.
5. At tablet and mobile widths, no illustrations overlap text, navigation, or buttons; no horizontal scroll; no tiny unreadable text.
6. Check all internal navigation and external links, image loading, keyboard use, and basic accessibility.
7. If browser/screenshot tooling is available, generate and inspect desktop and mobile screenshots and revise based on what you see. If visual review isn't possible, say so rather than claiming it was checked.

## Handoff

After implementation, give me:

- A short summary of **what changed** and **what stayed the same**, explicitly confirming **all existing text was preserved verbatim**.
- The files changed, especially any illustration assets.
- How to preview the site locally.
- What you tested and what you did **not** verify, including the method used for the text/link parity audit.
- Any design decisions or asset limitations that need my review.

**Implement this as a reviewable local change, not an automatic deployment. The changes are VISUAL-ONLY; DO NOT CHANGE ANY EXISTING TEXT.**

### Pre-delivery text-preservation check

Compare before/after source text and rendered visible text for each edited page. Check all text nodes, headings, buttons, navigation labels, links, alt attributes, `aria-label`, `<title>`, and meta descriptions. Check that every existing URL stays the same. If you do not have a robust automated DOM diff, manually review the relevant HTML diff and explicitly report what you checked. **No copy edits are authorized.**
