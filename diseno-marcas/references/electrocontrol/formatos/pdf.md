# Aplicación del diseño Electrocontrol a PDF

Guía para crear PDFs con el sistema de diseño de IoT Tech / Electrocontrol. **Esta skill NO reemplaza la skill `pdf`** — la complementa.

---

## Regla de carpetas de trabajo (OBLIGATORIA) — SIEMPRE

```bash
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
WORKDIR=".tmp/pdf-electrocontrol-$TIMESTAMP"
mkdir "$WORKDIR"
cp "<base-dir-skill>/assets/logo-electrocontrol.jpg" "$WORKDIR/"
```

**POR QUÉ:** la skill `pdf` SIEMPRE se ejecuta desde la carpeta temporal global de opencode (no la raíz del proyecto) para evitar contaminar el workspace del usuario. Combinar con la skill `diseno-electrocontrol` mantiene la coherencia.

Trabaja SIEMPRE dentro de `WORKDIR`. Al terminar, copia el PDF al destino. La carpeta temporal puede borrarse después (preguntar antes).

---

## Cuándo usar dark mode vs. light mode

PDF es el formato final, así que la elección del modo depende del uso:

| Documento | Modo | Razón |
|---|---|---|
| **Factura** | **Light** | Estándar fiscal, imprimible |
| **Cotización / Propuesta** | **Light** | Profesional, imprimible |
| **Reporte técnico** | **Light** | Imprimible, lectura en papel |
| **Contrato** | **Light** | Legal, imprimible |
| **Manual de usuario** | **Light** con header dark | Profesional + marca |
| **White paper / dossier** | **Dark** (marketing) | Engagement, share digital |
| **Newsletter** | **Dark** (presentación) | Engagement |
| **One-pager promocional** | **Dark** (marketing) | Captación |
| **Portafolio / CV** | **Light** con header dark | Profesional |
| **Caso de estudio** | **Light** con acentos dark | Marketing serio |
| **Reporte mensual** | **Light** con acentos dark | Lectura cómoda |
| **Tarjeta de presentación** | **Dark** | Marketing personal |
| **Certificado** | **Light** con bordes dark | Formal + marca |

**Regla práctica:**
- Documentos formales / imprimibles → **light**
- Marketing / engagement / share → **dark**
- Informes de gestión → **light con header dark**

---

## Herramientas para crear PDF

| Herramienta | Caso de uso | Ventaja |
|---|---|---|
| **ReportLab** (Python) | Programático, control total | Más flexible, genera PDF nativo |
| **FPDF** (Python) | Simple, rápido | Curva de aprendizaje baja |
| **WeasyPrint** (Python) | HTML → PDF | Mantiene diseño web oscuro |
| **Playwright/Chromium** (Python) | HTML → PDF con motor Chrome | Mejor soporte CSS, degradados |
| **Puppeteer** (Node) | HTML → PDF | Igual que Playwright |
| **wkhtmltopdf** | HTML → PDF | Rápido para HTML simple |
| **Conversión desde Office** | Word/Excel/PowerPoint → PDF | Mantiene el diseño original |
| **Conversión desde Canva/Figma** | Diseño → PDF | Más control visual |

**Para dark mode con degradados:** usa Playwright o WeasyPrint. ReportLab/FPDF son limitados para degradados.

**Para light mode con tablas:** ReportLab es ideal.

---

## Plantilla base

### Tamaño de página

| Formato | Dimensiones | Uso |
|---|---|---|
| **A4 vertical** | 210x297mm | Estándar corporativo |
| **A4 horizontal** | 297x210mm | Tablas grandes, diagramas |
| **Carta (Letter)** | 216x279mm | Estándar USA (poco usado en Panamá) |
| **A5** | 148x210mm | Folleto, manual compacto |
| **Personalizado cuadrado** | 200x200mm | Tarjeta de presentación, one-pager |

**Por defecto usa A4 vertical (210x297mm).**

### Márgenes

| Margen | Valor |
|---|---|
| Superior | 20mm |
| Inferior | 20mm |
| Izquierdo | 20mm |
| Derecho | 20mm |
| Header | 10mm |
| Footer | 10mm |

### Header (todas las páginas excepto portada)

```
[LOGO 25mm]   [Texto del documento]              [Fecha]
```

### Footer (todas las páginas)

```
IoT Tech · Electrocontrol · http://pag.electrocontrol.cloud/    Página X de Y
```

---

