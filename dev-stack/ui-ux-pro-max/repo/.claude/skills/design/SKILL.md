---
name: design
description: "Unified design skill: brand identity, design tokens, UI styling, logo generation, corporate identity programs, HTML presentations, banner design, icon design, and social photos. Actions: design, create, generate, build."
metadata:
  author: claudekit
  version: "2.1.0"
license: MIT
---

# Design

Unified design skill: brand, tokens, UI, logo, CIP, slides, banners, social photos, icons.

## When to Use

- Brand identity, voice, assets
- Design system tokens and specs
- UI styling with shadcn/ui + Tailwind
- Logo design and generation
- Corporate identity program (CIP) deliverables
- Presentations and pitch decks
- Banner design for social media, ads, web, print
- Social photos for multiple platforms

## Sub-skill Routing

| Task | Sub-skill |
|------|-----------|
| Brand identity, voice, assets | `brand` |
| Tokens, specs, CSS vars | `design-system` |
| shadcn/ui, Tailwind, code | `ui-styling` |
| Logo creation | Logo (built-in) → `references/logo-design.md` |
| CIP mockups | CIP (built-in) → `references/cip-design.md` |
| Presentations | Slides (built-in) → `references/slides.md` |
| Banners, covers | Banner (built-in) → `references/banner-sizes-and-styles.md` |
| Social photos | Social Photos (built-in) → `references/social-photos-design.md` |
| SVG icons | Icon (built-in) → `references/icon-design.md` |

## Logo Design

55+ styles, 30 color palettes, 25 industry guides.

```bash
# Generate design brief
python3 scripts/logo/search.py "tech startup modern" --design-brief -p "BrandName"

# Search styles/colors/industries
python3 scripts/logo/search.py "minimalist clean" --domain style
python3 scripts/logo/search.py "tech professional" --domain color

# Generate logo (white background)
python3 scripts/logo/generate.py --brand "TechFlow" --style minimalist --industry tech
```

## CIP Design

50+ deliverables, 20 styles, 20 industries.

```bash
# Generate brief
python3 scripts/cip/search.py "tech startup" --cip-brief -b "BrandName"

# Search domains
python3 scripts/cip/search.py "business card letterhead" --domain deliverable

# Generate mockups
python3 scripts/cip/generate.py --brand "TopGroup" --logo /path/to/logo.png --deliverable "business card"
```

## Slides

Strategic HTML presentations with Chart.js, design tokens, copywriting formulas.

Load `references/slides-create.md` for the creation workflow.

| Topic | File |
|-------|------|
| Creation Guide | `references/slides-create.md` |
| Layout Patterns | `references/slides-layout-patterns.md` |
| HTML Template | `references/slides-html-template.md` |
| Copywriting | `references/slides-copywriting-formulas.md` |

## Banner Design

22 art direction styles across social, ads, web, print.

Load `references/banner-sizes-and-styles.md` for complete reference.

| Platform | Size (px) |
|----------|-----------|
| Facebook Cover | 820 x 312 |
| Twitter/X Header | 1500 x 500 |
| LinkedIn Personal | 1584 x 396 |
| Instagram Post | 1080 x 1080 |
| Website Hero | 1920 x 600-1080 |

## Icon Design

15 styles, 12 categories. SVG text output.

```bash
python3 scripts/icon/generate.py --prompt "settings gear" --style outlined
python3 scripts/icon/generate.py --prompt "shopping cart" --style filled --color "#6366F1"
python3 scripts/icon/generate.py --prompt "cloud upload" --batch 4 --output-dir ./icons
```

## Social Photos

Multi-platform social image design: HTML/CSS → screenshot export.

Load `references/social-photos-design.md` for sizes and templates.

| Platform | Size (px) |
|----------|-----------|
| IG Post | 1080×1080 |
| IG Story | 1080×1920 |
| FB Post | 1200×630 |
| X Post | 1200×675 |
| LinkedIn | 1200×627 |
| YT Thumb | 1280×720 |

## References

| Topic | File |
|-------|------|
| Design Routing | `references/design-routing.md` |
| Logo Design Guide | `references/logo-design.md` |
| Logo Styles | `references/logo-style-guide.md` |
| Logo Color Psychology | `references/logo-color-psychology.md` |
| Logo Prompt Engineering | `references/logo-prompt-engineering.md` |
| CIP Design Guide | `references/cip-design.md` |
| CIP Style Guide | `references/cip-style-guide.md` |
| CIP Prompt Engineering | `references/cip-prompt-engineering.md` |
| CIP Deliverable Guide | `references/cip-deliverable-guide.md` |
| Slides Create | `references/slides-create.md` |
| Slides Strategies | `references/slides-strategies.md` |
| Slides Copywriting Formulas | `references/slides-copywriting-formulas.md` |
| Slides HTML Template | `references/slides-html-template.md` |
| Slides Layout Patterns | `references/slides-layout-patterns.md` |
| Slides Reference | `references/slides.md` |
| Banner Sizes | `references/banner-sizes-and-styles.md` |
| Social Photos | `references/social-photos-design.md` |
| Icon Design | `references/icon-design.md` |

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/logo/search.py` | Search logo styles, colors, industries |
| `scripts/logo/generate.py` | Generate logos with AI |
| `scripts/cip/search.py` | Search CIP deliverables, styles |
| `scripts/cip/generate.py` | Generate CIP mockups |
| `scripts/cip/render-html.py` | Render HTML presentation |
| `scripts/icon/generate.py` | Generate SVG icons |

## Prerequisites

**Python:** Use `python` instead of `python3` on Windows.

```bash
python --version
```

## Setup

```bash
export GEMINI_API_KEY="your-key"  # https://aistudio.google.com/apikey
pip install google-genai pillow
```
