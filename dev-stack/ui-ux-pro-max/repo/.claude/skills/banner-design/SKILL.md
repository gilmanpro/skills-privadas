---
name: banner-design
description: "Design banners for social media, ads, website heroes, and print. Multiple art direction options with HTML/CSS. Platforms: Facebook, Twitter/X, LinkedIn, YouTube, Instagram, Google Display, website hero."
metadata:
  author: claudekit
  version: "1.0.0"
---

# Banner Design

Multi-format creative banner system for social, ads, web, and print.

## When to Use

- Social media cover/header creation
- Ad banner or display ad design
- Website hero section visual design
- Event/print banner design

## Workflow

### Step 1: Gather Requirements

1. **Purpose** — social cover, ad banner, website hero, print?
2. **Platform/size** — which platform or custom dimensions?
3. **Content** — headline, subtext, CTA, logo placement?
4. **Brand** — existing brand guidelines? (check the user's project `docs/brand-guidelines.md`, managed by the `brand` skill; if missing, start from `brand/templates/brand-guidelines-starter.md`)
5. **Style preference** — any art direction?

### Step 2: Design HTML/CSS Banner

Create responsive HTML/CSS banner with:
- Exact platform dimensions
- Safe zones (critical content in central 70-80%)
- Max 2 typefaces, single CTA, 4.5:1 contrast ratio
- Brand colors from design tokens

### Step 3: Export to Images

Screenshot HTML banners at exact platform dimensions using browser tools.

## Banner Size Reference

| Platform | Type | Size (px) |
|----------|------|-----------|
| Facebook | Cover | 820 x 312 |
| Twitter/X | Header | 1500 x 500 |
| LinkedIn | Personal | 1584 x 396 |
| YouTube | Channel art | 2560 x 1440 |
| Instagram | Story | 1080 x 1920 |
| Instagram | Post | 1080 x 1080 |
| Google Ads | Med Rectangle | 300 x 250 |
| Website | Hero | 1920 x 600-1080 |

## Art Direction Styles

| Style | Best For |
|-------|----------|
| Minimalist | SaaS, tech |
| Bold Typography | Announcements |
| Gradient | Modern brands |
| Photo-Based | Lifestyle, e-com |
| Geometric | Tech, fintech |
| Glassmorphism | SaaS, apps |
| Neon/Cyberpunk | Gaming, events |

Full reference: `references/banner-sizes-and-styles.md`

## Design Rules

- **Safe zones**: critical content in central 70-80%
- **CTA**: one per banner, bottom-right, min 44px height
- **Typography**: max 2 fonts, min 16px body, ≥32px headline
- **Text ratio**: under 20% for ads (Meta penalizes)
- **Print**: 300 DPI, CMYK, 3-5mm bleed
