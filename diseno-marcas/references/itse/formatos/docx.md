# Plantilla Word / Documentos — ITSE

Guía para crear documentos Word (.docx) institucionales del ITSE con la skill `docx` + esta skill.

---

## ⚠️ Regla de carpeta de trabajo (OBLIGATORIA)

```bash
mkdir "%TEMP%\opencode\docx-YYYYMMDD-HHMMSS"
```

Todos los archivos intermedios (imágenes, scripts, docx sin terminar) van ahí. El `.docx` final se copia a la carpeta de destino.

---

## 🚨 REGLA CRÍTICA: Logo del ITSE ARRIBA en portadas

> **En TODA portada de documento Word, el logo del ITSE va en la parte
> SUPERIOR de la página (header o top del cuerpo) — NUNCA en el centro
> vertical, NUNCA debajo del título.** El logo preside la portada.

- **Portada de documento:** Logo horizontal en el TOP (alineado a la izquierda en el header o centrado arriba del título), alto ~2–3 cm
- **Documentos con varias páginas:** Logo en el HEADER de Word (aparece en todas las páginas), alineado a la izquierda, alto ~1–1.5 cm
- **Pie de página:** Logo footer o solo texto "Instituto Técnico Superior Especializado" + "itse.ac.pa"

---

## Especificaciones del documento

| Parámetro | Valor |
|---|---|
| Tamaño de página | Carta (21.59 × 27.94 cm) o A4 (21 × 29.7 cm) |
| Tipografía | **Calibri** (default Word) o **Arial** |
| Color de fondo | Blanco |
| Márgenes | 2.5 cm superior/inferior, 2.5 cm laterales |
| Carrera de referencia | **T.S. en Big Data y Ciencia de Datos** (Área de Innovación Digital) |

---

## Paleta aplicada a Word

### Colores personalizados

| Color | HEX | Uso en Word |
|---|---|---|
| Dorado ITSE | `#FFB000` | Bordes, líneas decorativas, títulos, íconos |
| Gris Carbón | `#424242` | Texto principal, fondo de portada/encabezados |
| Blanco | `#FFFFFF` | Fondo principal, texto sobre dorado/oscuro |
| Gris claro | `#F7F7F7` | Filas alternas en tablas, fondo de recuadros |
| Gris 100 | `#7B7B7B` | Texto secundario, captions, footnotes |

---

## Estilos de párrafo personalizados

En Word, define estos estilos (Inicio → Estilos → Crear estilo):

### Título Principal (para documentos)
- Fuente: Calibri, 28pt, **Bold**, color `#424242`
- Espacio antes: 24pt, después: 12pt
- Borde inferior: 3pt sólido `#FFB000`

### Título 1
- Fuente: Calibri, 22pt, **Bold**, color `#424242`
- Espacio antes: 18pt, después: 8pt

### Título 2
- Fuente: Calibri, 18pt, **Bold**, color `#424242`
- Espacio antes: 14pt, después: 6pt

### Título 3
- Fuente: Calibri, 14pt, **Bold**, color `#424242`
- Espacio antes: 10pt, después: 4pt

### Cuerpo
- Fuente: Calibri, 11pt, Regular, color `#424242`
- Interlineado: 1.5
- Espacio después: 6pt
- Sangría primera línea: 1.27 cm (opcional)

### Caption
- Fuente: Calibri, 9pt, Regular, color `#7B7B7B`, itálica
- Alineación: centrada (si es pie de figura)

### Cita destacada (Pull quote)
- Fuente: Calibri, 14pt, **Bold**, color `#FFB000`
- Sangría izquierda: 1.5 cm
- Borde izquierdo: 4pt sólido `#FFB000`

---

## Header y footer institucionales

### Header (encabezado)

```
┌──────────────────────────────────────────┐
│  [LOGO ITSE]           www.itse.ac.pa    │  ← 1 línea, logo a la izquierda
└──────────────────────────────────────────┘
```

- Logo: `assets/logo-itse-horizontal.png`, alto 1 cm
- Línea inferior del header: 1pt sólido `#AEAEAE`
- Activar en: Insertar → Encabezado → primera página diferente (opcional)

### Footer (pie de página)

```
┌──────────────────────────────────────────┐
│  Instituto Técnico Superior Especializado │  ← 9pt #7B7B7B
│  Página [X] de [Y]                       │  ← 9pt #7B7B7B, derecha
└──────────────────────────────────────────┘
```

