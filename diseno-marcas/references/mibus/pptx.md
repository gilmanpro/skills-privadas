# Guía: Aplicar Diseño MiBus a PowerPoint (.pptx)

> Cómo crear presentaciones corporativas con la identidad visual de MiBus.

## 📋 Antes de empezar

1. Lee `assets/brand-mibus.json` y `assets/colors-mibus.md` de esta skill.
2. Descarga los assets necesarios a `WORKDIR/ASSETS/`:
   - Logo: `logo-1.png` y `retina-logo.png`
   - Background: `bg-stats.jpg` (1920x566)
3. **Carga la skill `pptx`** del sistema opencode y sigue su flujo de trabajo (carpeta temporal, etc.).
4. Combina: identidad MiBus (esta skill) + buenas prácticas PPTX (skill `pptx`).

## 🎨 Paleta específica para PPTX

```python
MIBUS_COLORS = {
    "primary":      "283C90",   # Títulos, branding
    "primary_dark": "1B2A66",   # Backgrounds oscuros
    "secondary":    "205CA7",   # Botones, CTAs
    "secondary_h":  "409EFF",   # Hover de botones
    "accent":       "1DA1F2",   # Acentos, links
    "dark":         "1A1A2E",   # Header/Footer
    "white":        "FFFFFF",
    "text":         "333333",
    "text_light":   "FFFFFF",
    "border":       "E0E0E0",
}
```

## 🔤 Tipografía para PPTX

| Elemento | Fuente | Weight | Tamaño |
|---|---|---|---|
| Título slide (H1) | Poppins | 700 | 36-44 pt |
| Subtítulo (H2) | Poppins | 600 | 24-28 pt |
| Sección (H3) | Poppins | 600 | 18-22 pt |
| Body | Roboto | 400 | 14-18 pt |
| Bullet | Roboto | 400 | 14-16 pt |
| Caption/Nota | Roboto | 300 | 10-12 pt |
| Número destacado | Poppins | 700 | 48-72 pt |

**⚠️ Importante:** PowerPoint NO carga web fonts automáticamente. Tienes 2 opciones:

1. **Instalar las fuentes en el sistema** (recomendado para el usuario final):
   - Descargar Poppins y Roboto de Google Fonts
   - Instalarlas en Windows: clic derecho → Instalar para todos los usuarios
   - PowerPoint las detectará automáticamente

2. **Usar fallback** si las fuentes no están instaladas:
   - Poppins → `Calibri Light` o `Arial` (más cercano)
   - Roboto → `Calibri` o `Arial`
   - NO abuses del fallback, pierdes la identidad

## 📐 Layout de slides

### Slide 1: Portada
```
┌──────────────────────────────────────────┐
│                                          │
│  [BACKGROUND: bg-stats.jpg con          │
│   overlay oscuro 60% rgba(0,0,0,0.6)]   │
│                                          │
│         [LOGO MiBus - 4cm ancho]         │
│                                          │
│   TÍTULO DE LA PRESENTACIÓN              │
│   (Poppins 700, 40pt, blanco)            │
│                                          │
│   Subtítulo descriptivo                  │
│   (Roboto 400, 20pt, blanco 80%)        │
│                                          │
│   ─────                                  │
│   Fecha · Gilberto Castillo              │
│   (Roboto 300, 14pt, blanco 60%)        │
│                                          │
└──────────────────────────────────────────┘
```

### Slide 2: Índice / Tabla de Contenido
```
┌──────────────────────────────────────────┐
│ [Logo MiBus pequeño]    CONTENIDO        │ ← Header con primary #283c90
├──────────────────────────────────────────┤
│                                          │
│  1.  Introducción                        │
│  2.  Objetivos                          │
│  3.  Desarrollo                         │
│  4.  Resultados                         │
│  5.  Conclusiones                       │
│                                          │
│  (Números en Poppins 700 primary,        │
│   texto en Roboto 400)                   │
│                                          │
└──────────────────────────────────────────┘
```

### Slide 3 en adelante: Contenido
```
┌──────────────────────────────────────────┐
│ [Header: primary #283c90 + logo]        │ ← Banda superior 0.8cm
│                                          │
│  TÍTULO DE LA SECCIÓN (Poppins 700)      │
│  ───── (línea primary 2px)               │
│                                          │
│  Contenido de la slide...                │
│  - Bullet 1                              │
│  - Bullet 2                              │
│                                          │
├──────────────────────────────────────────┤
│ #2 / 10        [Logo mini]   MiBus 2026 │ ← Footer con #1A1A2E
└──────────────────────────────────────────┘
```

### Slide de estadísticas (destacada)
```
┌──────────────────────────────────────────┐
│ [BACKGROUND: bg-stats.jpg]               │
│                                          │
│  DATOS CLAVE                             │
│                                          │
│   1436        +4,000      152    450K    │ ← Poppins 700, 64pt
│   Unidades    Trab.      Rutas  Pasaj.  │ ← Roboto 400, 16pt
│                                          │
│  (Todo en blanco sobre el background)    │
└──────────────────────────────────────────┘
```

