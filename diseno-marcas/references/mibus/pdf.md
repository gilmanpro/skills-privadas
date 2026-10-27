# Guía: Aplicar Diseño MiBus a PDF

> Cómo generar reportes PDF, informes, folletos, manuales, etc. con la identidad visual de MiBus.

## 📋 Antes de empezar

1. Lee `assets/brand-mibus.json` y `assets/colors-mibus.md` de esta skill.
2. Descarga assets a `WORKDIR/ASSETS/`:
   - Logo: `logo.png`
   - Background: `bg-stats.jpg` (si necesitas portada con imagen)
3. **Carga la skill `pdf`** del sistema opencode y sigue su flujo de trabajo.
4. Combina: identidad MiBus (esta skill) + buenas prácticas PDF (skill `pdf`).

## 🎨 Aplicación por tipo de PDF

### 1. Reporte / Informe corporativo

**Estructura:**

```
Página 1 (Portada):
┌──────────────────────────────────────────┐
│ [Background: bg-stats.jpg                │
│  o color #283C90 sólido]                 │
│                                          │
│         [LOGO MiBus 4cm]                 │
│                                          │
│  TÍTULO DEL INFORME                      │
│  (Poppins 700, 36pt, blanco)             │
│                                          │
│  Subtítulo descriptivo                   │
│  (Roboto 400, 18pt, blanco)              │
│                                          │
│  ───                                     │
│  MiBus · Junio 2026                      │
│                                          │
└──────────────────────────────────────────┘

Páginas 2+ (Contenido):
┌──────────────────────────────────────────┐
│ [Header: banda primary + logo mini]     │
├──────────────────────────────────────────┤
│                                          │
│  SECCIÓN (Poppins 700, 20pt, primary)    │
│  ─── (línea primary)                     │
│                                          │
│  Contenido en Roboto 11pt...             │
│                                          │
│  • Bullet 1                              │
│  • Bullet 2                              │
│                                          │
├──────────────────────────────────────────┤
│ [Footer: banda dark + info + página]     │
└──────────────────────────────────────────┘
```

### 2. Folleto / Brochure (1-2 páginas)

- **Página 1 (exterior):** imagen corporativa grande + título + CTA
- **Página 2 (interior):** servicios, stats, contacto

### 3. Manual / Documentación técnica

- Header con logo y nombre del manual
- Numeración de página
- Tabla de contenidos
- Secciones claramente diferenciadas con colores primary

## 🛠️ Implementación con ReportLab (Python)

### Setup básico

```python
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.units import cm, mm, inch
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, 
    Table, TableStyle, PageBreak, KeepTogether,
    BaseDocTemplate, PageTemplate, Frame, NextPageTemplate
)
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# Colores MiBus
MIBUS_PRIMARY = HexColor("#283C90")
MIBUS_PRIMARY_DARK = HexColor("#1B2A66")
MIBUS_SECONDARY = HexColor("#205CA7")
MIBUS_SECONDARY_HOVER = HexColor("#409EFF")
MIBUS_ACCENT = HexColor("#1DA1F2")
MIBUS_DARK = HexColor("#1A1A2E")
MIBUS_WHITE = HexColor("#FFFFFF")
MIBUS_TEXT = HexColor("#333333")
MIBUS_BORDER = HexColor("#E0E0E0")
MIBUS_STRIPE = HexColor("#F0F0F0")
MIBUS_SUCCESS = HexColor("#B5D531")
MIBUS_ERROR = HexColor("#BC0C06")
```

### Registrar fuentes Poppins y Roboto

```python
def register_mibus_fonts():
    """Registra Poppins y Roboto para usar en el PDF."""
    try:
        # Intentar registrar las fuentes desde la carpeta de trabajo
        font_dir = "ASSETS/fonts"  # Asumir que el usuario descargó las fuentes aquí
        
        pdfmetrics.registerFont(TTFont("Poppins", os.path.join(font_dir, "Poppins-Regular.ttf")))
        pdfmetrics.registerFont(TTFont("Poppins-Bold", os.path.join(font_dir, "Poppins-Bold.ttf")))
        pdfmetrics.registerFont(TTFont("Poppins-SemiBold", os.path.join(font_dir, "Poppins-SemiBold.ttf")))
        pdfmetrics.registerFont(TTFont("Roboto", os.path.join(font_dir, "Roboto-Regular.ttf")))
        pdfmetrics.registerFont(TTFont("Roboto-Bold", os.path.join(font_dir, "Roboto-Bold.ttf")))
        pdfmetrics.registerFont(TTFont("Roboto-Italic", os.path.join(font_dir, "Roboto-Italic.ttf")))
        return True
    except:
        # Fallback a fuentes por defecto
        print("⚠️ No se encontraron Poppins/Roboto. Usando fuentes por defecto.")
        return False
```

### Estilos de párrafo

