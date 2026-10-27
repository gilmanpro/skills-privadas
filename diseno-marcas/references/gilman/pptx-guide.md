# Aplicación a PowerPoint (.pptx) — gilman.pro

Cómo aplicar el branding gilman.pro a presentaciones PowerPoint usando `python-pptx`.

## 1. CONFIGURACIÓN INICIAL

### Imports y constantes de marca

```python
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from lxml import etree

# ===== PALETA GILMAN (modo claro por defecto) =====
PRIMARY        = RGBColor(0x10, 0xB9, 0x81)  # Emerald 500
PRIMARY_HOVER  = RGBColor(0x05, 0x96, 0x69)  # Emerald 600
PRIMARY_DARK   = RGBColor(0x04, 0x78, 0x57)  # Emerald 700
SECONDARY      = RGBColor(0x25, 0x63, 0xEB)  # Blue 600
ACCENT         = RGBColor(0x22, 0xD3, 0xEE)  # Cyan 400
ACCENT_DARK    = RGBColor(0x06, 0xB6, 0xD4)  # Cyan 500
NAVBAR         = RGBColor(0x1E, 0x29, 0x3B)  # Slate 800
NAVBAR_ALT     = RGBColor(0x33, 0x41, 0x55)  # Slate 700
WHITE          = RGBColor(0xFF, 0xFF, 0xFF)
BG_ALT         = RGBColor(0xF8, 0xFA, 0xFC)  # Slate 50
GRAY_900       = RGBColor(0x11, 0x18, 0x27)
GRAY_500       = RGBColor(0x6B, 0x72, 0x80)
GRAY_400       = RGBColor(0x9C, 0xA3, 0xAF)
GRAY_200       = RGBColor(0xE5, 0xE7, 0xEB)
GRAY_100       = RGBColor(0xF3, 0xF4, 0xF6)

# DARK MODE (alternativa)
INDIGO_500     = RGBColor(0x63, 0x66, 0xF1)
INDIGO_600     = RGBColor(0x4F, 0x46, 0xE5)
VIOLET_500     = RGBColor(0x8B, 0x5C, 0xF6)
SLATE_900      = RGBColor(0x0F, 0x17, 0x2A)
SLATE_800      = RGBColor(0x1E, 0x29, 0x3B)
SLATE_400      = RGBColor(0x94, 0xA3, 0xB8)

# ===== TIPOGRAFÍA =====
FONT_HEADING = "Montserrat"
FONT_BODY    = "Lato"
FONT_DISPLAY = "Orbitron"
FONT_TECH    = "Rajdhani"
```

### Crear presentación con tamaño estándar

```python
prs = Presentation()
prs.slide_width  = Inches(13.333)  # 16:9 widescreen
prs.slide_height = Inches(7.5)
```

## 2. LAYOUTS (ESTRUCTURAS REUTILIZABLES)

### Función: agregar fondo completo a un slide

```python
def set_slide_background(slide, color):
    """Color de fondo sólido para un slide completo."""
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = color
```

### Función: agregar separador decorativo (signature)

```python
def add_signature_separator(slide, top_y, use_dark_mode=False):
    """Línea + punto + línea + punto (violet) + línea. Bajo cada H2."""
    if use_dark_mode:
        color_a, color_b = INDIGO_500, VIOLET_500
    else:
        color_a, color_b = PRIMARY, PRIMARY  # en claro, ambos emerald

    # Línea 1 (w=10)
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(5.0), top_y, Inches(1.0), Pt(1.5))
    line.fill.solid(); line.fill.fore_color.rgb = color_a
    line.line.fill.background()
    # Punto 1
    dot1 = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(6.2), top_y - Pt(3), Pt(8), Pt(8))
    dot1.fill.solid(); dot1.fill.fore_color.rgb = color_a
    dot1.line.fill.background()
    # Línea 2 (w=16)
    line2 = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.4), top_y, Inches(1.6), Pt(1.5))
    line2.fill.solid(); line2.fill.fore_color.rgb = color_a
    line2.line.fill.background()
    # Punto 2 (violet en dark, emerald en light)
    dot2 = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(8.2), top_y - Pt(3), Pt(8), Pt(8))
    dot2.fill.solid(); dot2.fill.fore_color.rgb = color_b
    dot2.line.fill.background()
    # Línea 3 (w=10)
    line3 = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(8.4), top_y, Inches(1.0), Pt(1.5))
    line3.fill.solid(); line3.fill.fore_color.rgb = color_b
    line3.line.fill.background()
```