- Línea superior: 1pt sólido `#FFB000` (en lugar de gris)
- Texto en gris claro
- Activar en: Insertar → Pie de página

---

## Portada de documento

Layout sugerido (1 página completa) — **logo ARRIBA**:

```
┌────────────────────────────────────┐
│  [LOGO ITSE]                       │  ← LOGO ARRIBA (header, 2-3cm alto)
│  ────────────────────────          │  ← línea 3pt #FFB000 (separador)
│                                    │
│                                    │
│                                    │
│   TÍTULO DEL DOCUMENTO             │  ← 28pt bold #424242 (centrado)
│                                    │
│   Subtítulo descriptivo            │  ← 18pt #424242
│                                    │
│  ────────────────────────          │  ← línea 3pt #FFB000
│                                    │
│                                    │
│   Autor: Mgtr. Nombre Apellido     │  ← 14pt #424242
│   T.S. Big Data y CD · ITSE        │  ← 14pt #424242
│                                    │
│   {Mes} · {año}                     │  ← 14pt #7B7B7B (usar mes y año actual)
│                                    │
│                                    │
└────────────────────────────────────┘
```

**Reglas de la portada (obligatorias):**
- El logo SIEMPRE va en la parte SUPERIOR de la página, NO en el centro
- Una línea dorada de 3pt separa el logo del cuerpo del título
- El título va centrado en el medio de la página
- Al pie va el autor + carrera de referencia (T.S. en Big Data y Ciencia de Datos) + fecha

**Fondo opcional:** Banda dorada vertical en el lado izquierdo (1cm de ancho) o fondo `#F7F7F7` en la parte superior (5cm de alto) — NUNCA sustituye al logo, solo lo acompaña.

---

## Tablas con estilo ITSE

### Header de tabla
- Fondo: `#424242` o `#FFB000`
- Texto: `#FFFFFF`, Calibri 11pt **Bold**
- Padding: 8pt

### Filas alternas
- Fila par: `#FFFFFF`
- Fila impar: `#F7F7F7`

### Bordes
- Solo bordes horizontales internos: 0.5pt `#AEAEAE`
- Sin bordes verticales
- Borde superior del header: 1pt `#FFB000` (si el header es blanco)
- Borde inferior de la última fila: 1pt `#FFB000`

### Ejemplo

```
┌──────────────────────────────────────────────────┐
│  CARRERA                       DURACIÓN  CRÉD.  │  ← fondo #424242, texto blanco
├──────────────────────────────────────────────────┤
│   T.S. Des. Software           2a 4m     112     │  ← fondo blanco
├──────────────────────────────────────────────────┤
│   T.S. Big Data y CD           2a 4m     113     │  ← fondo #F7F7F7
├──────────────────────────────────────────────────┤
│   T.S. Ciberseguridad          2a 4m     122     │  ← fondo blanco
└──────────────────────────────────────────────────┘
```

---

## Listas con estilo ITSE

### Bullets
- Símbolo: `▸` (triángulo pequeño) o `•` (círculo)
- Color: `#FFB000` para el símbolo
- Texto: `#424242`, Calibri 11pt
- Espaciado entre items: 6pt

### Numeradas
- Número en dorado `#FFB000`, **Bold**
- Texto en gris carbón

### Lista anidada (sub-items)
- Símbolo: `–` (guion) en gris claro
- Texto: igual al padre pero 10pt

---

## Recuadros / Callouts

### Callout informativo (azul)
- Borde izquierdo: 4pt sólido `#225082`
- Fondo: `#F7F7F7`
- Padding: 12pt
- Texto: Calibri 11pt `#424242`

### Callout de éxito (verde)
- Borde izquierdo: 4pt sólido `#9EBE43`
- Fondo: `#F7F7F7`
- Padding: 12pt

### Callout de advertencia (naranja)
- Borde izquierdo: 4pt sólido `#F57C00`
- Fondo: `#F7F7F7`
- Padding: 12pt

### Callout de error (rojo)
- Borde izquierdo: 4pt sólido `#CD2E26`
- Fondo: `#F7F7F7`
- Padding: 12pt

---

## Generación con python-docx (script base)

