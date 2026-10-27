---
name: ui-styling
description: "Create accessible UI with shadcn/ui components, Tailwind CSS, and responsive layouts. Use for building interfaces, implementing design systems, adding accessible components, customizing themes, and dark mode."
metadata:
  author: claudekit
  version: "1.0.0"
license: MIT
---

# UI Styling Skill

Comprehensive skill for creating beautiful, accessible user interfaces with shadcn/ui + Tailwind CSS.

## When to Use

- Building UI with React-based frameworks (Next.js, Vite, Remix, Astro)
- Implementing accessible components (dialogs, forms, tables, navigation)
- Styling with utility-first CSS approach
- Creating responsive, mobile-first layouts
- Implementing dark mode and theme customization
- Building design systems with consistent tokens

## Core Stack

### Component Layer: shadcn/ui
- Pre-built accessible components via Radix UI primitives
- Copy-paste distribution model
- TypeScript-first with full type safety

### Styling Layer: Tailwind CSS
- Utility-first CSS framework
- Build-time processing with zero runtime overhead
- Mobile-first responsive design

## Quick Start

### Component + Styling Setup

**Install shadcn/ui with Tailwind:**
```bash
npx shadcn@latest init
```

**Add components:**
```bash
npx shadcn@latest add button card dialog form
```

**Use components with utility styling:**
```tsx
import { Button } from "@/components/ui/button"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"

export function Dashboard() {
  return (
    <div className="container mx-auto p-6 grid gap-6 md:grid-cols-2 lg:grid-cols-3">
      <Card className="hover:shadow-lg transition-shadow">
        <CardHeader>
          <CardTitle className="text-2xl font-bold">Analytics</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <p className="text-muted-foreground">View your metrics</p>
          <Button variant="default" className="w-full">View Details</Button>
        </CardContent>
      </Card>
    </div>
  )
}
```

## References

| Topic | File |
|-------|------|
| Component Library | `references/shadcn-components.md` |
| Theming | `references/shadcn-theming.md` |
| Accessibility | `references/shadcn-accessibility.md` |
| Tailwind Utilities | `references/tailwind-utilities.md` |
| Responsive Design | `references/tailwind-responsive.md` |
| Customization | `references/tailwind-customization.md` |
| Visual Design | `references/canvas-design-system.md` |

## Utility Scripts

```bash
# Add shadcn/ui components
python scripts/shadcn_add.py button card dialog

# Generate tailwind.config.js
python scripts/tailwind_config_gen.py --colors brand:blue --fonts display:Inter
```

## Best Practices

1. **Component Composition**: Build complex UIs from simple, composable primitives
2. **Utility-First Styling**: Use Tailwind classes directly; extract components only for true repetition
3. **Mobile-First Responsive**: Start with mobile styles, layer responsive variants
4. **Accessibility-First**: Leverage Radix UI primitives, add focus states, use semantic HTML
5. **Design Tokens**: Use consistent spacing scale, color palettes, typography system
6. **Dark Mode Consistency**: Apply dark variants to all themed elements

## Resources

- shadcn/ui: https://ui.shadcn.com
- Tailwind CSS: https://tailwindcss.com
- Radix UI: https://radix-ui.com
