# Aplicación a Word (.docx) — gilman.pro

Cómo aplicar el branding gilman.pro a documentos Word usando `python-docx`.

## 1. CONFIGURACIÓN INICIAL

```python
from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn, nsmap
from docx.oxml import OxmlElement

# ===== PALETA GILMAN =====
PRIMARY       = RGBColor(0x10, 0xB9, 0x81)  # Emerald 500
PRIMARY_600   = RGBColor(0x05, 0x96, 0x69)  # Emerald 600
PRIMARY_700   = RGBColor(0x04, 0x78, 0x57)  # Emerald 700
PRIMARY_50    = RGBColor(0xEC, 0xFD, 0xF5)  # Emerald 50
SECONDARY     = RGBColor(0x25, 0x63, 0xEB)  # Blue 600
ACCENT        = RGBColor(0x22, 0xD3, 0xEE)  # Cyan 400
NAVBAR        = RGBColor(0x1E, 0x29, 0x3B)  # Slate 800
WHITE         = RGBColor(0xFF, 0xFF, 0xFF)
SLATE_50      = RGBColor(0xF8, 0xFA, 0xFC)
GRAY_900      = RGBColor(0x11, 0x18, 0x27)
GRAY_700      = RGBColor(0x37, 0x41, 0x51)
GRAY_500      = RGBColor(0x6B, 0x72, 0x80)
GRAY_400      = RGBColor(0x9C, 0xA3, 0xAF)
GRAY_200      = RGBColor(0xE5, 0xE7, 0xEB)
GRAY_100      = RGBColor(0xF3, 0xF4, 0xF6)

# ===== TIPOGRAFÍA =====
FONT_HEADING = "Montserrat"
FONT_BODY    = "Lato"
FONT_TECH    = "Rajdhani"
```

## 2. ESTILOS PERSONALIZADOS (CREAR EN EL DOC)

```python
def setup_styles(doc):
    """Configura estilos del documento con branding gilman."""
    styles = doc.styles
    
    # === NORMAL (body) ===
    normal = styles["Normal"]
    normal.font.name = FONT_BODY
    normal.font.size = Pt(11)
    normal.font.color.rgb = GRAY_900
    normal.paragraph_format.line_spacing = 1.5
    normal.paragraph_format.space_after = Pt(8)
    
    # === HEADINGS ===
    
    # H1
    h1 = styles["Heading 1"]
    h1.font.name = FONT_HEADING
    h1.font.size = Pt(28)
    h1.font.bold = True
    h1.font.color.rgb = PRIMARY_700
    h1.paragraph_format.space_before = Pt(20)
    h1.paragraph_format.space_after = Pt(8)
    h1.paragraph_format.keep_with_next = True
    
    # H2
    h2 = styles["Heading 2"]
    h2.font.name = FONT_HEADING
    h2.font.size = Pt(20)
    h2.font.bold = True
    h2.font.color.rgb = GRAY_900
    h2.paragraph_format.space_before = Pt(16)
    h2.paragraph_format.space_after = Pt(6)
    h2.paragraph_format.keep_with_next = True
    
    # H3
    h3 = styles["Heading 3"]
    h3.font.name = FONT_HEADING
    h3.font.size = Pt(14)
    h3.font.bold = True
    h3.font.color.rgb = PRIMARY_600
    h3.paragraph_format.space_before = Pt(12)
    h3.paragraph_format.space_after = Pt(4)
    h3.paragraph_format.keep_with_next = True
    
    # H4
    h4 = styles["Heading 4"]
    h4.font.name = FONT_HEADING
    h4.font.size = Pt(12)
    h4.font.bold = True
    h4.font.color.rgb = GRAY_700
    h4.paragraph_format.space_before = Pt(8)
    h4.paragraph_format.space_after = Pt(2)
    
    # === BLOCKQUOTE ===
    try:
        bq = styles["Quote"]
    except KeyError:
        from docx.enum.style import WD_STYLE_TYPE
        bq = styles.add_style("Quote", WD_STYLE_TYPE.PARAGRAPH)
    bq.font.name = FONT_BODY
    bq.font.size = Pt(11)
    bq.font.italic = True
    bq.font.color.rgb = GRAY_500
    
    # === CÓDIGO ===
    try:
        code = styles["Code"]
    except KeyError:
        from docx.enum.style import WD_STYLE_TYPE
        code = styles.add_style("Code", WD_STYLE_TYPE.CHARACTER)
    code.font.name = "Consolas"
    code.font.size = Pt(10)
    code.font.color.rgb = PRIMARY_700
```

