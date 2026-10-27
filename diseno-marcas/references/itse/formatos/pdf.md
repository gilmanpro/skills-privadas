# Plantilla PDF — ITSE

Guía para crear PDFs con el estilo ITSE usando la skill `pdf` + esta skill.

---

## ⚠️ Regla de carpeta de trabajo (OBLIGATORIA)

```bash
mkdir "%TEMP%\opencode\pdf-YYYYMMDD-HHMMSS"
```

SIEMPRE se ejecuta desde la carpeta temporal global de opencode. NUNCA escribas PDFs en la raíz del proyecto.

### Por qué la carpeta temporal de opencode (no la raíz del proyecto)

1. **No contaminar el workspace:** PDFs generados como `reporte.pdf`, `merged.pdf`, `output.pdf` no deben quedar en la raíz.
2. **No mezclar con archivos del usuario:** si el usuario tiene un PDF llamado igual, lo sobrescribimos.
3. **Limpieza fácil:** al final de la tarea, basta con `rmdir` la carpeta temporal.
4. **Aislamiento:** cada tarea usa su propia carpeta, sin colisiones.
5. **Persistencia ante `git clean` o `git reset`:** la carpeta `Temp\opencode` sobrevive.

---

## 🚨 REGLA CRÍTICA: Logo del ITSE ARRIBA en portadas

> **En TODA portada de PDF, el logo del ITSE va en la parte SUPERIOR de
> la página — NUNCA en el centro vertical, NUNCA debajo del título.**

- **Portada:** Logo horizontal en el TOP (alineado a la izquierda en el header o centrado arriba del título), alto ~1.5–2 cm
- **Páginas interiores:** Logo en el HEADER de la página (aparece en todas las páginas), alineado a la izquierda, alto ~1 cm
- **Footer:** Texto "Instituto Técnico Superior Especializado · itse.ac.pa" + numeración

---

## Especificaciones del PDF

| Parámetro | Valor |
|---|---|
| Tamaño de página | Carta (8.5 × 11 in) o A4 (210 × 297 mm) |
| Resolución | 300 DPI para impresión, 150 DPI para pantalla |
| Tipografía | **Helvetica** o **Arial** (incrustar siempre) |
| Color | CMYK para impresión, RGB para digital |
| Carrera de referencia | **T.S. en Big Data y Ciencia de Datos** (Área de Innovación Digital) |

---

## Opciones para generar PDFs del ITSE

### Opción 1: Generar el PDF desde HTML/WeasyPrint (recomendado)

```python
from weasyprint import HTML

html_content = """
<!DOCTYPE html>
<html>
<head>
  <style>
    @page {
      size: letter;
      margin: 2.5cm;
    }
    body {
      font-family: "Helvetica Neue", Inter, Helvetica, Arial, sans-serif;
      color: #424242;
      font-size: 11pt;
      line-height: 1.5;
    }
    h1 {
      color: #424242;
      font-size: 28pt;
      font-weight: 700;
      border-bottom: 3pt solid #FFB000;
      padding-bottom: 8pt;
    }
    h2 { color: #424242; font-size: 22pt; font-weight: 700; }
    h3 { color: #424242; font-size: 16pt; font-weight: 700; }
    .callout {
      border-left: 4pt solid #FFB000;
      background: #F7F7F7;
      padding: 12pt;
      margin: 12pt 0;
    }
    table { width: 100%; border-collapse: collapse; margin: 12pt 0; }
    th { background: #FFB000; color: white; padding: 8pt; font-weight: 700; }
    td { padding: 8pt; border-bottom: 0.5pt solid #AEAEAE; }
    tr:nth-child(even) td { background: #F7F7F7; }
  </style>
</head>
<body>
  <img src="logo-itse-horizontal.png" style="height: 1cm;">
  <h1>Título del Reporte</h1>
  <p>Contenido del reporte...</p>
  <div class="callout"><strong>Información:</strong> ITSE cuenta con +4.000 estudiantes.</div>
    <table>
      <tr><th>Carrera</th><th>Duración</th><th>Créditos</tr>
      <tr><td>T.S. en Desarrollo de Software</td><td>2a 4m</td><td>112</td></tr>
      <tr><td>T.S. en Big Data y Ciencia de Datos</td><td>2a 4m</td><td>113</td></tr>
    </table>
  </body>
</html>
"""

HTML(string=html_content, base_url=".").write_pdf("reporte-itse.pdf")
```

