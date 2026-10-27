---
name: ui-ux-pro-max
description: "UI/UX design intelligence for web and mobile. 50+ styles, 161 color palettes, 57 font pairings, 161 product types, 99 UX guidelines, 25 chart types across 10 stacks. Use for design, review, fix, optimize UI/UX code."
---

# UI/UX Pro Max - Design Intelligence

Comprehensive design guide for web and mobile applications.

## When to Apply

**Must Use:**
- Designing new pages (Landing Page, Dashboard, Admin, SaaS, Mobile App)
- Creating or refactoring UI components
- Choosing color schemes, typography, spacing, layout
- Reviewing UI code for UX, accessibility, or visual consistency
- Implementing navigation, animations, or responsive behavior

**Skip:**
- Pure backend logic
- API or database design only
- Performance optimization unrelated to interface
- Infrastructure or DevOps work

## Rule Categories by Priority

| Priority | Category | Impact | Domain |
|----------|----------|--------|--------|
| 1 | Accessibility | CRITICAL | `ux` |
| 2 | Touch & Interaction | CRITICAL | `ux` |
| 3 | Performance | HIGH | `ux` |
| 4 | Style Selection | HIGH | `style`, `product` |
| 5 | Layout & Responsive | HIGH | `ux` |
| 6 | Typography & Color | MEDIUM | `typography`, `color` |
| 7 | Animation | MEDIUM | `ux` |
| 8 | Forms & Feedback | MEDIUM | `ux` |
| 9 | Navigation Patterns | HIGH | `ux` |
| 10 | Charts & Data | LOW | `chart` |

## Quick Reference

### 1. Accessibility (CRITICAL)

- Contrast 4.5:1 minimum for normal text
- Visible focus rings on interactive elements
- Descriptive alt text for meaningful images
- aria-label for icon-only buttons
- Tab order matches visual order

### 2. Touch & Interaction (CRITICAL)

- Min touch target 44×44pt (iOS) / 48×48dp (Android)
- Minimum 8px gap between touch targets
- Use click/tap for primary interactions
- Disable button during async operations

### 3. Performance (HIGH)

- Use WebP/AVIF, responsive images (srcset)
- Lazy load non-critical assets
- Reserve space for async content (CLS < 0.1)
- Split code by route/feature

### 4. Style Selection (HIGH)

- Match style to product type
- Use SVG icons (Lucide, Heroicons), not emojis
- Consistent style across all pages
- Respect platform idioms (iOS HIG vs Material)

### 5. Layout & Responsive (HIGH)

- Mobile-first breakpoints (375/768/1024/1440)
- Minimum 16px body text on mobile
- 4pt/8dp incremental spacing system
- Consistent max-width on desktop

### 6. Typography & Color (MEDIUM)

- Line-height 1.5-1.75 for body text
- Consistent type scale (12/14/16/18/24/32)
- Semantic color tokens (not raw hex)
- Dark mode: desaturated/lighter tonal variants

### 7. Animation (MEDIUM)

- 150–300ms for micro-interactions
- Use transform/opacity only
- Show skeleton when loading > 300ms
- Respect prefers-reduced-motion

### 8. Forms & Feedback (MEDIUM)

- Visible label per input (not placeholder-only)
- Error below related field
- Loading then success/error state on submit
- Auto-dismiss toasts in 3-5s

### 9. Navigation Patterns (HIGH)

- Bottom navigation max 5 items
- Back navigation must be predictable
- All key screens reachable via deep link
- Current location visually highlighted

### 10. Charts & Data (LOW)

- Match chart type to data type
- Use accessible color palettes
- Provide table alternative for charts
- Always show legend near the chart

## How to Use

### Step 1: Analyze Requirements

- **Product type**: Tool, Productivity, Entertainment, hybrid
- **Target audience**: Age group, usage context
- **Style keywords**: minimal, dark mode, vibrant, etc.
- **Stack**: React, Next.js, Vue, etc.

### Step 2: Generate Design System

> Run from this skill's folder (base dir). On Windows use `py` if `python` is not available.

```bash
python scripts/search.py "<product_type> <industry> <keywords>" --design-system -p "Project Name"
```

### Step 3: Domain Searches (as needed)

```bash
python scripts/search.py "<keyword>" --domain <domain> -n <max_results>
```

**Domains:** `product`, `style`, `color`, `typography`, `landing`, `chart`, `ux`, `google-fonts`, `react`, `web`, `prompt`

### Step 4: Stack Guidelines

```bash
python scripts/search.py "<keyword>" --stack react-native
```

## Search Reference

| Domain | Use For |
|--------|---------|
| `product` | Product type recommendations |
| `style` | UI styles, colors, effects |
| `typography` | Font pairings, Google Fonts |
| `color` | Color palettes by product type |
| `landing` | Page structure, CTA strategies |
| `chart` | Chart types, library recommendations |
| `ux` | Best practices, anti-patterns |
| `react` | React/Next.js performance |
| `web` | App interface guidelines |

## Pre-Delivery Checklist

- [ ] No emojis as icons (use SVG)
- [ ] All touch targets ≥44pt
- [ ] Primary text contrast ≥4.5:1 (light + dark)
- [ ] Micro-interaction timing 150-300ms
- [ ] Safe areas respected for fixed elements
- [ ] Reduced motion supported
- [ ] Tested on 375px and landscape

## Resources

- shadcn/ui: https://ui.shadcn.com
- Tailwind CSS: https://tailwindcss.com
- Radix UI: https://radix-ui.com
