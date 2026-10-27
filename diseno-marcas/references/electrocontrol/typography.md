# Tipografía — Sistema Tipográfico Electrocontrol

El sitio web oficial no declara una familia de fuente personalizada en su CSS — usa el stack por defecto de Tailwind (Inter / Geist / system-ui). Esto es intencional: la identidad visual se construye con **colores, degradados y peso**, no con una tipografía exótica. Mantén esa filosofía en todos los formatos.

---

## Familia tipográfica

### Stack oficial (web y digital)

```css
font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI",
             Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif,
             "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol",
             "Noto Color Emoji";
```

**Tailwind equivalente:** dejar la fuente por defecto de Tailwind (no declarar `font-family` custom). En la práctica, esto se renderiza como:
- **macOS / iOS:** SF Pro / SF Pro Display
- **Windows:** Segoe UI
- **Android:** Roboto
- **Linux:** Cantarell / Noto Sans

### Familias recomendadas (instalables)

Si necesitas una familia específica más personalidad para presentaciones, documentos o branding, usa una de estas (todas gratuitas y similares en estilo):

| Familia | Cuándo usarla | Dónde conseguirla |
|---|---|---|
| **Inter** | Ideal para digital y presentaciones; la más usada en startups tech | [rsms.me/inter](https://rsms.me/inter/) — Google Fonts |
| **Geist Sans** | Recomendada por Vercel/Next.js, muy moderna | [vercel.com/geist](https://vercel.com/geist) |
| **Plus Jakarta Sans** | Ligeramente más cálida, ideal para slides | Google Fonts |
| **Manrope** | Geométrica moderna, excelente legibilidad | Google Fonts |
| **Sora** | Más futurista, ideal para hero/headlines | Google Fonts |

**Por defecto, usa Inter en TODO** — es la más cercana al stack del sitio y la más universal.

### Tipografías del logo (especial)

El texto "ELECTROCONTROL" del logo usa una tipografía **display sans-serif condensada, bold, mayúsculas, con tracking amplio**. Es una tipografía custom del logo. **No intentes replicarla en body text.**

Si necesitas una similar para headers de marca, prueba:
- **Bebas Neue** (gratis, Google Fonts)
- **Anton** (gratis, Google Fonts)
- **Oswald** (gratis, Google Fonts)

Pero la regla es: el logo se usa **como está** (imagen), no se replica tipográficamente.

---

## Escala tipográfica (basada en Tailwind)

El sitio usa las clases estándar de Tailwind. Aquí traducidas a valores absolutos:

| Elemento | Tailwind class | Tamaño | Peso | Line-height | Uso |
|---|---|---|---|---|---|
| **H1 hero** | `text-5xl md:text-7xl` | 48-72px | `font-bold` (700) | 1.1 (tight) | Título principal de slide/página, máximo 1-2 por pieza |
| **H2 sección** | `text-4xl md:text-5xl` | 36-48px | `font-bold` (700) | 1.2 | Títulos de sección ("Sobre Mí", "Servicios") |
| **H3 card** | `text-2xl md:text-3xl` | 24-30px | `font-bold` (700) | 1.25 | Títulos de cards de servicios, h3 |
| **H4 item** | `text-xl` | 20px | `font-semibold` (600) | 1.3 | Títulos de items, subtítulos importantes |
| **H5 label** | `text-lg` | 18px | `font-semibold` (600) | 1.4 | Labels destacados |
| **Body grande** | `text-lg` | 18px | `font-normal` (400) | `leading-relaxed` (1.625) | Párrafos destacados, lead text |
| **Body** | `text-base` | 16px | `font-normal` (400) | 1.5 | Párrafos normales |
| **Small** | `text-sm` | 14px | `font-normal` (400) | 1.5 | Texto secundario, captions |
| **Caption** | `text-xs` | 12px | `font-normal` (400) | 1.4 | Copyright, metadatos, badges |

---

## Pesos disponibles

| Peso | Tailwind class | Uso |
|---|---|---|
| **400** Regular | `font-normal` | Body, párrafos, captions |
| **500** Medium | `font-medium` | Labels destacados, subtítulos (poco usado) |
| **600** Semibold | `font-semibold` | H4, H5, labels de stat cards |
| **700** Bold | `font-bold` | H1, H2, H3, CTAs, números destacados |

**Regla:** la marca usa principalmente **2 pesos**: 400 (body) y 700 (headings). El 500/600 aparece solo en H4/H5. No abuses de los pesos intermedios.

---

## Colores de texto sobre dark

| Token | HEX | Uso | Tamaño mínimo |
|---|---|---|---|
| `--text-white` | `#FFFFFF` | Títulos principales, números destacados | 16px+ |
| `--text-body` | `#CBD5E1` slate-300 | Párrafos, descripciones | 14px+ |
| `--text-secondary` | `#94A3B8` slate-400 | Labels, captions, texto secundario | 12px+ |
| `--text-muted` | `#64748B` slate-500 | Copyright, metadatos deshabilitados | 12px (no crítico) |
| `--text-cyan-400` | `#22D3EE` | Texto destacado, headers con degradado | 16px+ |
| `--text-purple-400` | `#C084FC` | Texto destacado alternativo | 16px+ |
| `--text-pink-400` | `#F472B6` | Texto destacado para énfasis | 16px+ |

**Regla:** sobre fondo dark (`#0F172A`), nunca uses un color de texto con contraste menor a 4.5:1. Slate-500 está en el límite — solo para metadatos no críticos.

Ver tabla de contrastes WCAG en `colors.md` → sección "Combinaciones aprobadas".

---

## Text con degradado (signature)

**Esta es LA firma tipográfica de la marca.** Se usa en H1 del hero y en H2 de secciones principales:

```css
.gradient-text {
  background: linear-gradient(to right, #22D3EE 0%, #C084FC 50%, #F472B6 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  color: transparent;
}
```

**Tailwind:** `bg-gradient-to-r from-cyan-400 via-purple-400 to-pink-400 bg-clip-text text-transparent`

**Reglas:**
- Solo se aplica a **H1** (hero principal) y a **H2 de secciones principales**.
- Máximo **2 veces por página** (idealmente 1).
- **No aplicar** a párrafos, labels, captions.
- **No aplicar** más de 3 colores en el degradado (cyan→purple→pink es la única combinación permitida).

**Equivalentes en otros formatos (sin soporte de `background-clip: text`):**
- **PowerPoint:** usar degradado de relleno (gradient fill) en el texto
- **Word / PDF:** convertir texto a imagen o usar color sólido (cyan-400 como aproximación)
- **SVG:** usar `<linearGradient>` con `<text>` y `fill="url(#grad)"`
- **Excel:** no soportado nativamente, usar color sólido cyan-500

---

## Espaciado entre letras (letter-spacing)

| Uso | Valor |
|---|---|
| Headings, body | `0` (normal) |
| Texto del logo "ELECTROCONTROL" | `+0.05em` a `+0.1em` (tracking ancho, solo el logo) |
| UPPERCASE labels | `+0.05em` (para mejorar legibilidad) |
| Caption / small | `0` |

**El sitio NO usa letter-spacing custom en headings ni body.** Mantén el default. Solo aplica tracking ancho si el texto está en mayúsculas (ej. eyebrow text, "NUESTROS SERVICIOS").

---

## antialiasing

SIEMPRE activa `antialiasing` (en Tailwind: `antialiased` class en `<body>`). En CSS:

```css
body {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
```

Esto es CRÍTICO para que el texto se vea nítido en dark mode.

---

## Aplicación por formato (resumen rápido)

| Formato | Familia | Cómo aplicar |
|---|---|---|
| **Web** | Inter (Google Fonts) o sistema | `font-family: 'Inter', system-ui, sans-serif;` |
| **PowerPoint** | Calibri (default Office) o Inter instalada | Usar tema personalizado; ver `formatos/pptx.md` |
| **Word** | Calibri (default) | Cambiar a Inter/Calibri Light para títulos, mantener Calibri para body |
| **Excel** | Calibri | Limitado, aplicar a headers y celdas destacadas |
| **PDF** | Cualquiera embebida | Usar la del documento original si se convierte |
| **SVG** | Inter vía `@import` o sistema | Usar en `<text>` con `font-family="Inter, sans-serif"` |

Para detalles específicos de cada formato, consulta la referencia correspondiente:
- `formatos/web.md` — web
- `formatos/pptx.md` — PowerPoint
- `formatos/docx.md` — Word
- `formatos/xlsx.md` — Excel
- `formatos/pdf.md` — PDF
- `formatos/svg.md` — SVG