### Opción 2: Generar el PDF desde DOCX (vía LibreOffice)

```bash
libreoffice --headless --convert-to pdf documento-itse.docx
```

### Opción 3: Generar el PDF desde PPTX (vía LibreOffice)

```bash
libreoffice --headless --convert-to pdf presentacion-itse.pptx
```

### Opción 4: Generar con ReportLab (Python puro)

```python
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.enums import TA_CENTER, TA_LEFT

DORADO = HexColor("#FFB000")
GRIS = HexColor("#424242")
GRIS_CLARO = HexColor("#F7F7F7")
BLANCO = HexColor("#FFFFFF")

doc = SimpleDocTemplate(
    "reporte-itse.pdf",
    pagesize=letter,
    rightMargin=2.5*cm, leftMargin=2.5*cm,
    topMargin=2.5*cm, bottomMargin=2.5*cm
)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="ITSETitle", fontName="Helvetica-Bold",
    fontSize=28, textColor=GRIS, spaceAfter=12, leading=32))
styles.add(ParagraphStyle(name="ITSEBody", fontName="Helvetica",
    fontSize=11, textColor=GRIS, leading=15))

story = []
logo = Image("logo-itse-horizontal.png", width=4*cm, height=1.2*cm)
story.append(logo)
story.append(Spacer(1, 1*cm))
story.append(Paragraph("Reporte ITSE", styles["ITSETitle"]))
story.append(Spacer(1, 0.5*cm))
story.append(Paragraph("Cuerpo del reporte.", styles["ITSEBody"]))
story.append(Spacer(1, 0.3*cm))

data = [
    ["Carrera", "Duración", "Créditos"],
    ["T.S. en Desarrollo de Software", "2a 4m", "112"],
    ["T.S. en Big Data y Ciencia de Datos", "2a 4m", "113"],
    ["T.S. en Ciberseguridad", "2a 4m", "122"],
]
t = Table(data, colWidths=[8*cm, 4*cm, 3*cm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), DORADO),
    ("TEXTCOLOR", (0,0), (-1,0), BLANCO),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,-1), 11),
    ("TEXTCOLOR", (0,1), (-1,-1), GRIS),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("LINEBELOW", (0,0), (-1,0), 1.5, DORADO),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [BLANCO, GRIS_CLARO]),
    ("LINEBELOW", (0,1), (-1,-1), 0.5, HexColor("#AEAEAE")),
    ("TOPPADDING", (0,0), (-1,-1), 8),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
]))
story.append(t)
doc.build(story)
```

---

## Portada de PDF

**El logo SIEMPRE va ARRIBA en la portada del PDF:**

```
┌────────────────────────────────────┐
│  [LOGO ITSE]   1.5-2cm de ancho    │  ← LOGO ARRIBA (header, alto 1.5-2cm)
│  ────────────────────────          │  ← línea 3pt #FFB000 (separador)
│                                    │
│                                    │
│   TÍTULO DEL DOCUMENTO             │  ← 28pt bold #424242 (centrado)
│                                    │
│   Subtítulo descriptivo            │  ← 18pt #424242
│                                    │
│   ────────────────────────         │  ← línea 3pt #FFB000
│                                    │
│   Autor: Mgtr. Nombre Apellido     │  ← 14pt #424242
│   T.S. Big Data y CD · ITSE        │  ← 14pt #424242
│   {Mes} · {año}                     │  ← 14pt #7B7B7B (usar mes y año actual)
└────────────────────────────────────┘
```