```python
def create_mibus_styles():
    """Crea estilos de párrafo con identidad MiBus."""
    styles = getSampleStyleSheet()
    
    # Título portada
    styles.add(ParagraphStyle(
        name="MibusCoverTitle",
        fontName="Poppins-Bold",
        fontSize=36,
        textColor=MIBUS_WHITE,
        alignment=TA_CENTER,
        leading=42,
        spaceAfter=12
    ))
    
    # Subtítulo portada
    styles.add(ParagraphStyle(
        name="MibusCoverSubtitle",
        fontName="Roboto",
        fontSize=18,
        textColor=MIBUS_WHITE,
        alignment=TA_CENTER,
        leading=22,
        spaceAfter=24
    ))
    
    # H1 sección
    styles.add(ParagraphStyle(
        name="MibusH1",
        fontName="Poppins-Bold",
        fontSize=20,
        textColor=MIBUS_PRIMARY,
        alignment=TA_LEFT,
        leading=24,
        spaceBefore=18,
        spaceAfter=8
    ))
    
    # H2 subsección
    styles.add(ParagraphStyle(
        name="MibusH2",
        fontName="Poppins-SemiBold",
        fontSize=14,
        textColor=MIBUS_PRIMARY,
        alignment=TA_LEFT,
        leading=18,
        spaceBefore=12,
        spaceAfter=6
    ))
    
    # H3
    styles.add(ParagraphStyle(
        name="MibusH3",
        fontName="Poppins-SemiBold",
        fontSize=12,
        textColor=MIBUS_SECONDARY,
        alignment=TA_LEFT,
        leading=15,
        spaceBefore=8,
        spaceAfter=4
    ))
    
    # Body
    styles.add(ParagraphStyle(
        name="MibusBody",
        fontName="Roboto",
        fontSize=11,
        textColor=MIBUS_TEXT,
        alignment=TA_JUSTIFY,
        leading=15,
        spaceAfter=6
    ))
    
    # Bullet
    styles.add(ParagraphStyle(
        name="MibusBullet",
        fontName="Roboto",
        fontSize=11,
        textColor=MIBUS_TEXT,
        alignment=TA_LEFT,
        leading=15,
        leftIndent=20,
        bulletIndent=8,
        spaceAfter=3
    ))
    
    # Caption
    styles.add(ParagraphStyle(
        name="MibusCaption",
        fontName="Roboto-Italic",
        fontSize=9,
        textColor=HexColor("#666666"),
        alignment=TA_LEFT,
        leading=12,
        spaceAfter=6
    ))
    
    return styles
```

### Header y footer en cada página

```python
def add_header_footer(canvas_obj, doc):
    """Callback que añade header y footer MiBus en cada página."""
    canvas_obj.saveState()
    
    page_num = canvas_obj.getPageNumber()
    page_width, page_height = A4
    
    # Saltar header/footer en la portada (página 1)
    if page_num == 1:
        canvas_obj.restoreState()
        return
    
    # Header (banda primary)
    canvas_obj.setFillColor(MIBUS_PRIMARY)
    canvas_obj.rect(0, page_height - 1.2*cm, page_width, 1.2*cm, fill=1, stroke=0)
    
    # Logo en header (esquina izquierda)
    if os.path.exists("ASSETS/logo.png"):
        canvas_obj.drawImage(
            "ASSETS/logo.png",
            1*cm, page_height - 1.0*cm,
            width=3*cm, height=0.8*cm,
            preserveAspectRatio=True
        )
    
    # Texto header (a la derecha del logo)
    canvas_obj.setFont("Poppins-Bold", 11)
    canvas_obj.setFillColor(MIBUS_WHITE)
    canvas_obj.drawString(5*cm, page_height - 0.7*cm, "MiBus · Transporte Masivo de Panamá")
    
    # Línea divisora primary
    canvas_obj.setStrokeColor(MIBUS_PRIMARY_DARK)
    canvas_obj.setLineWidth(0.5)
    canvas_obj.line(0, page_height - 1.2*cm, page_width, page_height - 1.2*cm)
    
    # Footer (banda dark)
    canvas_obj.setFillColor(MIBUS_DARK)
    canvas_obj.rect(0, 0, page_width, 0.8*cm, fill=1, stroke=0)
    
    # Texto footer izquierda
    canvas_obj.setFont("Roboto", 8)
    canvas_obj.setFillColor(MIBUS_WHITE)
    canvas_obj.drawString(1*cm, 0.3*cm, "www.mibus.com.pa · contacto@mibus.com.pa")
    
    # Página footer derecha
    canvas_obj.drawRightString(page_width - 1*cm, 0.3*cm, f"Página {page_num}")
    
    canvas_obj.restoreState()


def add_cover_page_background(canvas_obj, doc):
    """Callback especial para la portada con background primary."""
    canvas_obj.saveState()
    
    page_width, page_height = A4
    
    # Background primary full
    canvas_obj.setFillColor(MIBUS_PRIMARY)
    canvas_obj.rect(0, 0, page_width, page_height, fill=1, stroke=0)
    
    # O usar imagen de fondo
    if os.path.exists("ASSETS/bg-stats.jpg"):
        canvas_obj.drawImage(
            "ASSETS/bg-stats.jpg",
            0, 0, width=page_width, height=page_height,
            preserveAspectRatio=False
        )
        # Overlay oscuro
        canvas_obj.setFillColor(HexColor("#283C90", alpha=0.7))
        # ReportLab no soporta alpha nativo, usar gris oscuro
        # Workaround: dibujar rect con opacidad manual
    
    canvas_obj.restoreState()
```

