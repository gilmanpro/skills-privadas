# Guía: Aplicar Diseño MiBus a Word (.docx)

> Cómo crear documentos Word con la identidad visual de MiBus: cartas, memorandos, informes, oficios, etc.

## 📋 Antes de empezar

1. Lee `assets/brand-mibus.json` y `assets/colors-mibus.md` de esta skill.
2. Descarga el logo a `WORKDIR/ASSETS/logo.png`.
3. **Carga la skill `docx`** del sistema opencode y sigue su flujo de trabajo.
4. Combina: identidad MiBus (esta skill) + buenas prácticas DOCX (skill `docx`).

## 🎨 Aplicación por tipo de documento

### 1. Carta formal / Oficio

**Estructura recomendada:**

```
┌──────────────────────────────────────────┐
│ [LOGO MiBus - 3cm]    MiBus             │ ← Encabezado con logo
│                       Transporte Masivo  │
│                       de Panamá         │
├──────────────────────────────────────────┤
│                                          │
│  Panamá, [FECHA]                         │
│                                          │
│  Asunto: [TÍTULO]                        │
│  ───── (línea primary 2px)              │
│                                          │
│  Estimado/a [NOMBRE]:                    │
│                                          │
│  Cuerpo del documento en Roboto 11pt...  │
│                                          │
│  Atentamente,                            │
│                                          │
│  [FIRMA]                                 │
│  Nombre                                  │
│  Cargo                                   │
│                                          │
├──────────────────────────────────────────┤
│ [Footer: #1A1A2E]                        │
│ www.mibus.com.pa · contacto@mibus.com.pa │
└──────────────────────────────────────────┘
```

### 2. Informe corporativo

**Estructura recomendada:**

- **Portada:** background `#283c90` con logo blanco + título grande
- **Página 2:** Tabla de contenidos
- **Cuerpo:** Secciones con headers primary y divisores
- **Apéndices:** Tablas y figuras con caption MiBus

### 3. Memorando interno

**Estructura recomendada:**

```
┌──────────────────────────────────────────┐
│ [LOGO]    MEMORÁNDUM INTERNO             │ ← Header
│           #2026-001                      │
├──────────────────────────────────────────┤
│ PARA:    [Nombre]                        │
│ DE:      [Nombre]                        │
│ FECHA:   [Fecha]                         │
│ ASUNTO:  [Asunto]                        │
│ ─────                                   │
│                                          │
│ [Cuerpo...]                              │
│                                          │
└──────────────────────────────────────────┘
```

## 🔤 Tipografía para Word

| Elemento | Fuente | Tamaño | Color |
|---|---|---|---|
| Título portada | Poppins Bold | 36-48pt | `#FFFFFF` sobre `#283c90` |
| H1 sección | Poppins Bold | 18-20pt | `#283c90` |
| H2 subsección | Poppins Semibold | 14-16pt | `#283c90` |
| H3 sub-sub | Poppins Semibold | 12-13pt | `#205CA7` |
| Body | Roboto Regular | 11pt | `#333333` |
| Énfasis | Roboto Medium | 11pt | `#333333` |
| Caption | Roboto Regular | 9pt | `#666666` |
| Cita | Roboto Italic | 10pt | `#666666` |

**⚠️ Word no carga web fonts automáticamente.** Opciones:

1. **Instalar Poppins y Roboto** en el sistema (recomendado)
   - Word las detectará automáticamente
   - El usuario podrá editarlas sin perder formato
2. **Usar Calibri/Arial** como fallback (más conservador)
3. **Embebir fuentes** en el .docx (solo Word 2016+ con archivo .docx)

## 🛠️ Implementación con python-docx

### Setup básico

```python
from docx import Document
from docx.shared import Pt, Inches, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.oxml.ns import qn, nsmap
from docx.oxml import OxmlElement

doc = Document()

# Colores MiBus
PRIMARY = RGBColor(0x28, 0x3C, 0x90)
PRIMARY_DARK = RGBColor(0x1B, 0x2A, 0x66)
SECONDARY = RGBColor(0x20, 0x5C, 0xA7)
ACCENT = RGBColor(0x1D, 0xA1, 0xF2)
DARK = RGBColor(0x1A, 0x1A, 0x2E)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
TEXT = RGBColor(0x33, 0x33, 0x33)
BORDER = RGBColor(0xE0, 0xE0, 0xE0)
```

### Función helper para aplicar formato

```python
def set_run_format(run, font_name="Roboto", size=11, bold=False, italic=False, color=None):
    """Aplica formato MiBus a un run."""
    run.font.name = font_name
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    if color:
        run.font.color.rgb = color
    # Forzar East Asian font
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = OxmlElement('w:rFonts')
        rPr.append(rFonts)
    rFonts.set(qn('w:ascii'), font_name)
    rFonts.set(qn('w:hAnsi'), font_name)
    rFonts.set(qn('w:cs'), font_name)
    rFonts.set(qn('w:eastAsia'), font_name)


def add_styled_paragraph(doc, text, font_name="Roboto", size=11, bold=False, color=TEXT, align=None, space_after=6):
    """Añade párrafo con estilo MiBus."""
    p = doc.add_paragraph()
    if align:
        p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    run = p.add_run(text)
    set_run_format(run, font_name, size, bold, color=color)
    return p
```

### Header con logo