### Función: agregar logo + wordmark en esquina

```python
def add_logo(slide, x=Inches(0.4), y=Inches(0.3), w=Inches(1.2), h=Inches(0.4)):
    """Logo SVG insertado como imagen. Requiere tener assets/logo_gilmanpro.svg."""
    from pathlib import Path
    logo_path = Path(__file__).parent / "assets" / "logo_gilmanpro.svg"
    if logo_path.exists():
        slide.shapes.add_picture(str(logo_path), x, y, width=w, height=h)
    else:
        # Fallback: rectángulo emerald con texto
        box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
        box.fill.solid(); box.fill.fore_color.rgb = PRIMARY
        box.line.fill.background()
        tf = box.text_frame
        tf.text = "gilman.pro"
        p = tf.paragraphs[0]
        p.font.name = FONT_TECH
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = WHITE
```

## 3. SLIDES MAESTROS (TEMPLATES)

### Slide de portada (hero)

```python
def add_hero_slide(prs, title, subtitle, description="", ctas=None):
    blank = prs.slide_layouts[6]  # blank layout
    slide = prs.slides.add_slide(blank)

    # Fondo emerald
    set_slide_background(slide, PRIMARY)

    # Overlay sutil
    overlay = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    overlay.fill.solid(); overlay.fill.fore_color.rgb = NAVBAR
    overlay.fill.transparency = 0  # 0 = opaco, ajustar
    overlay.line.fill.background()

    # Logo
    add_logo(slide, Inches(0.5), Inches(0.4), Inches(1.5), Inches(0.5))

    # Título
    title_box = slide.shapes.add_textbox(Inches(1), Inches(2.0), Inches(11.3), Inches(1.5))
    tf = title_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = title
    run.font.name = FONT_HEADING
    run.font.size = Pt(60)
    run.font.bold = True
    run.font.color.rgb = WHITE

    # Subtítulo
    sub_box = slide.shapes.add_textbox(Inches(1), Inches(3.8), Inches(11.3), Inches(0.8))
    tf = sub_box.text_frame
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = subtitle
    run.font.name = FONT_BODY
    run.font.size = Pt(24)
    run.font.color.rgb = WHITE
    run.font.transparency = 0.10

    # Descripción
    if description:
        desc_box = slide.shapes.add_textbox(Inches(2.5), Inches(4.8), Inches(8.3), Inches(1.5))
        tf = desc_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        run = p.add_run()
        run.text = description
        run.font.name = FONT_BODY
        run.font.size = Pt(16)
        run.font.color.rgb = WHITE
        run.font.transparency = 0.20

    # CTAs
    if ctas:
        for i, cta in enumerate(ctas):
            btn = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
                                          Inches(4 + i*2.5), Inches(6.3),
                                          Inches(2.2), Inches(0.6))
            btn.fill.solid()
            btn.fill.fore_color.rgb = WHITE if cta.get("style") == "outline" else PRIMARY_HOVER
            btn.line.color.rgb = WHITE
            btn.line.width = Pt(2) if cta.get("style") == "outline" else Pt(0)
            tf = btn.text_frame
            tf.margin_left = Inches(0.15); tf.margin_right = Inches(0.15)
            p = tf.paragraphs[0]
            p.alignment = PP_ALIGN.CENTER
            run = p.add_run()
            run.text = cta["text"]
            run.font.name = FONT_BODY
            run.font.size = Pt(12)
            run.font.bold = True
            run.font.color.rgb = PRIMARY if cta.get("style") == "outline" else WHITE
```