## 3. BARRA LATERAL DE COLOR EN HEADINGS (signature)

```python
def _add_paragraph_shading(paragraph, hex_color):
    """Aplica shading (fondo de color) a un párrafo."""
    pPr = paragraph._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_color)
    pPr.append(shd)


def _add_paragraph_border(paragraph, side, color, size=24, space=8):
    """Agrega borde lateral (left/right/top/bottom) a un párrafo."""
    pPr = paragraph._p.get_or_add_pPr()
    pBdr = pPr.find(qn("w:pBdr"))
    if pBdr is None:
        pBdr = OxmlElement("w:pBdr")
        pPr.append(pBdr)
    
    border = OxmlElement(f"w:{side}")
    border.set(qn("w:val"), "single")
    border.set(qn("w:sz"), str(size))  # en 1/8 pt; 24 = 3pt
    border.set(qn("w:space"), str(space))
    border.set(qn("w:color"), color)
    pBdr.append(border)


def add_h1_with_bar(doc, text):
    """H1 con barra lateral emerald 4pt (signature del branding)."""
    p = doc.add_paragraph()
    p.style = doc.styles["Heading 1"]
    p.add_run(text)
    _add_paragraph_border(p, "left", "10B981", size=32, space=12)
    return p


def add_h2_with_separator(doc, text):
    """H2 + separador signature: línea + dot + línea + dot (violet) + línea."""
    p = doc.add_paragraph()
    p.style = doc.styles["Heading 2"]
    p.add_run(text)
    
    # Tabla invisible para el separador signature
    table = doc.add_table(rows=1, cols=9)
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    # Anchos: line(2) - gap(1) - dot(1) - gap(1) - line(3) - gap(1) - dot(1) - gap(1) - line(2)
    widths_in = [0.2, 0.1, 0.1, 0.1, 0.4, 0.1, 0.1, 0.1, 0.2]
    for i, w in enumerate(widths_in):
        table.columns[i].width = Inches(w)
    # Celdas pintadas
    cells = table.rows[0].cells
    paint_indices_emerald = [0, 2, 4]
    paint_indices_violet = [6, 8]
    for idx in paint_indices_emerald:
        _set_cell_shading(cells[idx], "10B981")
    for idx in paint_indices_violet:
        _set_cell_shading(cells[idx], "8B5CF6")
    # Altura mínima
    table.rows[0].height = Pt(4)
    
    return p, table


def _set_cell_shading(cell, hex_color):
    """Aplica color de fondo a una celda."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_color)
    tcPr.append(shd)
```

## 4. PORTADA / PRIMERA PÁGINA

```python
def add_cover_page(doc, title, subtitle, author="", contact=""):
    """Página completa emerald con logo, título, subtítulo y autor."""
    # Fondo emerald en toda la página: se logra con un textbox de fondo
    # o configurando el fondo en secciones
    
    # Sección: fondo emerald
    section = doc.sections[0]
    
    # Logo (insertar imagen)
    from pathlib import Path
    logo = Path(__file__).parent / "assets" / "logo_gilmanpro.png"
    if logo.exists():
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(120)
        run = p.add_run()
        run.add_picture(str(logo), width=Inches(2.0))
    
    # Espaciado
    for _ in range(3):
        doc.add_paragraph()
    
    # Título
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(title)
    run.font.name = FONT_HEADING
    run.font.size = Pt(40)
    run.font.bold = True
    run.font.color.rgb = WHITE
    
    # Subtítulo
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(subtitle)
    run.font.name = FONT_BODY
    run.font.size = Pt(18)
    run.font.color.rgb = WHITE
    run.font.transparency = 0.10  # NO soportado en docx real, se ignora
    
    # Autor
    if author:
        for _ in range(2):
            doc.add_paragraph()
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(author)
        run.font.name = FONT_TECH
        run.font.size = Pt(16)
        run.font.color.rgb = ACCENT
        run.font.bold = True
    
    # Contacto
    if contact:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(contact)
        run.font.name = FONT_TECH
        run.font.size = Pt(11)
        run.font.color.rgb = ACCENT
    
    # Salto de página
    doc.add_page_break()
```

