# Paleta de Colores — gilman.pro

Referencia completa de la paleta de colores del sistema de diseño gilman.pro. **No inventes colores fuera de esta paleta.**

## Acceso rápido

Importar `palette-gilman.json` (en `assets/`) en scripts Python o Node para uso programático:

```python
import json
palette = json.load(open("assets/palette-gilman.json"))
emerald_500 = palette["light_mode"]["primary"]["hex"]  # "#10B981"
```

## 1. MODO CLARO (default)

### Colores primarios

| Token | Nombre | HEX | RGB | Tailwind | Uso principal |
|---|---|---|---|---|---|
| `primary` | Emerald 500 | `#10B981` | (16, 185, 129) | `emerald-500` | CTA, acentos, separador decorativo, logo, gradiente |
| `primary-hover` | Emerald 600 | `#059669` | (5, 150, 105) | `emerald-600` | Hover de botones, fondo hero |
| `primary-dark` | Emerald 700 | `#047857` | (4, 120, 87) | `emerald-700` | Hover oscuro, énfasis |
| `secondary` | Blue 600 | `#2563EB` | (37, 99, 235) | `blue-600` | Botón ATS claro, alternancia |

### Acentos

| Token | Nombre | HEX | RGB | Tailwind | Uso principal |
|---|---|---|---|---|---|
| `accent` | Cyan 400 | `#22D3EE` | (34, 211, 238) | `cyan-400` | Acentos secundarios, hover dark |
| `accent-dark` | Cyan 500 | `#06B6D4` | (6, 182, 212) | `cyan-500` | Gradiente del logo (stop 2) |

### Neutrales (oscuros para navbar/footer)

| Token | Nombre | HEX | RGB | Tailwind | Uso principal |
|---|---|---|---|---|---|
| `navbar` | Slate 800 | `#1E293B` | (30, 41, 59) | `slate-800` | Navbar, footer, secciones oscuras |
| `navbar-alt` | Slate 700 | `#334155` | (51, 65, 85) | `slate-700` | Bordes, social icons |

### Backgrounds y superficies

| Token | Nombre | HEX | RGB | Tailwind | Uso principal |
|---|---|---|---|---|---|
| `bg` | White | `#FFFFFF` | (255, 255, 255) | `white` | Fondo principal |
| `bg-alt` | Slate 50 | `#F8FAFC` | (248, 250, 252) | `slate-50` | Fondo alterno de secciones, cards |
| `bg-card` | Gray 50 | `#F9FAFB` | (249, 250, 251) | `gray-50` | Fondo de cards de contenido |

### Textos

| Token | Nombre | HEX | RGB | Tailwind | Uso principal |
|---|---|---|---|---|---|
| `text` | Gray 900 | `#111827` | (17, 24, 39) | `gray-900` | Títulos, cuerpo principal |
| `text-muted` | Gray 700 | `#374151` | (55, 65, 81) | `gray-700` | Texto con énfasis medio, labels |
| `text-secondary` | Gray 500 | `#6B7280` | (107, 114, 128) | `gray-500` | Texto secundario, descripciones |
| `text-tertiary` | Gray 400 | `#9CA3AF` | (156, 163, 175) | `gray-400` | Texto auxiliar, placeholders, captions |
| `text-light` | Gray 300 | `#D1D5DB` | (209, 213, 219) | `gray-300` | Texto sobre fondos oscuros |
| `text-navbar` | Slate 300 | `#CBD5E1` | (203, 213, 225) | `slate-300` | Links de navbar |

### Bordes

| Token | Nombre | HEX | RGB | Tailwind | Uso principal |
|---|---|---|---|---|---|
| `border` | Gray 200 | `#E5E7EB` | (229, 231, 235) | `gray-200` | Bordes de inputs, separadores |
| `border-card` | Gray 100 | `#F3F4F6` | (243, 244, 246) | `gray-100` | Bordes de cards |

## 2. MODO OSCURO (alternativa)

### Colores primarios

| Token | Nombre | HEX | RGB | Tailwind | Uso principal |
|---|---|---|---|---|---|
| `primary` | Indigo 500 | `#6366F1` | (99, 102, 241) | `indigo-500` | CTA, separador decorativo, fondo hero |
| `primary-hover` | Indigo 600 | `#4F46E5` | (79, 70, 229) | `indigo-600` | Hover, botones primary |
| `primary-dark` | Indigo 700 | `#4338CA` | (67, 56, 202) | `indigo-700` | Hover oscuro |

