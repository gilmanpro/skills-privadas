# Aplicación a PDF — gilman.pro

Cómo aplicar el branding gilman.pro a documentos PDF. Dos enfoques:

1. **HTML → PDF** (recomendado): usar WeasyPrint o Playwright para máxima fidelidad visual
2. **ReportLab** (nativo Python): control total sobre el PDF, más código

---

## ENFOQUE 1: HTML → PDF (RECOMENDADO)

Genera HTML con la marca gilman y lo convierte a PDF. Mantiene tipografías, colores y el separador signature.

### Con WeasyPrint (ligero, sin navegador)

```python
from weasyprint import HTML, CSS
from pathlib import Path

# Cargar la skill palette y referencias
SKILL_DIR = Path(__file__).parent.parent  # diseno-gilman/
PALETTE = json.load(open(SKILL_DIR / "assets" / "palette-gilman.json"))

# HTML con branding gilman
html_content = f"""
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&family=Lato:wght@300;400;700&family=Orbitron:wght@400;500;600;700;800;900&family=Rajdhani:wght@300;400;500;600;700&display=swap">
  <style>
    @page {{
      size: A4;
      margin: 2.5cm 2cm;
      @bottom-center {{
        content: counter(page) " / " counter(pages);
        font-family: 'Rajdhani', sans-serif;
        font-size: 9pt;
        color: #6B7280;
      }}
      @bottom-left {{
        content: "© 2026 gilman.pro";
        font-family: 'Rajdhani', sans-serif;
        font-size: 9pt;
        color: #6B7280;
      }}
    }}
    
    @page :first {{
      margin: 0;
      @bottom-center {{ content: ""; }}
      @bottom-left {{ content: ""; }}
    }}
    
    body {{
      font-family: 'Lato', sans-serif;
      color: #111827;
      line-height: 1.6;
      font-size: 11pt;
    }}
    
    h1, h2, h3, h4 {{
      font-family: 'Montserrat', sans-serif;
      color: #111827;
    }}
    
    h1 {{
      font-size: 28pt;
      font-weight: 800;
      color: #047857;
      border-left: 4pt solid #10B981;
      padding-left: 12pt;
      margin-top: 24pt;
    }}
    
    h2 {{
      font-size: 20pt;
      font-weight: 700;
      color: #111827;
      margin-top: 20pt;
    }}
    
    h3 {{
      font-size: 14pt;
      font-weight: 600;
      color: #059669;
    }}
    
    .separator {{
      display: flex;
      align-items: center;
      margin: 8pt 0 16pt 0;
    }}
    .separator .line {{ height: 1.5pt; background: #10B981; }}
    .separator .line.short {{ width: 30pt; }}
    .separator .line.long {{ width: 48pt; }}
    .separator .line.violet {{ background: #8B5CF6; }}
    .separator .dot {{
      width: 6pt; height: 6pt;
      border-radius: 50%;
      background: #10B981;
      margin: 0 6pt;
    }}
    .separator .dot.violet {{ background: #8B5CF6; }}
    
    /* Cover */
    .cover {{
      page-break-after: always;
      height: 100vh;
      background: linear-gradient(135deg, #10B981 0%, #06B6D4 100%);
      color: white;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: 4cm 2cm;
    }}
    .cover h1 {{
      color: white;
      font-size: 40pt;
      font-weight: 800;
      border: none;
      padding: 0;
      margin: 12pt 0;
    }}
    .cover h2 {{
      color: white;
      font-size: 18pt;
      font-weight: 300;
    }}
    .cover img {{ width: 200pt; margin-bottom: 24pt; }}
    .cover .contact {{
      font-family: 'Rajdhani', sans-serif;
      color: #CFFAFE;
      font-size: 12pt;
      margin-top: 32pt;
    }}
    
    /* Tables */
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 12pt 0;
    }}
    th {{
      background: #059669;
      color: white;
      font-family: 'Lato', sans-serif;
      font-weight: 700;
      padding: 8pt;
      border: 1pt solid #047857;
      text-align: center;
    }}
    td {{
      padding: 6pt 8pt;
      border: 0.5pt solid #E5E7EB;
      font-size: 10pt;
    }}
    tbody tr:nth-child(even) td {{
      background: #F8FAFC;
    }}
    
    /* Callouts */
    .callout {{
      padding: 10pt 14pt;
      margin: 12pt 0;
      border-left: 4pt solid;
      background: #F8FAFC;
      font-size: 10pt;
    }}
    .callout.info {{ border-color: #22D3EE; background: #CFFAFE; color: #0E7490; }}
    .callout.success {{ border-color: #10B981; background: #D1FAE5; color: #047857; }}
    .callout.warning {{ border-color: #F59E0B; background: #FEF3C7; color: #92400E; }}
    
    .stat {{
      font-family: 'Orbitron', sans-serif;
      font-weight: 700;
      color: #047857;
    }}
  </style>
</head>
<body>

  <!-- COVER -->
  <div class="cover">
    <img src="{logo_path}" alt="gilman.pro">
    <h1>{title}</h1>
    <h2>{subtitle}</h2>
    <div class="contact">{author} · {contact}</div>
  </div>
  
  <!-- CONTENT -->
  <h1>Resumen Ejecutivo</h1>
  <p>Lorem ipsum...</p>
  
  <h2>Indicadores Clave</h2>
  <div class="separator">
    <div class="line short"></div>
    <div class="dot"></div>
    <div class="line long"></div>
    <div class="dot"></div>
    <div class="line short violet"></div>
  </div>
  
  <table>
    <thead>
      <tr><th>Indicador</th><th>Q4 2025</th><th>Q1 2026</th><th>Δ</th></tr>
    </thead>
    <tbody>
      <tr><td>Unidades</td><td>1,250</td><td>1,720</td><td class="stat">+37.6%</td></tr>
    </tbody>
  </table>
  
  <div class="callout success">
    <strong>Crecimiento sostenido.</strong> El Q1 2026 muestra una mejora del 37.6% sobre el trimestre anterior.
  </div>
  
</body>
</html>
"""

# Convertir a PDF
HTML(string=html_content, base_url=str(SKILL_DIR / "assets")).write_pdf("output.pdf")
```

