# Plantilla PowerPoint — ITSE

Guía para crear presentaciones institucionales del ITSE con la skill `pptx` + esta skill.

---

## ⚠️ Regla de carpeta de trabajo (OBLIGATORIA)

Antes de empezar, **crea SIEMPRE una carpeta temporal dedicada** para no contaminar la raíz del proyecto:

```bash
mkdir "%TEMP%\opencode\pptx-YYYYMMDD-HHMMSS"
```

Todos los archivos intermedios (imágenes, scripts, pptx sin terminar) van ahí. El `.pptx` final se copia a la carpeta de destino.

---

## 🚨 REGLA CRÍTICA: Logo del ITSE ARRIBA en portadas

> **En TODA portada de PowerPoint, el logo del ITSE va en la parte SUPERIOR
> del slide (header) — NUNCA en el centro vertical, NUNCA debajo del título.**
> El logo es la firma institucional; siempre preside el diseño.

- **Portada:** Logo horizontal centrado o alineado a la izquierda en el TOP del slide (parte superior, dentro del header), alto ~1.5–2 cm
- **Slides de contenido:** Logo horizontal en la esquina SUPERIOR IZQUIERDA, alto ~1–1.2 cm
- **Slide de cierre ("Gracias"):** Logo horizontal centrado en el TOP, alto ~1.5 cm

---

## Especificaciones de la presentación

| Parámetro | Valor |
|---|---|
| Tamaño de slide | 16:9 widescreen (33.867 × 19.05 cm) |
| Resolución | HD (1920×1080) |
| Tipografía | **Arial** (presente en Office) o Calibri |
| Color de fondo | Blanco (`#FFFFFF`) o gris claro (`#F7F7F7`) |
| Carrera de referencia | **T.S. en Big Data y Ciencia de Datos** (Área de Innovación Digital) |

---

## Paleta aplicada a PowerPoint

### Colores personalizados a crear

En PowerPoint: **Diseño → Variantes → Colores → Personalizar colores**, agregar:

| Nombre en PowerPoint | HEX |
|---|---|
| Dorado ITSE | `#FFB000` |
| Gris Carbón | `#424242` |
| Blanco | `#FFFFFF` |
| Gris 100 | `#7B7B7B` |
| Gris 400 | `#F7F7F7` |
| Azul | `#225082` |
| Verde | `#9EBE43` |
| Rojo | `#CD2E26` |

### Tipos de slides (layouts personalizados)

Diseña 6 layouts base reutilizables:

#### Layout 1: Portada (logo ARRIBA)
```
┌────────────────────────────────────┐
│  [LOGO ITSE]                       │  ← LOGO ARRIBA (header, 1.5-2cm alto)
│  ─────────────                     │  ← línea dorada 2pt como separador
│                                    │
│                                    │
│   TÍTULO DE LA PRESENTACIÓN        │  ← 44pt bold #424242 (centrado)
│   Subtítulo descriptivo            │  ← 24pt regular #7B7B7B
│                                    │
│                                    │
│   Mgtr. Nombre Apellido            │  ← 18pt #424242
│   T.S. Big Data y CD · ITSE        │  ← 14pt #7B7B7B
│   {Mes} · {año}                     │  ← mes y año actual
└────────────────────────────────────┘
```

**Reglas de la portada:**
- El logo SIEMPRE va en el TOP (header), NO en el centro vertical
- Debajo del logo, una línea dorada de 2pt como separador
- El título va centrado en el medio-inferior del slide
- El autor y la fecha van al pie, con la carrera de referencia (T.S. en Big Data y Ciencia de Datos) si aplica

Fondo: blanco con un **banda dorada vertical** en el lado izquierdo (5cm de ancho) o **banda dorada inferior** (3cm de alto) — la banda dorada NO reemplaza al logo, solo lo complementa.

#### Layout 2: Contenido — Título + texto
```
┌────────────────────────────────────┐
│ [LOGO]                  ITSE {año}  │  ← header (año actual)
├────────────────────────────────────┤
│                                    │
│  TÍTULO DE LA SECCIÓN              │  ← 32pt bold #424242
│  ──────── (línea dorada)           │  ← 3px #FFB000
│                                    │
│  • Punto 1                         │  ← 18pt #424242
│  • Punto 2                         │
│  • Punto 3                         │
│                                    │
└────────────────────────────────────┘
```

#### Layout 3: Contenido — Título + imagen
```
┌────────────────────────────────────┐
│ [LOGO]                             │
├────────────────────────────────────┤
│  TÍTULO                            │
│  ─────                             │
│                                    │
│  Texto a la        ┌──────────┐   │
│  izquierda,        │          │   │
│  imagen a la       │  IMAGEN  │   │
│  derecha.          │          │   │
│                    └──────────┘   │
└────────────────────────────────────┘
```