## 🛠️ Implementación con python-pptx

### Setup básico

```python
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn
from copy import deepcopy

# Crear presentación 16:9
prs = Presentation()
prs.slide_width = Inches(13.333)   # 16:9
prs.slide_height = Inches(7.5)

# Colores MiBus
PRIMARY = RGBColor(0x28, 0x3C, 0x90)
PRIMARY_DARK = RGBColor(0x1B, 0x2A, 0x66)
SECONDARY = RGBColor(0x20, 0x5C, 0xA7)
SECONDARY_HOVER = RGBColor(0x40, 0x9E, 0xFF)
ACCENT = RGBColor(0x1D, 0xA1, 0xF2)
DARK = RGBColor(0x1A, 0x1A, 0x2E)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
TEXT = RGBColor(0x33, 0x33, 0x33)
BORDER = RGBColor(0xE0, 0xE0, 0xE0)
```

### Función helper para textos

```python
def set_text(run, text, font_name="Roboto", size=18, bold=False, color=TEXT):
    """Aplica formato MiBus a un run de texto."""
    run.text = text
    run.font.name = font_name
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    # Set East Asian font también
    rPr = run._r.get_or_add_rPr()
    eastAsian = rPr.find(qn('a:ea'))
    if eastAsian is None:
        from lxml import etree
        eastAsian = etree.SubElement(rPr, qn('a:ea'))
    eastAsian.set('typeface', font_name)
```

### Función helper para shapes

```python
def add_header_band(slide, prs, page_num, total):
    """Añade banda de header con color MiBus primary."""
    # Banda superior
    band = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        0, 0, prs.slide_width, Inches(0.8)
    )
    band.fill.solid()
    band.fill.fore_color.rgb = PRIMARY
    band.line.fill.background()
    
    # Logo (esquina izquierda)
    slide.shapes.add_picture(
        "ASSETS/logo.png", 
        Inches(0.3), Inches(0.1), 
        height=Inches(0.6)
    )
    
    # Título de slide (a la derecha del logo)
    title_box = slide.shapes.add_textbox(
        Inches(3.5), Inches(0.15), Inches(9.5), Inches(0.5)
    )
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    run = p.add_run()
    set_text(run, "MiBus · Título de la Sección", "Poppins", 18, True, WHITE)
    
    # Footer (número de página)
    footer = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        0, prs.slide_height - Inches(0.4), prs.slide_width, Inches(0.4)
    )
    footer.fill.solid()
    footer.fill.fore_color.rgb = DARK
    footer.line.fill.background()
    
    # Texto footer
    footer_box = slide.shapes.add_textbox(
        Inches(0.3), prs.slide_height - Inches(0.35),
        Inches(12.5), Inches(0.3)
    )
    tf = footer_box.text_frame
    p = tf.paragraphs[0]
    run = p.add_run()
    set_text(run, f"{page_num} / {total}", "Roboto", 10, False, WHITE)
    
    # Logo mini en footer
    slide.shapes.add_picture(
        "ASSETS/favicon.png",
        prs.slide_width - Inches(0.5), prs.slide_height - Inches(0.35),
        height=Inches(0.3)
    )
```

### Botón MiBus

```python
def add_mibus_button(slide, left, top, width, height, text):
    """Crea un botón con estilo MiBus."""
    btn = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        left, top, width, height
    )
    btn.fill.solid()
    btn.fill.fore_color.rgb = SECONDARY
    btn.line.color.rgb = SECONDARY
    btn.line.width = Pt(1)
    
    # Texto del botón
    tf = btn.text_frame
    tf.margin_left = Pt(10)
    tf.margin_right = Pt(10)
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    set_text(run, text, "Roboto", 14, True, WHITE)
    
    return btn
```

## ✅ Checklist para PPTX MiBus

- [ ] Logo MiBus en TODAS las slides (header o footer)
- [ ] Header con color `#283c90` o `#1A1A2E`
- [ ] Footer con número de página y logo mini
- [ ] Slide de portada con background `bg-stats.jpg` o color primary oscuro
- [ ] Títulos en Poppins (o Calibri/Arial si no está instalada)
- [ ] Body en Roboto (o Calibri/Arial)
- [ ] Paleta respetada: solo azules MiBus + blanco + gris
- [ ] Sin emojis, sin imágenes coloridas fuera de marca
- [ ] Datos numéricos destacados en grande y Poppins 700
- [ ] Botones (si los hay) en `#205CA7`

## 🚫 Errores comunes

- ❌ Fondo blanco puro sin header/footer
- ❌ Logo pixelado (usar siempre el de retina para PPTX)
- ❌ Texto blanco sobre fondo claro
- ❌ Mezcla de Calibri, Arial, Times New Roman
- ❌ Colores no corporativos (rojo, verde, amarillo)
- ❌ Emojis como íconos
- ❌ Imágenes con marca de agua