## Generación de PDFs con la web como base (Playwright)

Si quieres el PDF con la estética exacta de la web, usa Playwright. El sitio web está construido con Next.js + Tailwind, así que puedes:

**Opción A — Exportar el sitio web existente a PDF:**
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("http://pag.electrocontrol.cloud/", wait_until="networkidle")
    page.pdf(
        path="electrocontrol-web.pdf",
        format="A4",
        print_background=True,  # CRÍTICO para mantener colores dark
        margin={"top": "0", "bottom": "0", "left": "0", "right": "0"}
    )
    browser.close()
```

**Opción B — Crear HTML propio con la estética y convertirlo:**
```python
html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet">
  <style>
    @page { size: A4; margin: 20mm; }
    body {
      font-family: 'Inter', sans-serif;
      background: linear-gradient(135deg, #0F172A 0%, #1E293B 50%, #0F172A 100%);
      color: #FFFFFF;
      -webkit-font-smoothing: antialiased;
    }
    h1 {
      background: linear-gradient(90deg, #22D3EE 0%, #C084FC 50%, #F472B6 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      font-size: 48px;
      font-weight: 700;
    }
    /* ... más estilos ... */
  </style>
</head>
<body>
  <!-- contenido -->
</body>
</html>
"""

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.set_content(html_content)
    page.pdf(
        path="documento-electrocontrol.pdf",
        format="A4",
        print_background=True,
        margin={"top": "20mm", "bottom": "20mm", "left": "20mm", "right": "20mm"}
    )
    browser.close()
```

---

## Generación de PDFs con ReportLab (light mode)

```python
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

# Colores de marca
CYAN_500 = HexColor("#06B6D4")
PURPLE_500 = HexColor("#A855F7")
PINK_500 = HexColor("#EC4899")
SLATE_900 = HexColor("#0F172A")
SLATE_800 = HexColor("#1E293B")
SLATE_300 = HexColor("#CBD5E1")
SLATE_400 = HexColor("#94A3B8")
WHITE = HexColor("#FFFFFF")
CYAN_100 = HexColor("#CFFAFE")
SLATE_100 = HexColor("#F1F5F9")
SLATE_200 = HexColor("#E2E8F0")

# Crear documento
doc = SimpleDocTemplate(
    "cotizacion-electrocontrol.pdf",
    pagesize=A4,
    leftMargin=20*mm, rightMargin=20*mm,
    topMargin=20*mm, bottomMargin=20*mm
)

# Estilos
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle', parent=styles['Heading1'],
    fontSize=24, textColor=SLATE_900, alignment=TA_LEFT,
    spaceAfter=12, fontName='Helvetica-Bold'
)
subtitle_style = ParagraphStyle(
    'CustomSubtitle', parent=styles['Normal'],
    fontSize=11, textColor=HexColor('#64748B'),
    spaceAfter=18
)
h2_style = ParagraphStyle(
    'CustomH2', parent=styles['Heading2'],
    fontSize=16, textColor=CYAN_500, alignment=TA_LEFT,
    spaceAfter=10, fontName='Helvetica-Bold'
)
body_style = ParagraphStyle(
    'CustomBody', parent=styles['Normal'],
    fontSize=11, textColor=SLATE_800, alignment=TA_LEFT,
    spaceAfter=8
)

# Contenido
story = []

# Logo
logo = Image("logo-electrocontrol.jpg", width=30*mm, height=30*mm)
story.append(logo)
story.append(Spacer(1, 10))

# Título
story.append(Paragraph("COTIZACIÓN", title_style))
story.append(Paragraph("Cliente: {{nombre}} · Fecha: {{fecha}}", subtitle_style))

# Línea accent
story.append(Spacer(1, 5))
# (En ReportLab, una línea se dibuja con canvas, no con flowables)
# Alternativa: usar tabla 1x1 con fondo cyan

# H2
story.append(Paragraph("1. Alcance del proyecto", h2_style))

# Body
story.append(Paragraph(
    "IoT Tech (Electrocontrol) ofrece los siguientes servicios:",
    body_style
))

# Tabla
data = [
    ["#", "Servicio", "Cantidad", "P. Unit", "Total"],
    ["1", "IoT & Desarrollo", "1", "$1,500.00", "$1,500.00"],
    ["2", "Reparación ECU", "1", "$800.00", "$800.00"],
    ["3", "Automatización", "1", "$2,000.00", "$2,000.00"],
    ["4", "Programación", "1", "$1,200.00", "$1,200.00"],
    ["", "", "", "TOTAL", "$5,885.00"],
]
table = Table(data, colWidths=[15*mm, 70*mm, 25*mm, 30*mm, 30*mm])
table.setStyle(TableStyle([
    # Header
    ('BACKGROUND', (0, 0), (-1, 0), CYAN_500),
    ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 11),
    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
    ('TOPPADDING', (0, 0), (-1, 0), 8),
    # Filas alternas
    ('BACKGROUND', (0, 1), (-1, -2), WHITE),
    ('ROWBACKGROUNDS', (0, 1), (-1, -2), [WHITE, SLATE_100]),
    # Total
    ('BACKGROUND', (0, -1), (-1, -1), CYAN_100),
    ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
    ('FONTSIZE', (0, -1), (-1, -1), 12),
    # Bordes
    ('GRID', (0, 0), (-1, -1), 0.5, SLATE_200),
    ('LINEABOVE', (0, -1), (-1, -1), 2, CYAN_500),
    # Padding
    ('TOPPADDING', (0, 1), (-1, -1), 6),
    ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
]))
story.append(table)
story.append(Spacer(1, 12))

# Datos de contacto
story.append(Paragraph("Datos de contacto", h2_style))
story.append(Paragraph("Malkom Daniel Cordoba · +507 6250-9318", body_style))
story.append(Paragraph("http://pag.electrocontrol.cloud/", body_style))
story.append(Paragraph("https://wa.me/50762509318", body_style))

# Construir PDF
doc.build(story)
```

**Para ReportLab con fuentes Inter**: hay que descargar el .ttf y registrarlo:
```python
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('Inter', 'Inter-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Inter-Bold', 'Inter-Bold.ttf'))
# Luego usar fontName='Inter' en los estilos
```

---

## Generación de PDFs con FPDF (más simple)

```python
from fpdf import FPDF

class ElectrocontrolPDF(FPDF):
    def header(self):
        # Logo
        self.image('logo-electrocontrol.jpg', 10, 8, 25)
        # Marca
        self.set_font('helvetica', 'B', 14)
        self.set_text_color(15, 23, 42)  # slate-900
        self.cell(0, 10, 'IoT Tech · Electrocontrol', 0, 1, 'R')
        # Línea accent
        self.set_draw_color(6, 182, 212)  # cyan-500
        self.set_line_width(0.5)
        self.line(10, 30, 200, 30)
        self.ln(15)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', '', 8)
        self.set_text_color(100, 116, 139)  # slate-500
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

pdf = ElectrocontrolPDF()
pdf.add_page()
pdf.set_font('helvetica', '', 11)
# ... contenido ...
pdf.output('documento.pdf')
```

---

## Estilos según modo

### Light mode (recomendado para documentos formales)

| Elemento | Estilo |
|---|---|
| **Fondo de página** | Blanco (#FFFFFF) |
| **Texto principal** | slate-900 (#0F172A) |
| **Texto secundario** | slate-500 (#64748B) |
| **H1** | slate-900, Inter Bold, 24pt |
| **H2** | cyan-500, Inter Bold, 16pt |
| **Acentos** | cyan-500, purple-500 |
| **Tablas header** | cyan-500 fondo, blanco texto |
| **Tablas filas alternas** | blanco / slate-100 |
| **Línea decorativa** | cyan-500, 0.5pt |

### Dark mode (marketing/presentación)

| Elemento | Estilo |
|---|---|
| **Fondo de página** | slate-900 (#0F172A) con degradado a slate-800 |
| **Texto principal** | Blanco (#FFFFFF) |
| **Texto secundario** | slate-300 (#CBD5E1) |
| **H1** | Degradado cyan→purple→pink, 36-48pt |
| **H2** | cyan-400, 24pt |
| **Acentos** | cyan-400, purple-400, pink-400 |
| **Cards** | slate-800/50 fondo, slate-700/50 borde, 1rem radius |
| **Decoración** | Blobs blur cyan y purple, opacidad 10% |

---

## Características especiales

### Encabezados y pies de página

Usa `canvas.Canvas` o `PageTemplate` de ReportLab para headers/footers repetidos:

```python
def header_footer(canvas, doc):
    canvas.saveState()
    # Header
    canvas.setFillColor(HexColor('#0F172A'))
    canvas.rect(0, 280*mm, 210*mm, 17*mm, fill=True, stroke=False)
    canvas.setFillColor(WHITE)
    canvas.setFont('Helvetica-Bold', 12)
    canvas.drawString(20*mm, 290*mm, 'IoT Tech · Electrocontrol')
    # Footer
    canvas.setFillColor(HexColor('#94A3B8'))
    canvas.setFont('Helvetica', 8)
    canvas.drawString(20*mm, 10*mm, 'Malkom Cordoba · +507 6250-9318')
    canvas.drawRightString(190*mm, 10*mm, f'Página {doc.page}')
    canvas.restoreState()

doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
```

### Numeración de páginas

```python
from reportlab.pdfgen.canvas import Canvas
canvas.drawString(500, 50, f"Página {page_number}")
```

### Tabla de contenidos

Para PDFs largos, genera TOC con hyperlinks. Más simple: usa Word con TOC automático, exporta a PDF.

### Bookmarks / marcadores

```python
# ReportLab
bookmark = canvas.bookmarkPage('servicios')
canvas.addOutlineEntry('Servicios', 'servicios', level=0)
```

### Hipervínculos

```python
# ReportLab
from reportlab.platypus import Paragraph
link = Paragraph('<link href="https://wa.me/50762509318">WhatsApp</link>', style)
```

### Marca de agua (watermark)

```python
# ReportLab
def add_watermark(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(HexColor('#06B6D4'))
    canvas.setFont('Helvetica-Bold', 80)
    canvas.setFillAlpha(0.05)  # 5% opacity
    canvas.rotate(45)
    canvas.drawCentredString(400, 100, 'ELECTROCONTROL')
    canvas.restoreState()
```

---

## Combinar con otras herramientas

### Desde Word

```bash
# Word tiene "Guardar como PDF" nativo
# O desde línea de comandos con Office instalado:
# (Mejor: abrir el .docx en Word, Archivo > Guardar como > PDF)
```

### Desde PowerPoint

```bash
# PowerPoint > Archivo > Guardar como > PDF
# O con libreoffice en headless:
libreoffice --headless --convert-to pdf presentacion.pptx
```

### Desde Excel

```bash
# Excel > Archivo > Guardar como > PDF
libreoffice --headless --convert-to pdf hoja.xlsx
```

### Desde HTML (con marca completa)

```python
# Playwright (recomendado)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("file:///path/to/document.html", wait_until="networkidle")
    page.pdf(path="output.pdf", format="A4", print_background=True)
    browser.close()
```

### Desde Figma / Canva

- **Figma:** Archivo > Save as > PDF (preset "Presentation" o "Custom")
- **Canva:** Compartir > Descargar > PDF Print (para impresión) o PDF Standard (digital)

---

## Optimización del PDF

| Aspecto | Recomendación |
|---|---|
| **Tamaño** | Comprimir imágenes a 150-300 DPI |
| **Fuentes** | Incrustar todas las fuentes usadas (subset si es posible) |
| **Imágenes** | JPEG para fotos, PNG para logos, SVG vectorial si se soporta |
| **Compresión** | Usar `gs` (Ghostscript) para comprimir: `gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dBATCH -sOutputFile=output.pdf input.pdf` |
| **Accesibilidad** | Agregar tags para lectores de pantalla, definir idioma del documento |
| **PDF/A** | Para archivado legal, convertir a PDF/A con `gs` |

---

## Recursos

- **Logo:** `assets/logo-electrocontrol.jpg`
- **Fuentes:** Inter de Google Fonts (https://fonts.google.com/specimen/Inter)
- **Skill complementaria:** `pdf` (cargar ANTES — usar `WORKDIR` global de opencode)
- **Iconos:** Lucide icons en SVG

---

## Checklist antes de entregar

- [ ] ¿PDF generado desde `WORKDIR` (no raíz del proyecto)?
- [ ] ¿Modo dark o light apropiado para el documento?
- [ ] ¿Colores de marca respetados? (cyan, purple, pink, slate)
- [ ] ¿Header con logo en todas las páginas?
- [ ] ¿Footer con número de página y contacto?
- [ ] ¿Datos de contacto correctos? (+507 6250-9318, web, WhatsApp)
- [ ] ¿Tamaño de archivo razonable? (<5MB idealmente)
- [ ] ¿Fuentes incrustadas?
- [ ] ¿PDF/A si es documento legal?
- [ ] ¿Marcadores/Bookmarks si el documento es largo?
- [ ] ¿Texto con contraste WCAG AA? (slate-300+ sobre dark, slate-700+ sobre light)