#### Layout 4: Título + 2 columnas
```
┌────────────────────────────────────┐
│  TÍTULO                            │
│  ─────                             │
│                                    │
│  ┌─────────┐    ┌─────────┐        │
│  │  LADO   │    │  LADO   │        │
│  │  A      │    │  B      │        │
│  │         │    │         │        │
│  └─────────┘    └─────────┘        │
└────────────────────────────────────┘
```

Cada "lado" puede ser una **card** con borde dorado superior (4px) o fondo `#F7F7F7` y esquinas redondeadas.

#### Layout 5: Cifras destacadas
```
┌────────────────────────────────────┐
│  TÍTULO                            │
│  ─────                             │
│                                    │
│      +4.000        15        +80%  │  ← 72pt bold #FFB000
│   Estudiantes   Carreras   Inserción│  ← 14pt #7B7B7B
│                                    │
└────────────────────────────────────┘
```

**Reglas para números grandes:**
- Tamaño: 60-72pt
- Color: dorado `#FFB000`
- Peso: 700
- Label debajo: 12-14pt, gris claro `#7B7B7B`

#### Layout 6: Slide de cierre / Contacto
```
┌────────────────────────────────────┐
│                                    │
│                                    │
│         ¡GRACIAS!                  │  ← 60pt bold #424242
│                                    │
│         [LOGO ITSE]                │
│                                    │
│   itse.ac.pa                       │  ← 18pt #FFB000
│   contacto@itse.ac.pa              │  ← 14pt #7B7B7B
│                                    │
└────────────────────────────────────┘
```

Fondo: blanco con un **gran círculo dorado degradado** como acento decorativo en la esquina.

---

## Tipografía aplicada

| Elemento | Tamaño | Peso | Color |
|---|---|---|---|
| Título de slide | 36-44pt | 700 | `#424242` |
| Subtítulo | 24-28pt | 500 | `#424242` |
| Contenido / bullets | 18-24pt | 400 | `#424242` |
| Footer | 10-12pt | 400 | `#7B7B7B` |
| Números grandes | 60-72pt | 700 | `#FFB000` |
| Labels de números | 12-14pt | 400 | `#7B7B7B` |

**Tipografía:** Arial (default en Office). Alternativa: Calibri.

---

## Logo en slides

> **Regla inquebrantable:** el logo del ITSE **SIEMPRE va ARRIBA** en las
> portadas. Ver la sección "🚨 REGLA CRÍTICA" más arriba.

- **Slide de portada:** Logo en el TOP (parte superior del slide, alineado a la izquierda o centrado en el header), alto **~1.5–2 cm** — NUNCA en el centro vertical
- **Slides de contenido:** Logo en esquina superior IZQUIERDA, alto 1–1.2 cm
- **Slide de cierre ("Gracias"):** Logo en el TOP centrado, alto ~1.5 cm

**Archivo a usar:** `assets/logo-itse-horizontal.png`

---

## Botones y elementos interactivos

Si la presentación tiene botones/enlaces:

```css
/* Equivalente en PowerPoint: insertar forma con relleno */
Fondo: linear-gradient(135deg, #FFCE00 0%, #FFB000 100%)
Texto: blanco, 18pt, bold
Esquinas: redondeadas
Padding: 12px 32px
```

Para simular el gradiente en PowerPoint:
1. Insertar rectángulo con esquinas redondeadas
2. Relleno → Degradado preestablecido → "Lineal - Diagonal"
3. Detener degradado en 0%: `#FFCE00`, en 100%: `#FFB000`

---

## Colores de slides (fondos alternativos)

| Tipo | Color | Uso |
|---|---|---|
| Slide normal | `#FFFFFF` | Mayoría de slides |
| Slide alterno | `#F7F7F7` | Cada 3-4 slides, para dar respiro |
| Slide de impacto | `#424242` | Slide inicial, slides de cierre, slides de cifras grandes (texto blanco) |
| Slide de números | Degradado `#FFCE00 → #FFB000` | Solo para slides de título hero (texto blanco) |

**Regla:** No más de 2 slides oscuras consecutivas. Máximo 3 slides oscuras en toda la presentación.

---

## Estructura recomendada (15 slides)

1. Portada
2. Introducción / Contexto
3. Tabla de contenido
4. Sección 1 — título
5. Sección 1 — contenido 1
6. Sección 1 — contenido 2
7. Sección 2 — título
8. Sección 2 — contenido
9. Sección 2 — ejemplo / caso
10. Cifras destacadas
11. Sección 3 — título
12. Sección 3 — contenido
13. Conclusiones
14. Próximos pasos
15. Cierre / Gracias