### Slide de contenido (con H2 + separador + cards)

```python
def add_content_slide(prs, h2_text, cards=None, use_dark=False):
    blank = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank)
    set_slide_background(slide, WHITE if not use_dark else SLATE_900)

    # Logo
    add_logo(slide)

    # H2
    h2_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.4), Inches(12.3), Inches(0.8))
    tf = h2_box.text_frame
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = h2_text
    run.font.name = FONT_HEADING
    run.font.size = Pt(36)
    run.font.bold = True
    run.font.color.rgb = GRAY_900 if not use_dark else WHITE

    # Separador signature
    add_signature_separator(slide, Inches(1.4), use_dark_mode=use_dark)

    # Cards
    if cards:
        card_w = Inches(3.8)
        spacing = Inches(0.4)
        total_w = card_w * len(cards) + spacing * (len(cards) - 1)
        start_x = (prs.slide_width - total_w) / 2
        for i, card in enumerate(cards):
            x = start_x + i * (card_w + spacing)
            add_card(slide, x, Inches(2.2), card_w, Inches(3.5), card, use_dark=use_dark)

    return slide


def add_card(slide, x, y, w, h, data, use_dark=False):
    """Card con border rounded, fondo gris, contenido."""
    # Sombra simulada con rect behind
    shadow = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x + Emu(38100), y + Emu(38100), w, h)
    shadow.fill.solid()
    shadow.fill.fore_color.rgb = GRAY_200 if not use_dark else SLATE_800
    shadow.line.fill.background()

    # Card principal
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
    card.fill.solid()
    card.fill.fore_color.rgb = BG_ALT if not use_dark else SLATE_800
    card.line.color.rgb = GRAY_100 if not use_dark else RGBColor(0xFF, 0xFF, 0xFF)
    card.line.width = Pt(0.5)
    # Ajustar radius
    card.adjustments[0] = 0.08  # ~8% = rounded-xl aproximado

    # Contenido
    tf = card.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2); tf.margin_right = Inches(0.2)
    tf.margin_top = Inches(0.15); tf.margin_bottom = Inches(0.15)

    # Categoría / fecha
    p0 = tf.paragraphs[0]
    p0.alignment = PP_ALIGN.LEFT
    run = p0.add_run()
    run.text = data.get("category", "")
    run.font.name = FONT_BODY
    run.font.size = Pt(10)
    run.font.color.rgb = PRIMARY if not use_dark else INDIGO_500

    # Título
    p1 = tf.add_paragraph()
    p1.space_before = Pt(4)
    run = p1.add_run()
    run.text = data.get("title", "")
    run.font.name = FONT_HEADING
    run.font.size = Pt(16)
    run.font.bold = True
    run.font.color.rgb = GRAY_900 if not use_dark else WHITE

    # Subtítulo
    if data.get("subtitle"):
        p2 = tf.add_paragraph()
        run = p2.add_run()
        run.text = data["subtitle"]
        run.font.name = FONT_BODY
        run.font.size = Pt(12)
        run.font.color.rgb = GRAY_500

    # Descripción
    if data.get("description"):
        p3 = tf.add_paragraph()
        p3.space_before = Pt(4)
        run = p3.add_run()
        run.text = data["description"]
        run.font.name = FONT_BODY
        run.font.size = Pt(10)
        run.font.color.rgb = GRAY_400
```

### Slide de cierre / contacto

