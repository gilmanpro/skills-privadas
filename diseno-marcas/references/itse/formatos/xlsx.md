# Plantilla Excel — ITSE

Guía para crear hojas de cálculo Excel (.xlsx) con el estilo ITSE usando la skill `ofimatica` (seccion hojas de calculo; absorbio a la antigua `xlsx`) + esta skill.

---

## ⚠️ Regla de carpeta de trabajo (OBLIGATORIA)

```bash
mkdir "%TEMP%\opencode\xlsx-YYYYMMDD-HHMMSS"
```

Si la hoja tiene fórmulas complejas, ejecuta `scripts/recalc.py` (de la skill `ofimatica`) para forzar el recálculo.

---

## 🚨 REGLA: Logo del ITSE ARRIBA en la primera hoja

> **En la primera hoja (portada/cover) de cada workbook, el logo del ITSE
> va en la parte SUPERIOR de la hoja — NUNCA en el centro vertical.**

- **Primera hoja (cover/portada):** Logo ITSE en la parte superior (fila 1, esquina superior izquierda), seguido de la banda dorada en la fila 2
- **Hojas de datos:** Solo el header (logo a la izquierda + título + fecha) en la fila 1, banda dorada en la fila 2
- **No es necesario repetir el logo** en hojas internas si ya está en el header de impresión

---

## Especificaciones de la hoja

| Parámetro | Valor |
|---|---|
| Tipografía | Calibri 11pt (cuerpo), Calibri 14pt (títulos) |
| Color de fondo principal | Blanco (`#FFFFFF`) |
| Color de encabezado | Dorado ITSE o Gris Carbón |
| Filas alternas | Sí, con `#F7F7F7` |
| Ancho de columnas | Auto-ajustado al contenido |
| Carrera de referencia | **T.S. en Big Data y Ciencia de Datos** (Área de Innovación Digital) |

---

## Paleta aplicada a Excel

| Color | HEX | Uso |
|---|---|---|
| Dorado ITSE | `#FFB000` | Encabezados principales, títulos, líneas decorativas |
| Gris Carbón | `#424242` | Encabezados secundarios, texto importante |
| Blanco | `#FFFFFF` | Fondo, texto sobre dorado/oscuro |
| Gris claro | `#F7F7F7` | Filas alternas |
| Gris 100 | `#7B7B7B` | Texto secundario, footer |
| Gris 300 | `#AEAEAE` | Bordes de tabla |

---

## Tipografía en celdas

| Elemento | Fuente | Tamaño | Peso | Color |
|---|---|---|---|---|
| Título del documento (fila 1) | Calibri | 16-18pt | Bold | `#424242` |
| Subtítulo | Calibri | 12pt | Regular | `#7B7B7B` |
| Encabezado de tabla | Calibri | 11pt | Bold | `#FFFFFF` (sobre fondo oscuro/dorado) |
| Datos | Calibri | 11pt | Regular | `#424242` |
| Total / suma | Calibri | 11pt | Bold | `#424242` |
| Footer / notas | Calibri | 9pt | Regular | `#7B7B7B` |
| Números grandes (KPIs) | Calibri | 24-36pt | Bold | `#FFB000` |

---

## Estilo de tablas (la clave visual)

### Encabezado de tabla
- **Fondo:** `#FFB000` (dorado) o `#424242` (gris carbón)
- **Texto:** `#FFFFFF`, Calibri 11pt **Bold**
- **Alineación:** Centrada
- **Borde inferior:** 2pt sólido `#FFB000` (si el fondo del header es otro color)
- **Padding:** 8pt en cada lado

### Filas alternas (zebra striping)
- Fila par (2, 4, 6...): fondo `#FFFFFF`
- Fila impar (3, 5, 7...): fondo `#F7F7F7`
- **NO usar rayas más oscuras** que el `#F7F7F7` — la idea es que sea sutil.

### Bordes
- Solo horizontales internos: 0.5pt `#AEAEAE`
- Sin bordes verticales (o muy sutiles)
- Borde superior del header: 1.5pt `#FFB000`
- Borde inferior de la última fila: 1.5pt `#FFB000`

### Fila de totales
- Fondo: `#F7F7F7` con borde superior 2pt `#FFB000`
- Texto: **Bold** `#424242`
- Etiqueta "TOTAL" alineada a la derecha

### Ejemplo de tabla