### Con Playwright (mayor fidelidad, requiere navegador)

```python
from playwright.sync_api import sync_playwright
from pathlib import Path

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f"file://{Path('reporte.html').resolve()}")
    page.pdf(
        path="output.pdf",
        format="A4",
        margin={"top": "25mm", "bottom": "25mm", "left": "20mm", "right": "20mm"},
        print_background=True,
        display_header_footer=True,
        header_template="<div></div>",
        footer_template="""
          <div style="font-size: 9pt; color: #6B7280; width: 100%;
                      padding: 0 20mm; display: flex;
                      justify-content: space-between; font-family: Rajdhani, sans-serif;">
            <span>© 2026 gilman.pro</span>
            <span>Página <span class="pageNumber"></span> / <span class="totalPages"></span></span>
          </div>
        """,
    )
    browser.close()
```

---

## ENFOQUE 2: REPORTLAB (NATIVO)

Mayor control, pero más verboso. Útil cuando no se puede usar un navegador.

```python
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pathlib import Path

# ===== REGISTRAR FUENTES GILMAN =====
# Descargar de Google Fonts y apuntar a la ruta
FONTS_DIR = Path("C:/Windows/Fonts")  # o ruta de fuentes descargadas
try:
    pdfmetrics.registerFont(TTFont("Montserrat", str(FONTS_DIR / "Montserrat-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("Montserrat-Bold", str(FONTS_DIR / "Montserrat-Bold.ttf")))
    pdfmetrics.registerFont(TTFont("Lato", str(FONTS_DIR / "Lato-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("Lato-Bold", str(FONTS_DIR / "Lato-Bold.ttf")))
    pdfmetrics.registerFont(TTFont("Rajdhani", str(FONTS_DIR / "Rajdhani-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("Rajdhani-Bold", str(FONTS_DIR / "Rajdhani-Bold.ttf")))
    pdfmetrics.registerFont(TTFont("Orbitron", str(FONTS_DIR / "Orbitron-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("Orbitron-Bold", str(FONTS_DIR / "Orbitron-Bold.ttf")))
    HAS_CUSTOM_FONTS = True
except Exception:
    HAS_CUSTOM_FONTS = False
    # Fallback a Helvetica
    pdfmetrics.registerFont(TTFont("Montserrat", "Helvetica"))
    pdfmetrics.registerFont(TTFont("Montserrat-Bold", "Helvetica-Bold"))

# ===== PALETA =====
EMERALD_500 = HexColor("#10B981")
EMERALD_600 = HexColor("#059669")
EMERALD_700 = HexColor("#047857")
VIOLET_500  = HexColor("#8B5CF6")
CYAN_400    = HexColor("#22D3EE")
SLATE_800   = HexColor("#1E293B")
SLATE_50    = HexColor("#F8FAFC")
GRAY_900    = HexColor("#111827")
GRAY_500    = HexColor("#6B7280")
GRAY_200    = HexColor("#E5E7EB")

# ===== ESTILOS =====
def get_gilman_styles():
    styles = getSampleStyleSheet()
    
    heading_font = "Montserrat-Bold" if HAS_CUSTOM_FONTS else "Helvetica-Bold"
    body_font    = "Lato" if HAS_CUSTOM_FONTS else "Helvetica"
    tech_font    = "Rajdhani" if HAS_CUSTOM_FONTS else "Helvetica"
    
    # H1 con barra lateral
    styles.add(ParagraphStyle(
        name="GilmanH1",
        fontName=heading_font,
        fontSize=22,
        leading=26,
        textColor=EMERALD_700,
        spaceBefore=18,
        spaceAfter=10,
        leftIndent=12,
        borderPadding=4,
        borderColor=EMERALD_500,
        borderWidth=0,  # 0 = sin borde nativo
    ))
    
    # H2
    styles.add(ParagraphStyle(
        name="GilmanH2",
        fontName=heading_font,
        fontSize=16,
        leading=20,
        textColor=GRAY_900,
        spaceBefore=14,
        spaceAfter=6,
    ))
    
    # H3
    styles.add(ParagraphStyle(
        name="GilmanH3",
        fontName=heading_font,
        fontSize=12,
        leading=16,
        textColor=EMERALD_600,
        spaceBefore=10,
        spaceAfter=4,
    ))
    
    # Body
    styles.add(ParagraphStyle(
        name="GilmanBody",
        fontName=body_font,
        fontSize=10,
        leading=14,
        textColor=GRAY_900,
        alignment=TA_JUSTIFY,
        spaceAfter=6,
    ))
    
    # Caption
    styles.add(ParagraphStyle(
        name="GilmanCaption",
        fontName=body_font,
        fontSize=8,
        leading=10,
        textColor=GRAY_500,
        alignment=TA_CENTER,
    ))
    
    return styles
```