**Reglas obligatorias de la portada:**
- Logo en la parte SUPERIOR de la página (header)
- Línea dorada de 3pt como separador entre el logo y el título
- El título va centrado en el medio de la página
- Al pie: autor + carrera de referencia (T.S. en Big Data y Ciencia de Datos) + fecha

---

## Header y footer del PDF

### Header (todas las páginas)
- Logo ITSE en esquina superior izquierda (alto 1 cm)
- Línea inferior: 0.5pt `#AEAEAE`

### Footer (todas las páginas)
- "Instituto Técnico Superior Especializado · itse.ac.pa" centrado, 9pt `#7B7B7B`
- Numeración: "Página X de Y", derecha, 9pt `#7B7B7B`
- Línea superior: 0.5pt `#FFB000`

---

## Tipografía en el PDF

| Elemento | Fuente | Tamaño | Color |
|---|---|---|---|
| Título | Helvetica Bold | 28pt | `#424242` |
| Subtítulo | Helvetica | 18pt | `#424242` |
| H1 | Helvetica Bold | 22pt | `#424242` |
| H2 | Helvetica Bold | 18pt | `#424242` |
| H3 | Helvetica Bold | 14pt | `#424242` |
| Body | Helvetica | 11pt | `#424242` |
| Caption | Helvetica Italic | 9pt | `#7B7B7B` |
| Números grandes | Helvetica Bold | 36pt | `#FFB000` |

⚠️ **SIEMPRE incrusta las fuentes** en el PDF.

---

## Elementos gráficos en el PDF

- **Líneas decorativas:** `#FFB000`, 2-3pt
- **Recuadros (callouts):** borde izquierdo 4pt `#FFB000`, fondo `#F7F7F7`
- **Cifras destacadas:** 36-48pt bold `#FFB000`, label 11pt `#7B7B7B`

---

## PDF multipágina: numeración y marcas

- Numeración: "Página 1 de 10" en footer derecha
- Marca de agua (opcional): "BORRADOR" o "CONFIDENCIAL" en gris con 30% opacidad, rotada 45°

---

## Comprimir y optimizar

```bash
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 \
   -dPDFSETTINGS=/ebook \
   -dNOPAUSE -dQUIET -dBATCH \
   -sOutputFile=reporte-optimizado.pdf reporte.pdf
```

Niveles: `/screen` (72 DPI), `/ebook` (150 DPI, recomendado), `/printer` (300 DPI), `/prepress` (máxima).

---

## Cheatsheet

```
ITSE PDF
========
Tipografía: Helvetica / Arial (incrustar)
Tamaño: Carta o A4
Márgenes: 2.5cm
Carrera de referencia: T.S. en Big Data y Ciencia de Datos

PALETA:
  #FFB000 Dorado (líneas, KPI, callouts)
  #424242 Gris Carbón (texto, títulos)
  #FFFFFF Blanco (fondo)
  #F7F7F7 Gris claro (filas alternas, callouts)
  #7B7B7B Gris 100 (footer, captions)
  #AEAEAE Gris 300 (bordes)

TIPOGRAFÍA:
  Título:    28pt bold #424242
  H1:        22pt bold #424242
  H2:        18pt bold #424242
  Body:      11pt      #424242
  Caption:   9pt       #7B7B7B
  Números:   36pt bold #FFB000

LOGO: ARRIBA en portadas (header, 1.5-2cm alto)
      Header en páginas interiores (1cm alto)
      Footer = texto gris + numeración

GENERACIÓN:
  WeasyPrint (recomendado): HTML + CSS → PDF
  LibreOffice: DOCX/PPTX → PDF
  ReportLab: Python puro
```

---

## Recursos adicionales

- `references/itse/colors.md` — paleta completa
- `references/itse/typography.md` — sistema tipográfico
- `references/itse/logo.md` — uso del logo
- `references/itse/branding.md` — datos institucionales
- `assets/logo-itse-horizontal.png` — logo principal
- Skill complementaria: `pdf`