### Portada con background

```python
def create_cover_page(styles, title, subtitle, logo_path="ASSETS/logo.png"):
    """Crea los elementos de la portada."""
    elements = []
    
    # Logo centrado
    if os.path.exists(logo_path):
        img = Image(logo_path, width=8*cm, height=4*cm)
        img.hAlign = "CENTER"
        elements.append(Spacer(1, 6*cm))
        elements.append(img)
        elements.append(Spacer(1, 2*cm))
    
    # Título
    elements.append(Paragraph(title, styles["MibusCoverTitle"]))
    elements.append(Spacer(1, 0.5*cm))
    
    # Subtítulo
    elements.append(Paragraph(subtitle, styles["MibusCoverSubtitle"]))
    
    # Salto de página
    elements.append(NextPageTemplate("Content"))
    elements.append(PageBreak())
    
    return elements
```

### Tabla con estilo MiBus

```python
def create_mibus_table(data, has_header=True):
    """Crea una tabla con estilo MiBus."""
    table = Table(data, colWidths=[4*cm, 4*cm, 4*cm, 4*cm])
    
    style_cmds = [
        # Bordes sutiles
        ("GRID", (0, 0), (-1, -1), 0.5, MIBUS_BORDER),
        # Padding
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        # Alineación
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]
    
    if has_header:
        style_cmds.extend([
            # Header primary
            ("BACKGROUND", (0, 0), (-1, 0), MIBUS_PRIMARY),
            ("TEXTCOLOR", (0, 0), (-1, 0), MIBUS_WHITE),
            ("FONTNAME", (0, 0), (-1, 0), "Poppins-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 11),
            ("ALIGN", (0, 0), (-1, 0), "CENTER"),
        ])
        
        # Stripe pattern para body
        for i in range(1, len(data)):
            if i % 2 == 0:
                style_cmds.append(
                    ("BACKGROUND", (0, i), (-1, i), MIBUS_STRIPE)
                )
    
    table.setStyle(TableStyle(style_cmds))
    return table
```

### Función principal para generar PDF

```python
def generate_mibus_pdf(
    output_path,
    title,
    subtitle,
    content_elements,
    logo_path="ASSETS/logo.png"
):
    """Genera un PDF completo con identidad MiBus."""
    
    # Registrar fuentes
    register_mibus_fonts()
    
    # Crear estilos
    styles = create_mibus_styles()
    
    # Crear documento
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        topMargin=2*cm,
        bottomMargin=1.5*cm,
        leftMargin=2*cm,
        rightMargin=2*cm,
        title=title,
        author="Gilberto Castillo - Analista de Programación, MiBus"
    )
    
    # Elementos del documento
    elements = []
    elements.extend(create_cover_page(styles, title, subtitle, logo_path))
    elements.extend(content_elements)
    
    # Generar PDF
    doc.build(elements, onFirstPage=add_cover_page_background, onLaterPages=add_header_footer)


# Ejemplo de uso
content = [
    Paragraph("Sección 1: Introducción", styles["MibusH1"]),
    Paragraph("Este es el contenido de la primera sección del documento...", styles["MibusBody"]),
    Spacer(1, 0.5*cm),
    Paragraph("Subsección 1.1", styles["MibusH2"]),
    Paragraph("Texto de la subsección...", styles["MibusBody"]),
]

generate_mibus_pdf(
    output_path="OUTPUT/reporte.pdf",
    title="Reporte Mensual de Operaciones",
    subtitle="MiBus · Junio 2026",
    content_elements=content
)
```

## ✅ Checklist para PDF MiBus

- [ ] Logo MiBus en header de TODAS las páginas
- [ ] Footer con info corporativa + número de página
- [ ] Portada con background primary o bg-stats.jpg
- [ ] Títulos H1 en Poppins Bold primary
- [ ] Body en Roboto 11pt justificado
- [ ] Tablas con header primary y stripes
- [ ] Embedir Poppins y Roboto en el PDF (no usar fuentes default)
- [ ] Márgenes: 2cm todos los lados
- [ ] Sin emojis, sin imágenes de stock genéricas

## 🚫 Errores comunes

- ❌ PDF generado con Helvetica/Times default
- ❌ Sin header/footer en páginas interiores
- ❌ Portada solo con texto sobre blanco
- ❌ Colores fuera de paleta
- ❌ Tablas con bordes negros gruesos
- ❌ Sin logo en ninguna página