```
┌────────────────────────────────────────────────┐
│  CARRERA              DURACIÓN    CRÉDITOS     │ ← fondo #FFB000, texto blanco bold
├────────────────────────────────────────────────┤
│  T.S. Des. Software   2a 4m        112         │ ← fondo blanco
├────────────────────────────────────────────────┤
│  T.S. Big Data y CD   2a 4m        113         │ ← fondo #F7F7F7
├────────────────────────────────────────────────┤
│  T.S. Ciberseguridad  2a 4m        122         │ ← fondo blanco
├────────────────────────────────────────────────┤
│  TOTAL                            347          │ ← fondo #F7F7F7, bold, borde sup. dorado
└────────────────────────────────────────────────┘
```

---

## Encabezados y pies de hoja (header/footer)

### Header (parte superior de cada hoja) — LOGO ARRIBA
- **Fila 1 (ARRIBA):** logo ITSE a la izquierda + título del documento + fecha
- **Fila 2:** banda dorada de 6pt de alto (color de relleno `#FFB000`) como divisor
- **Fila 3:** espacio en blanco (1 fila vacía)
- **Fila 4 en adelante:** datos

### Footer
- Última fila: notas en Calibri 9pt, color `#7B7B7B`
- Configurar en: Insertar → Encabezado y pie de página

---

## Formato de números

| Tipo | Formato Panamá | Formato Excel |
|---|---|---|
| Enteros grandes | 4.000 | `#,##0` |
| Porcentaje | 80% | `0%` |
| Moneda (USD) | $1.500,00 | `"$"#,##0.00` |
| Moneda (Balboa) | B/. 1.500,00 | `"B/."#,##0.00` |
| Decimales | 3,50 | `#,##0.00` |
| Fechas | 30/06/{año} | `dd/mm/yyyy` (usar año actual) |

⚠️ **Usar formato Panamá:** separador de miles con punto (`.`), separador decimal con coma (`,`).

---

## Celdas KPI (cifras destacadas)

Para dashboards o resúmenes ejecutivos, usa celdas "card" con números grandes:

| | A | B | C |
|---|---|---|---|
| **1** | | | |
| **2** | **[+4.000]** | **[15]** | **[+80%]** | ← números gigantes 36pt, dorado bold
| **3** | Estudiantes | Carreras | Inserción | ← labels 10pt, gris claro
| **4** | activos | | laboral |

Para esto:
1. Combina 3 celdas para cada KPI (ej: A2:B2)
2. Aplica fondo: `#F7F7F7` o `#424242`
3. Tamaño de fuente: 32-36pt
4. Color: `#FFB000` (sobre fondo claro) o `#FFFFFF` (sobre fondo oscuro)
5. Borde superior 4pt `#FFB000`

---

## Gráficos con estilo ITSE

Si el documento incluye gráficos, aplica:

| Elemento | Estilo |
|---|---|
| Colores de series | `#FFB000`, `#424242`, `#225082`, `#9EBE43`, `#CD2E26` |
| Título del gráfico | Calibri 14pt Bold, `#424242` |
| Eje labels | Calibri 10pt, `#424242` |
| Leyenda | Calibri 10pt, `#424242` |
| Fondo del gráfico | `#FFFFFF` |
| Líneas de grid | `#AEAEAE`, muy sutiles |
| Borde del gráfico | Ninguno (o 0.5pt `#AEAEAE`) |

### Ejemplo de paleta de gráfico

Para un gráfico de barras: usar secuencia `Dorado → Gris → Azul → Verde → Rojo`.

---

## Generación con openpyxl (script base)

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
from openpyxl.utils import get_column_letter

# Colores ITSE
DORADO = "FFB000"
GRIS = "424242"
BLANCO = "FFFFFF"
GRIS_CLARO = "F7F7F7"
GRIS_100 = "7B7B7B"
GRIS_300 = "AEAEAE"

wb = Workbook()
ws = wb.active
ws.title = "Carreras ITSE"

# === HEADER (fila 1) ===
ws.merge_cells("A1:C1")
ws["A1"] = "ITSE — Instituto Técnico Superior Especializado"
ws["A1"].font = Font(name="Calibri", size=14, bold=True, color=GRIS)
ws["A1"].alignment = Alignment(horizontal="left", vertical="center")
ws.row_dimensions[1].height = 30

# Banda dorada (fila 2)
for col in range(1, 4):
    cell = ws.cell(row=2, column=col)
    cell.fill = PatternFill("solid", fgColor=DORADO)
ws.row_dimensions[2].height = 6

# Título de la tabla (fila 4)
ws.merge_cells("A4:C4")
ws["A4"] = "Oferta Académica — Innovación Digital"
ws["A4"].font = Font(name="Calibri", size=16, bold=True, color=GRIS)