### Portada con ReportLab

```python
def cover_page_callback(canvas_obj, doc):
    """Callback para dibujar la portada en page 1."""
    canvas_obj.saveState()
    
    # Fondo emerald
    canvas_obj.setFillColor(EMERALD_500)
    canvas_obj.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    
    # Logo (centrado)
    logo_path = SKILL_DIR / "assets" / "logo_gilmanpro.png"
    if logo_path.exists():
        canvas_obj.drawImage(
            str(logo_path),
            x=A4[0]/2 - 100, y=A4[1] - 250,
            width=200, height=80,
            preserveAspectRatio=True, mask='auto'
        )
    
    # Título
    canvas_obj.setFillColor(white)
    canvas_obj.setFont("Montserrat-Bold" if HAS_CUSTOM_FONTS else "Helvetica-Bold", 36)
    canvas_obj.drawCentredString(A4[0]/2, A4[1] - 360, "Gilberto Castillo")
    
    # Subtítulo
    canvas_obj.setFont("Lato" if HAS_CUSTOM_FONTS else "Helvetica", 14)
    canvas_obj.setFillColor(HexColor("#CFFAFE"))
    canvas_obj.drawCentredString(A4[0]/2, A4[1] - 400, "Ingeniero en Telecomunicaciones | Especialista en Big Data y Data Science")
    
    # Línea separadora
    canvas_obj.setStrokeColor(HexColor("#FFFFFF"))
    canvas_obj.setLineWidth(1.5)
    canvas_obj.line(A4[0]/2 - 80, A4[1] - 430, A4[0]/2 + 80, A4[1] - 430)
    
    # Contacto
    canvas_obj.setFont("Rajdhani" if HAS_CUSTOM_FONTS else "Helvetica", 11)
    canvas_obj.setFillColor(CYAN_400)
    canvas_obj.drawCentredString(A4[0]/2, 80, "contacto@gilman.pro")
    
    canvas_obj.restoreState()


def make_cover_page():
    """Hoja completa con fondo."""
    from reportlab.platypus import Spacer
    return [Spacer(1, 1)]  # placeholder; el fondo se dibuja en el callback
```