## 5. TABLAS CON BRANDING

```python
def add_branded_table(doc, headers, rows, header_fill="059669"):
    """Tabla con header emerald, body zebra, bordes gray-200."""
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    # Header
    header_cells = table.rows[0].cells
    for i, h in enumerate(headers):
        cell = header_cells[i]
        cell.text = ""
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h)
        run.font.name = FONT_BODY
        run.font.size = Pt(10)
        run.font.bold = True
        run.font.color.rgb = WHITE
        _set_cell_shading(cell, header_fill)
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    
    # Body zebra
    for i, row in enumerate(rows):
        row_cells = table.rows[i + 1].cells
        fill = "FFFFFF" if i % 2 == 0 else "F8FAFC"
        for j, val in enumerate(row):
            cell = row_cells[j]
            cell.text = ""
            p = cell.paragraphs[0]
            run = p.add_run(str(val))
            run.font.name = FONT_BODY
            run.font.size = Pt(10)
            run.font.color.rgb = GRAY_900
            _set_cell_shading(cell, fill)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    
    return table
```

## 6. CALLOUT / CAJA DE COLOR

```python
def add_callout(doc, text, kind="info"):
    """
    Inserta un párrafo con fondo de color y borde lateral.
    kind: 'info' (cyan), 'success' (emerald), 'warning' (yellow), 'error' (red).
    """
    colors = {
        "info":    ("CFFAFE", "0E7490", "22D3EE"),  # bg / text / bar
        "success": ("D1FAE5", "047857", "10B981"),
        "warning": ("FEF3C7", "92400E", "F59E0B"),
        "error":   ("FEE2E2", "991B1B", "EF4444"),
    }
    bg_hex, text_hex, bar_hex = colors[kind]
    
    # Crear tabla 1x1 con el formato
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.autofit = False
    table.columns[0].width = Inches(6.5)
    cell = table.rows[0].cells[0]
    cell.width = Inches(6.5)
    _set_cell_shading(cell, bg_hex)
    _add_cell_left_border(cell, bar_hex, size=24, space=8)
    
    p = cell.paragraphs[0]
    p.paragraph_format.left_indent = Inches(0.1)
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text)
    run.font.name = FONT_BODY
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor.from_string(text_hex)
    
    return table


def _add_cell_left_border(cell, color, size=24, space=8):
    """Borde lateral izquierdo en una celda."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = OxmlElement("w:tcBorders")
    border = OxmlElement("w:left")
    border.set(qn("w:val"), "single")
    border.set(qn("w:sz"), str(size))
    border.set(qn("w:color"), color)
    tcBorders.append(border)
    tcPr.append(tcBorders)
```

## 7. HEADER Y FOOTER

```python
def setup_header_footer(doc, footer_text="© 2026 Gilberto Castillo — Ing. Telecomunicaciones | Big Data y Data Science | Desarrollador de Soluciones"):
    """Header con logo pequeño + tagline, footer con copyright y página."""
    section = doc.sections[0]
    
    # Header
    header = section.header
    h_p = header.paragraphs[0]
    h_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = h_p.add_run("gilman.pro")
    run.font.name = FONT_TECH
    run.font.size = Pt(10)
    run.font.bold = True
    run.font.color.rgb = PRIMARY_600
    # Borde inferior en header
    _add_paragraph_border(h_p, "bottom", "10B981", size=6, space=4)
    
    # Footer
    footer = section.footer
    f_p = footer.paragraphs[0]
    f_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    # Tabla 1x2 para dividir izquierda/derecha
    f_table = footer.add_table(rows=1, cols=2, width=Inches(6.5))
    f_table.autofit = True
    
    # Izquierda: copyright
    left_cell = f_table.rows[0].cells[0]
    left_cell.text = ""
    p = left_cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run = p.add_run(footer_text)
    run.font.name = FONT_TECH
    run.font.size = Pt(8)
    run.font.color.rgb = GRAY_500
    
    # Derecha: número de página
    right_cell = f_table.rows[0].cells[1]
    right_cell.text = ""
    p = right_cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = p.add_run("Página ")
    run.font.name = FONT_TECH
    run.font.size = Pt(8)
    run.font.color.rgb = GRAY_500
    # Campo PAGE
    fld_run = p.add_run()
    fldChar1 = OxmlElement("w:fldChar")
    fldChar1.set(qn("w:fldCharType"), "begin")
    instrText = OxmlElement("w:instrText")
    instrText.set(qn("xml:space"), "preserve")
    instrText.text = "PAGE"
    fldChar2 = OxmlElement("w:fldChar")
    fldChar2.set(qn("w:fldCharType"), "end")
    fld_run._r.append(fldChar1)
    fld_run._r.append(instrText)
    fld_run._r.append(fldChar2)
    fld_run.font.name = FONT_TECH
    fld_run.font.size = Pt(8)
    fld_run.font.color.rgb = GRAY_500
```