# === ENCABEZADOS (fila 6) ===
headers = ["CARRERA", "DURACIÓN", "CRÉDITOS"]
header_fill = PatternFill("solid", fgColor=GRIS)
header_font = Font(name="Calibri", size=11, bold=True, color=BLANCO)
header_align = Alignment(horizontal="center", vertical="center", wrap_text=True)
border_bottom = Border(bottom=Side(style="medium", color=DORADO))

for col, h in enumerate(headers, 1):
    cell = ws.cell(row=6, column=col, value=h)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = header_align
    cell.border = border_bottom
ws.row_dimensions[6].height = 28

# === DATOS ===
data = [
    ("T.S. en Desarrollo de Software", "2a 4m", 112),
    ("T.S. en Big Data y Ciencia de Datos", "2a 4m", 113),
    ("T.S. en Ciberseguridad", "2a 4m", 122),
    ("T.S. en Inteligencia Artificial", "2a 4m", 126),
]

thin_border = Border(
    bottom=Side(style="thin", color=GRIS_300)
)

for i, row in enumerate(data, 7):
    for col, val in enumerate(row, 1):
        cell = ws.cell(row=i, column=col, value=val)
        cell.font = Font(name="Calibri", size=11, color=GRIS)
        # Filas alternas
        if i % 2 == 0:
            cell.fill = PatternFill("solid", fgColor=GRIS_CLARO)
        cell.border = thin_border
        if col == 3:
            cell.alignment = Alignment(horizontal="center")

# === TOTAL ===
total_row = 7 + len(data)
ws.cell(row=total_row, column=1, value="TOTAL").font = Font(bold=True, color=GRIS)
ws.cell(row=total_row, column=1).alignment = Alignment(horizontal="right")
ws.cell(row=total_row, column=1).fill = PatternFill("solid", fgColor=GRIS_CLARO)
ws.cell(row=total_row, column=1).border = Border(
    top=Side(style="medium", color=DORADO),
    bottom=Side(style="thin", color=GRIS_300)
)

ws.cell(row=total_row, column=3, value=sum(r[2] for r in data))
ws.cell(row=total_row, column=3).font = Font(bold=True, color=GRIS)
ws.cell(row=total_row, column=3).fill = PatternFill("solid", fgColor=GRIS_CLARO)
ws.cell(row=total_row, column=3).border = Border(
    top=Side(style="medium", color=DORADO),
    bottom=Side(style="thin", color=GRIS_300)
)
ws.cell(row=total_row, column=3).alignment = Alignment(horizontal="center")

# Anchos de columna
ws.column_dimensions["A"].width = 40
ws.column_dimensions["B"].width = 15
ws.column_dimensions["C"].width = 12

# Footer (última fila)
from datetime import datetime
fecha_actual = datetime.now().strftime("%B %Y")
ws.cell(row=total_row + 3, column=1, value=f"Fuente: itse.ac.pa · {fecha_actual}")
ws.cell(row=total_row + 3, column=1).font = Font(name="Calibri", size=9, color=GRIS_100)

wb.save("carreras-itse.xlsx")
```

---

## Cheatsheet

```
ITSE EXCEL
==========
Tipografía: Calibri 11pt
Fondo principal: blanco
Filas alternas: #F7F7F7
Carrera de referencia: T.S. en Big Data y Ciencia de Datos

PALETA:
  #FFB000 Dorado (encabezado, totales, KPI)
  #424242 Gris Carbón (texto, encabezado alternativo)
  #FFFFFF Blanco (fondo, texto sobre dorado)
  #F7F7F7 Gris claro (filas alternas, totales)
  #7B7B7B Gris 100 (footer, notas)
  #AEAEAE Gris 300 (bordes)

LOGO: ARRIBA en la primera hoja (fila 1, esquina sup. izq.)
      Banda dorada en fila 2 como separador

ENCABEZADO DE TABLA:
  Fondo: #FFB000 o #424242
  Texto: blanco bold
  Borde inferior: 1.5pt #FFB000

FILAS:
  Alternas: blanco / #F7F7F7
  Bordes: solo horizontales 0.5pt #AEAEAE

TOTALES:
  Borde superior: 2pt #FFB000
  Fondo: #F7F7F7
  Texto: bold

NÚMEROS:
  Formato Panamá: 4.000 / 3,50
  Formato Excel: #,##0 / #,##0.00
```

---

## Recursos adicionales

- `references/itse/colors.md` — paleta completa
- `references/itse/typography.md` — sistema tipográfico
- `references/itse/branding.md` — datos institucionales
- Skill complementaria: `ofimatica` (seccion hojas de calculo; absorbio a la antigua `xlsx`)