### Función de header/footer con ReportLab

```python
def header_footer_callback(canvas_obj, doc):
    """Header y footer para páginas NO portada."""
    canvas_obj.saveState()
    
    page_w, page_h = A4
    
    # Header: "gilman.pro" en Rajdhani
    canvas_obj.setFont("Rajdhani-Bold" if HAS_CUSTOM_FONTS else "Helvetica-Bold", 9)
    canvas_obj.setFillColor(EMERALD_600)
    canvas_obj.drawRightString(page_w - 2*cm, page_h - 1.5*cm, "gilman.pro")
    
    # Línea inferior header
    canvas_obj.setStrokeColor(EMERALD_500)
    canvas_obj.setLineWidth(0.5)
    canvas_obj.line(2*cm, page_h - 1.7*cm, page_w - 2*cm, page_h - 1.7*cm)
    
    # Footer izquierda: copyright
    canvas_obj.setFont("Rajdhani" if HAS_CUSTOM_FONTS else "Helvetica", 8)
    canvas_obj.setFillColor(GRAY_500)
    canvas_obj.drawString(2*cm, 1.2*cm, "© 2026 Gilberto Castillo — Ing. Telecomunicaciones | Big Data y Data Science | gilman.pro")
    
    # Footer derecha: número de página
    canvas_obj.drawRightString(page_w - 2*cm, 1.2*cm, f"Página {doc.page}")
    
    canvas_obj.restoreState()
```

### Generar PDF completo

```python
def generate_gilman_pdf(output_path, title, subtitle, author, contact, content_blocks):
    """
    content_blocks: lista de dicts con keys:
        - type: 'h1' | 'h2' | 'h3' | 'p' | 'table' | 'callout' | 'separator' | 'spacer' | 'image'
        - text, items, headers, rows, kind, src, etc.
    """
    styles = get_gilman_styles()
    
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        topMargin=2.5*cm, bottomMargin=2.5*cm,
        leftMargin=2*cm, rightMargin=2*cm,
        title=title,
        author=author,
    )
    
    story = []
    
    for block in content_blocks:
        btype = block.get("type")
        if btype == "h1":
            # H1 con barra lateral usando tabla
            from reportlab.platypus import Table
            h1_table = Table(
                [[Paragraph(f'<font color="#047857">{block["text"]}</font>', styles["GilmanH1"])]],
                colWidths=[A4[0] - 4*cm]
            )
            h1_table.setStyle(TableStyle([
                ("LINEBEFORE", (0, 0), (0, 0), 3, EMERALD_500),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]))
            story.append(h1_table)
        elif btype == "h2":
            story.append(Paragraph(block["text"], styles["GilmanH2"]))
            # Separador signature
            story.append(_signature_separator())
        elif btype == "h3":
            story.append(Paragraph(block["text"], styles["GilmanH3"]))
        elif btype == "p":
            story.append(Paragraph(block["text"], styles["GilmanBody"]))
        elif btype == "spacer":
            story.append(Spacer(1, block.get("height", 0.5*cm)))
        elif btype == "separator":
            story.append(_signature_separator())
        elif btype == "table":
            story.append(_branded_table(block["headers"], block["rows"]))
        elif btype == "callout":
            story.append(_callout(block["text"], block.get("kind", "info")))
        elif btype == "image":
            story.append(Image(block["src"], width=block.get("width", 12*cm), height=block.get("height", 8*cm)))
        elif btype == "pagebreak":
            story.append(PageBreak())
    
    # Construir con páginas: portada con fondo, resto con header/footer
    doc.build(
        story,
        onFirstPage=cover_page_callback,
        onLaterPages=header_footer_callback
    )


def _signature_separator():
    """Tabla invisible con líneas y dots del separador signature."""
    line = HRFlowable(width="60%", thickness=1.5, color=EMERALD_500,
                       spaceBefore=2, spaceAfter=8, hAlign="LEFT")
    # Para más fidelidad, usar Table con celdas pintadas
    t = Table(
        [["" for _ in range(7)]],
        colWidths=[1.2*cm, 0.2*cm, 2*cm, 0.2*cm, 1.2*cm, 0.2*cm, 0.5*cm]
    )
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), EMERALD_500),
        ("BACKGROUND", (2, 0), (2, 0), EMERALD_500),
        ("BACKGROUND", (4, 0), (4, 0), VIOLET_500),
        ("BACKGROUND", (6, 0), (6, 0), VIOLET_500),
        ("LINEABOVE", (0, 0), (-1, -1), 0, white),
        ("LINEBELOW", (0, 0), (-1, -1), 0, white),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return t


def _branded_table(headers, rows):
    data = [headers] + [[str(c) for c in r] for r in rows]
    t = Table(data, repeatRows=1)
    t.setStyle(TableStyle([
        # Header
        ("BACKGROUND", (0, 0), (-1, 0), EMERALD_600),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("FONTNAME", (0, 0), (-1, 0), "Lato" if HAS_CUSTOM_FONTS else "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, 0), 10),
        ("FONTWEIGHT", (0, 0), (-1, 0), "BOLD"),
        ("ALIGN", (0, 0), (-1, 0), "CENTER"),
        ("VALIGN", (0, 0), (-1, 0), "MIDDLE"),
        # Body
        ("FONTNAME", (0, 1), (-1, -1), "Lato" if HAS_CUSTOM_FONTS else "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), 9),
        ("TEXTCOLOR", (0, 1), (-1, -1), GRAY_900),
        ("ALIGN", (0, 1), (-1, -1), "LEFT"),
        ("VALIGN", (0, 1), (-1, -1), "MIDDLE"),
        # Zebra
        ("BACKGROUND", (0, 1), (-1, -1), white),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, SLATE_50]),
        # Borders
        ("BOX", (0, 0), (-1, -1), 0.5, GRAY_200),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, GRAY_200),
        ("TOPPADDING", (0, 1), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 6),
    ]))
    return t


def _callout(text, kind="info"):
    colors = {
        "info":    (HexColor("#CFFAFE"), HexColor("#0E7490"), CYAN_400),
        "success": (HexColor("#D1FAE5"), HexColor("#047857"), EMERALD_500),
        "warning": (HexColor("#FEF3C7"), HexColor("#92400E"), HexColor("#F59E0B")),
    }
    bg, txt, bar = colors.get(kind, colors["info"])
    t = Table([[Paragraph(text, ParagraphStyle("c", fontName="Lato" if HAS_CUSTOM_FONTS else "Helvetica", fontSize=10, textColor=txt))]])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LINEBEFORE", (0, 0), (0, 0), 3, bar),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return t
```