```python
def add_contact_slide(prs, contact_info):
    blank = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank)
    set_slide_background(slide, NAVBAR)

    # Logo centrado
    add_logo(slide, Inches(5.5), Inches(2.0), Inches(2.3), Inches(0.8))

    # Título
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(3.2), Inches(12.3), Inches(1))
    tf = title_box.text_frame
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = contact_info.get("title", "Contáctame")
    run.font.name = FONT_HEADING
    run.font.size = Pt(48)
    run.font.bold = True
    run.font.color.rgb = WHITE

    # Email
    email_box = slide.shapes.add_textbox(Inches(0.5), Inches(4.5), Inches(12.3), Inches(0.5))
    p = email_box.text_frame.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run = p.add_run()
    run.text = contact_info.get("email", "")
    run.font.name = FONT_BODY
    run.font.size = Pt(20)
    run.font.color.rgb = ACCENT
```

## 4. USO COMPLETO

```python
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# Slide 1: Portada
add_hero_slide(
    prs,
    title="Gilberto Castillo",
    subtitle="Ingeniero en Telecomunicaciones | Especialista en Big Data y Data Science | Desarrollador de Soluciones",
    description="5+ años desarrollando soluciones tecnológicas que resuelven problemas críticos.",
    ctas=[
        {"text": "Descargar CV", "style": "solid"},
        {"text": "Ver Portafolio", "style": "outline"}
    ]
)

# Slide 2: Experiencia
add_content_slide(
    prs,
    h2_text="Experiencia",
    cards=[
        {"category": "Junio 2025 — Presente", "title": "Analista de Programación", "subtitle": "MiBus S.A.", "description": "Transmisión de datos y reportes operativos clave."},
        {"category": "Junio 2023 — Junio 2024", "title": "Auxiliar de Programación", "subtitle": "MiBus S.A.", "description": "Reportes operativos y planificación de flota."},
        {"category": "Diciembre 2020 — Junio 2023", "title": "Técnico de Soporte", "subtitle": "MiBus S.A.", "description": "Diagnóstico y reparación de hardware/software."},
    ]
)

# Slide 3: Habilidades
add_content_slide(
    prs,
    h2_text="Habilidades Técnicas",
    cards=[
        {"title": "Big Data & Data Science", "description": "Pandas, NumPy, Scikit-learn, Pentaho ETL"},
        {"title": "Redes y Telecomunicaciones", "description": "TCP/IP, MQTT, Routing & Switching"},
        {"title": "Infraestructura TI", "description": "Docker, Linux, Git, VPS, Ciberseguridad"},
    ]
)

# Slide 4: Contacto
add_contact_slide(prs, {
    "title": "Contáctame",
    "email": "contacto@gilman.pro"
})

prs.save("presentacion-gilmanpro.pptx")
```

## 5. REGLAS

1. **Tipografía:** cargar Montserrat, Lato, Orbitron, Rajdhani en el sistema antes de generar. Si no están, usar Calibri (fallback) y avisar.
2. **Logo:** insertar SVG en cada slide en la esquina superior izquierda.
3. **Separador signature:** bajo cada H2 — es la firma visual.
4. **Botones:** `ROUNDED_RECTANGLE` con `adjustments[0] = 0.20` para `rounded-lg`.
5. **Cards:** `ROUNDED_RECTANGLE` con `adjustments[0] = 0.08` para `rounded-xl`.
6. **Backgrounds:** usar `set_slide_background` para slides completos, `BG_ALT` para alternar.
7. **Colores:** siempre de la paleta. No inventar HEX.
8. **Footer:** incluir en cada slide (excepto portada y contacto) línea con `© 2026 gilman.pro` en `GRAY_400`, tamaño 8pt.

## 6. ERRORES COMUNES

- ❌ Olvidar `word_wrap = True` en textboxes → texto se sale
- ❌ Usar `Emu(38100)` directamente sin `from pptx.util import Emu`
- ❌ Aplicar `fill.transparency` antes de definir `fill.solid()`
- ❌ Usar nombres de color en lugar de `RGBColor` → el color se muestra negro
- ❌ No verificar que la fuente está instalada en el sistema → PowerPoint la reemplaza