---

## Generación con python-pptx (script base)

```python
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# Colores ITSE
DORADO = RGBColor(0xFF, 0xB0, 0x00)
GRIS = RGBColor(0x42, 0x42, 0x42)
BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
GRIS_CLARO = RGBColor(0xF7, 0xF7, 0xF7)

# Crear presentación 16:9
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# Layout en blanco (índice 6)
blank_layout = prs.slide_layouts[6]

# === SLIDE 1: PORTADA (logo ARRIBA) ===
slide = prs.slides.add_slide(blank_layout)
slide.background.fill.solid()
slide.background.fill.fore_color.rgb = BLANCO

# Banda dorada vertical a la izquierda (acento, NO reemplaza al logo)
banda = slide.shapes.add_shape(
    MSO_SHAPE.RECTANGLE, 0, 0, Inches(0.4), Inches(7.5)
)
banda.fill.solid()
banda.fill.fore_color.rgb = DORADO
banda.line.fill.background()

# LOGO DEL ITSE EN LA PARTE SUPERIOR (header) — REGLA OBLIGATORIA
# Centrado horizontal en el TOP del slide, alto ~1.8 cm
slide.shapes.add_picture(
    "logo-itse-horizontal.png",
    Inches(5.4), Inches(0.5), height=Inches(1.8)  # ARRIBA (y=0.5")
)

# Línea dorada decorativa debajo del logo
linea = slide.shapes.add_shape(
    MSO_SHAPE.RECTANGLE, Inches(2), Inches(2.5), Inches(9.3), Inches(0.05)
)
linea.fill.solid()
linea.fill.fore_color.rgb = DORADO
linea.line.fill.background()

# Título (centrado, en el medio-inferior del slide)
title = slide.shapes.add_textbox(
    Inches(1.5), Inches(3.0), Inches(10.5), Inches(1.5)
)
tf = title.text_frame
p = tf.paragraphs[0]
p.text = "TÍTULO DE LA PRESENTACIÓN"
p.font.size = Pt(40)
p.font.bold = True
p.font.color.rgb = GRIS
p.font.name = "Arial"

# Subtítulo
sub = slide.shapes.add_textbox(
    Inches(1.5), Inches(4.3), Inches(10.5), Inches(0.8)
)
p = sub.text_frame.paragraphs[0]
p.text = "Subtítulo descriptivo de la presentación"
p.font.size = Pt(20)
p.font.color.rgb = RGBColor(0x7B, 0x7B, 0x7B)
p.font.name = "Arial"

# Autor + carrera de referencia + fecha (al pie)
autor = slide.shapes.add_textbox(
    Inches(1.5), Inches(5.8), Inches(10.5), Inches(1)
)
p = autor.text_frame.paragraphs[0]
from datetime import datetime
fecha_actual = datetime.now().strftime("%B · %Y")
p.text = f"Mgtr. Nombre Apellido · T.S. en Big Data y Ciencia de Datos · ITSE · {fecha_actual}"
p.font.size = Pt(14)
p.font.color.rgb = GRIS
p.font.name = "Arial"

prs.save("presentacion-itse.pptx")
```

---

## Cheatsheet rápida

```
ITSE POWERPOINT
===============
Tipografía: Arial / Calibri
Slide size: 16:9 widescreen
Carrera de referencia: T.S. en Big Data y Ciencia de Datos

PALETA:
  #FFB000 Dorado (acentos, números, líneas)
  #424242 Gris Carbón (texto, fondos oscuros)
  #FFFFFF Blanco (fondo)
  #F7F7F7 Gris claro (slides alternas)

TIPOGRAFÍA:
  Título:    36-44pt bold #424242
  Subtítulo: 24-28pt semi  #424242
  Body:      18-24pt       #424242
  Números:   60-72pt bold #FFB000
  Labels:    12-14pt       #7B7B7B

LAYOUTS: portada, contenido, dos-columnas, cifras, cierre
LOGO: ARRIBA en portadas (header, 1.5-2cm alto)
      Esquina sup. izq. (1-1.2cm alto) en slides de contenido
      ARRIBA centrado en slide de cierre
```

---

## Recursos adicionales

- `references/itse/colors.md` — paleta completa
- `references/itse/typography.md` — sistema tipográfico
- `references/itse/logo.md` — uso del logo
- `references/itse/branding.md` — datos institucionales
- `assets/logo-itse-horizontal.png` — logo principal