## USO

```python
generate_gilman_pdf(
    "informe-gilmanpro.pdf",
    title="Informe Técnico",
    subtitle="Análisis Q1 2026",
    author="Gilberto Castillo — Ingeniero en Telecomunicaciones | Especialista en Big Data y Data Science",
    contact="contacto@gilman.pro",
    content_blocks=[
        {"type": "h1", "text": "Resumen Ejecutivo"},
        {"type": "p", "text": "Este informe presenta el análisis..."},
        {"type": "h2", "text": "Indicadores Clave"},
        {"type": "table", "headers": ["Indicador", "Q1"], "rows": [["Unidades", "1,720"], ["SLA", "95.7%"]]},
        {"type": "callout", "text": "Crecimiento del 37.6% sobre Q4.", "kind": "success"},
    ]
)
```

## REGLAS

1. **Tipografía:** registrar Montserrat, Lato, Rajdhani, Orbitron. Si no están, usar Helvetica.
2. **HTML→PDF es preferido** sobre ReportLab para mayor fidelidad.
3. **Portada con fondo** mediante `onFirstPage` callback.
4. **Header/footer** en `onLaterPages`.
5. **H1 con barra lateral** usando tabla con `LINEBEFORE`.
6. **H2 con separador signature** usando tabla con celdas pintadas.
7. **Tablas** con header emerald-600 + body zebra white/slate-50.
8. **Colores exactos** de la paleta, sin inventar HEX.
9. **Tamaño A4** (default) o Letter si el destino es USA.
10. **Márgenes:** 2-2.5 cm.

## ERRORES COMUNES

- ❌ Olvidar registrar fuentes → aparece en Courier
- ❌ `setFillColor(HexColor("#10B981"))` — usar `HexColor` siempre, no tupla
- ❌ `drawCentredString` con coordenadas invertidas (y) → texto aparece fuera
- ❌ `onFirstPage` y `onLaterPages` no se pasan a `doc.build()` → no se aplican
- ❌ `HRFlowable` con thickness > 5 → se ve pixelado
- ❌ Usar imágenes sin `mask='auto'` → fondo blanco visible alrededor