```python
from docx import Document
from docx.shared import Pt, RGBColor, Cm, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# Colores ITSE
DORADO = RGBColor(0xFF, 0xB0, 0x00)
GRIS = RGBColor(0x42, 0x42, 0x42)
GRIS_CLARO = RGBColor(0xF7, 0xF7, 0xF7)
GRIS_100 = RGBColor(0x7B, 0x7B, 0x7B)

doc = Document()

# Configurar márgenes
for section in doc.sections:
    section.top_margin = Cm(2.5)
    section.bottom_margin = Cm(2.5)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.5)

# Header con logo (aparece en todas las páginas)
header = doc.sections[0].header
p_header = header.paragraphs[0]
p_header.alignment = WD_ALIGN_PARAGRAPH.LEFT
run = p_header.add_run()
run.add_picture("logo-itse-horizontal.png", width=Inches(1.5))

# === PORTADA: LOGO ARRIBA (centrado en el top de la primera página) ===
# Centrar el logo en la parte superior de la portada
p_logo = doc.add_paragraph()
p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p_logo.add_run()
run.add_picture("logo-itse-horizontal.png", width=Inches(2.5))  # ARRIBA centrado

# Línea dorada decorativa debajo del logo
p_linea_logo = doc.add_paragraph()
p_linea_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
pPr = p_linea_logo._p.get_or_add_pPr()
pBdr = OxmlElement('w:pBdr')
bottom = OxmlElement('w:bottom')
bottom.set(qn('w:val'), 'single')
bottom.set(qn('w:sz'), '18')  # 3pt
bottom.set(qn('w:color'), 'FFB000')
pBdr.append(bottom)
pPr.append(pBdr)

# Espacio antes del título
doc.add_paragraph()

# Título principal (centrado en el medio de la portada)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("TÍTULO DEL DOCUMENTO")
run.font.size = Pt(28)
run.font.bold = True
run.font.color.rgb = GRIS
run.font.name = "Calibri"

# Subtítulo
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("Subtítulo descriptivo")
run.font.size = Pt(18)
run.font.color.rgb = GRIS
run.font.name = "Calibri"

# Línea dorada separadora
p_linea = doc.add_paragraph()
p_linea.alignment = WD_ALIGN_PARAGRAPH.CENTER
pPr = p_linea._p.get_or_add_pPr()
pBdr = OxmlElement('w:pBdr')
bottom = OxmlElement('w:bottom')
bottom.set(qn('w:val'), 'single')
bottom.set(qn('w:sz'), '18')  # 3pt
bottom.set(qn('w:color'), 'FFB000')
pBdr.append(bottom)
pPr.append(pBdr)

# Autor + carrera de referencia (al pie de la portada)
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
from datetime import datetime
fecha_actual = datetime.now().strftime("%B · %Y")  # ej: "June · 2026"
run = p.add_run(f"Mgtr. Nombre Apellido\nT.S. en Big Data y Ciencia de Datos · ITSE · {fecha_actual}")
run.font.size = Pt(14)
run.font.color.rgb = GRIS
run.font.name = "Calibri"

# === SALTO DE PÁGINA → contenido del documento ===
doc.add_page_break()

# Cuerpo del documento
p = doc.add_paragraph()
run = p.add_run("Este es el cuerpo del documento. Usa Calibri 11pt, interlineado 1.5.")
run.font.size = Pt(11)
run.font.color.rgb = GRIS
run.font.name = "Calibri"
p.paragraph_format.line_spacing = 1.5

doc.save("documento-itse.docx")
```

---

## Cheatsheet

```
ITSE WORD
=========
Tipografía: Calibri / Arial
Márgenes: 2.5cm
Tamaño: Carta o A4
Carrera de referencia: T.S. en Big Data y Ciencia de Datos

PALETA:
  #FFB000 Dorado (acentos, líneas, títulos)
  #424242 Gris Carbón (texto principal)
  #FFFFFF Blanco (fondo)
  #F7F7F7 Gris claro (callouts, filas alternas)
  #7B7B7B Gris 100 (texto secundario)

ESTILOS:
  Título Principal: 28pt bold #424242 + línea dorada inferior
  Título 1:        22pt bold #424242
  Título 2:        18pt bold #424242
  Cuerpo:          11pt regular #424242, interlineado 1.5
  Caption:         9pt itálica #7B7B7B

LOGO: ARRIBA en portadas (header, 2-3cm ancho)
      Header en páginas interiores (1.5cm ancho)
      Footer = texto gris
```

---

## Recursos adicionales

- `references/itse/colors.md` — paleta completa
- `references/itse/typography.md` — sistema tipográfico
- `references/itse/logo.md` — uso del logo
- `references/itse/branding.md` — datos institucionales
- `assets/logo-itse-horizontal.png` — logo principal