## 8. USO COMPLETO

```python
doc = Document()
setup_styles(doc)
setup_header_footer(doc, "© 2026 Gilberto Castillo — Ing. Telecomunicaciones | Big Data y Data Science | Desarrollador de Soluciones")

# Configurar márgenes
section = doc.sections[0]
section.top_margin = Cm(2.5)
section.bottom_margin = Cm(2.5)
section.left_margin = Cm(2.5)
section.right_margin = Cm(2.5)

# Portada
add_cover_page(
    doc,
    title="Informe Técnico",
    subtitle="Análisis de Datos — Q1 2026",
    author="Gilberto Castillo — Ingeniero en Telecomunicaciones | Especialista en Big Data y Data Science",
    contact="contacto@gilman.pro"
)

# Contenido
add_h1_with_bar(doc, "Resumen Ejecutivo")
doc.add_paragraph(
    "Este informe presenta el análisis de los indicadores clave del primer trimestre. "
    "Los datos provienen de la integración de tres fuentes operativas..."
)

add_h2_with_separator(doc, "Indicadores Principales")
add_branded_table(
    doc,
    headers=["Indicador", "Ene", "Feb", "Mar", "Total"],
    rows=[
        ["Unidades procesadas", "1,250", "1,480", "1,720", "4,450"],
        ["Tickets cerrados", "85", "92", "78", "255"],
        ["SLA cumplido (%)", "94%", "96%", "97%", "95.7%"],
    ]
)

add_callout(
    doc,
    "El SLA trimestral fue del 95.7%, 0.7 puntos por encima del objetivo. "
    "Destaca la mejora sostenida en marzo.",
    kind="success"
)

add_h2_with_separator(doc, "Conclusiones")
doc.add_paragraph(
    "Los resultados del trimestre superan las expectativas. Se recomienda mantener "
    "la estrategia actual y reforzar el equipo de soporte para Q2."
)

doc.save("informe-gilmanpro.docx")
```

## 9. REGLAS

1. **Tipografía:** Montserrat, Lato, Rajdhani. Si no están, Calibri.
2. **H1 con barra lateral emerald 4pt** (signature).
3. **H2 con separador signature** debajo.
4. **Tablas:** header emerald-600 con texto blanco, body zebra (white/slate-50).
5. **Callouts:** fondo de color claro + barra lateral del color más fuerte.
6. **Header:** "gilman.pro" en Rajdhani 700 + borde inferior emerald 0.75pt.
7. **Footer:** copyright a la izquierda + número de página a la derecha.
8. **Portada:** fondo emerald + texto blanco + logo centrado.
9. **Márgenes:** 2.5cm en todos los lados.
10. **Tamaño de papel:** A4 o Letter según el destino.

## 10. ERRORES COMUNES

- ❌ Olvidar `qn("w:val")` en elementos OxmlElement → no se aplica el shading
- ❌ `RGBColor.from_string("FFFFFF")` con `#` → falla
- ❌ `_set_cell_shading` antes de añadir texto → texto se reemplaza con shading solo
- ❌ `add_picture` con width muy grande → distorsiona
- ❌ Headers/footers solo se aplican a la sección actual; si hay múltiples secciones, repetir
- ❌ `WD_ALIGN_VERTICAL.CENTER` con `cell.text = "..."` reemplaza el formato previo
- ❌ Usar `font.transparency` → NO soportado en docx, se ignora silenciosamente