### Acentos

| Token | Nombre | HEX | RGB | Tailwind | Uso principal |
|---|---|---|---|---|---|
| `accent` | Violet 500 | `#8B5CF6` | (139, 92, 246) | `violet-500` | Acento decorativo (punto final del separador) |
| `accent-hover` | Cyan 400 | `#22D3EE` | (34, 211, 238) | `cyan-400` | Hover de links, social icons |

### Backgrounds y superficies

| Token | Nombre | HEX | RGB | Tailwind | Uso principal |
|---|---|---|---|---|---|
| `bg` | Slate 900 | `#0F172A` | (15, 23, 42) | `slate-900` | Fondo principal |
| `bg-alt` | Slate 800 | `#1E293B` | (30, 41, 59) | `slate-800` | Fondo alterno, secciones |
| `bg-card` | Slate 800/80 | `rgba(30,41,59,0.8)` | (30, 41, 59, 0.8) | `slate-800/80` | Cards con glass effect |

### Textos

| Token | Nombre | HEX | RGB | Tailwind | Uso principal |
|---|---|---|---|---|---|
| `text` | White | `#FFFFFF` | (255, 255, 255) | `white` | Títulos, cuerpo |
| `text-secondary` | Slate 300 | `#CBD5E1` | (203, 213, 225) | `slate-300` | Texto secundario, labels |
| `text-muted` | Slate 400 | `#94A3B8` | (148, 163, 184) | `slate-400` | Texto auxiliar |
| `text-tertiary` | Slate 500 | `#64748B` | (100, 116, 139) | `slate-500` | Texto auxiliar (bajo contraste — solo para hints) |

### Bordes

| Token | Nombre | HEX | RGB | Tailwind | Uso principal |
|---|---|---|---|---|---|
| `border` | White/5 | `rgba(255,255,255,0.05)` | (255, 255, 255, 0.05) | `white/5` | Bordes sutiles |
| `border-card` | White/10 | `rgba(255,255,255,0.1)` | (255, 255, 255, 0.1) | `white/10` | Bordes de cards |

## 3. GRADIENTES DE MARCA

```css
/* Gradiente principal: emerald → cyan, diagonal */
--gradient-brand: linear-gradient(135deg, #10B981 0%, #06B6D4 100%);

/* Gradiente para dark mode: cyan → blanco */
--gradient-brand-dark: linear-gradient(135deg, #22D3EE 0%, #FFFFFF 100%);

/* Gradiente del logo Circuit G */
--gradient-logo: linear-gradient(0deg 0% 0%, 100% 100%);
/* aplicado con stops en SVG */
```

## 4. COMBINACIONES DE CONTRASTE VALIDADAS

| Foreground | Background | Contraste | Uso |
|---|---|---|---|
| `#10B981` (emerald-500) | `#FFFFFF` (white) | 3.16:1 | Solo texto grande o iconos — NO para texto pequeño |
| `#059669` (emerald-600) | `#FFFFFF` (white) | 4.55:1 | Texto pequeño OK, mejor opción para links |
| `#FFFFFF` (white) | `#10B981` (emerald-500) | 3.16:1 | OK para texto grande, no para párrafo |
| `#FFFFFF` (white) | `#1E293B` (slate-800) | 14.78:1 | Excelente — texto navbar |
| `#94A3B8` (slate-400) | `#0F172A` (slate-900) | 5.74:1 | OK para texto secundario dark |
| `#FFFFFF` (white) | `#6366F1` (indigo-500) | 3.66:1 | OK para texto grande, no para párrafo |
| `#22D3EE` (cyan-400) | `#0F172A` (slate-900) | 10.39:1 | Excelente — acentos dark |

## 5. GUÍA DE USO

- **Hero / Portada:** fondo `emerald-500` (claro) o `indigo-600` (dark) con texto blanco.
- **Botones primary:** fondo `emerald-600` (claro) o `indigo-600` (dark), texto blanco.
- **Botones outline:** borde `emerald-600` (claro) o `indigo-500` (dark), texto color marca.
- **Acentos secundarios:** `cyan-400` para highlights, nunca para texto principal.
- **Texto sobre fondo blanco:** siempre `gray-900` o más oscuro, NUNCA `gray-500` para párrafo.
- **Texto sobre fondo dark:** `white` o `slate-300`, evitar `slate-500` salvo para hints muy sutiles.
- **Separador decorativo:** emerald (claro) o indigo+violet (dark) — **es la firma visual gilman**.