```python
def add_mibus_header(doc, logo_path="ASSETS/logo.png", include_text=True):
    """Añade un header con logo MiBus."""
    section = doc.sections[0]
    header = section.header
    
    # Crear tabla 1x2: logo a la izquierda, texto a la derecha
    table = header.add_table(rows=1, cols=2, width=Inches(7))
    table.autofit = False
    
    # Celda logo
    cell_logo = table.cell(0, 0)
    cell_logo.width = Inches(2.5)
    p = cell_logo.paragraphs[0]
    run = p.add_run()
    run.add_picture(logo_path, width=Inches(2.2))
    
    # Celda texto
    if include_text:
        cell_text = table.cell(0, 1)
        cell_text.width = Inches(4.5)
        p1 = cell_text.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        run = p1.add_run("MiBus")
        set_run_format(run, "Poppins", 18, True, PRIMARY)
        
        p2 = cell_text.add_paragraph()
        p2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        run = p2.add_run("Transporte Masivo de Panamá")
        set_run_format(run, "Roboto", 9, False, TEXT)
    
    # Borde inferior
    for cell in table.row_cells(0):
        p = cell.paragraphs[0]
        pPr = p._p.get_or_add_pPr()
        pBdr = OxmlElement('w:pBdr')
        bottom = OxmlElement('w:bottom')
        bottom.set(qn('w:val'), 'single')
        bottom.set(qn('w:sz'), '12')  # 1.5pt
        bottom.set(qn('w:color'), '283C90')
        pBdr.append(bottom)
        pPr.append(pBdr)
```

### Footer corporativo

```python
def add_mibus_footer(doc, page_num_text=None):
    """Añade un footer con info de MiBus."""
    section = doc.sections[0]
    footer = section.footer
    
    # Tabla 1x2: texto a la izquierda, página a la derecha
    table = footer.add_table(rows=1, cols=2, width=Inches(7))
    
    cell_left = table.cell(0, 0)
    p = cell_left.paragraphs[0]
    run = p.add_run("MiBus · www.mibus.com.pa · contacto@mibus.com.pa")
    set_run_format(run, "Roboto", 8, False, RGBColor(0x66, 0x66, 0x66))
    
    if page_num_text:
        cell_right = table.cell(0, 1)
        p = cell_right.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        run = p.add_run(page_num_text)
        set_run_format(run, "Roboto", 8, False, RGBColor(0x66, 0x66, 0x66))
```

### Portada con background azul

```python
def add_cover_page(doc, title, subtitle, logo_path="ASSETS/logo.png"):
    """Crea una portada con background primary y logo blanco."""
    # Crear tabla de 1x1 que ocupe toda la página
    table = doc.add_table(rows=2, cols=1)
    table.autofit = False
    
    # Celda 1: Background primary con logo
    cell1 = table.cell(0, 0)
    cell1.width = Inches(7)
    
    # Background color de la celda
    tcPr = cell1._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), '283C90')
    tcPr.append(shd)
    
    # Padding
    for direction in ['top', 'left', 'bottom', 'right']:
        tcMar = OxmlElement(f'w:{direction}')
        tcMar.set(qn('w:w'), '1440')  # 1 inch
        tcMar.set(qn('w:type'), 'dxa')
        tcPr.append(tcMar)
    
    # Logo
    p = cell1.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    run.add_picture(logo_path, width=Inches(3))
    
    # Celda 2: Título grande
    cell2 = table.cell(1, 0)
    p = cell2.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(48)
    run = p.add_run(title)
    set_run_format(run, "Poppins", 36, True, PRIMARY)
    
    p_sub = cell2.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(12)
    run = p_sub.add_run(subtitle)
    set_run_format(run, "Roboto", 18, False, RGBColor(0x66, 0x66, 0x66))
    
    # Page break
    doc.add_page_break()
```

### Tabla con estilo MiBus

```python
def style_mibus_table(table, has_header=True):
    """Aplica estilo MiBus a una tabla de Word."""
    for i, row in enumerate(table.rows):
        for cell in row.cells:
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            
            # Background
            tcPr = cell._tc.get_or_add_tcPr()
            shd = OxmlElement('w:shd')
            shd.set(qn('w:val'), 'clear')
            shd.set(qn('w:color'), 'auto')
            
            if has_header and i == 0:
                shd.set(qn('w:fill'), '283C90')  # Header primary
                for p in cell.paragraphs:
                    for run in p.runs:
                        run.font.color.rgb = WHITE
                        run.font.bold = True
                        run.font.name = "Poppins"
            elif i % 2 == 0:
                shd.set(qn('w:fill'), 'F0F0F0')  # Stripe gris
            else:
                shd.set(qn('w:fill'), 'FFFFFF')  # Blanco
            
            tcPr.append(shd)
            
            # Bordes
            tcBorders = OxmlElement('w:tcBorders')
            for border_name in ['top', 'left', 'bottom', 'right']:
                border = OxmlElement(f'w:{border_name}')
                border.set(qn('w:val'), 'single')
                border.set(qn('w:sz'), '4')
                border.set(qn('w:color'), 'E0E0E0')
                tcBorders.append(border)
            tcPr.append(tcBorders)
```

## ✅ Checklist para DOCX MiBus

- [ ] Logo MiBus en header de TODAS las páginas
- [ ] Footer corporativo con web/email
- [ ] Títulos H1 con color `#283c90` en Poppins
- [ ] Body en Roboto 11pt
- [ ] Tablas con header primary y stripes alternados
- [ ] Portada con background primary (si es informe formal)
- [ ] Sin imágenes de stock genéricas
- [ ] Márgenes: 2.5cm todos los lados (estándar)
- [ ] Numeración de página en footer

## 🚫 Errores comunes

- ❌ Word en Calibri por defecto sin sobrescribir
- ❌ Solo Word y sin imagen/logo
- ❌ Texto justificado en cartas (preferir izquierda)
- ❌ Márgenes mínimos (0.5cm) - usar 2.5cm
- ❌ Tablas sin estilo (bordes gruesos negros)
- ❌ Mezcla de colores saturados
