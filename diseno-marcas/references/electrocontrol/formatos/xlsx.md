# Aplicación del diseño Electrocontrol a Excel (.xlsx)

Guía para crear hojas Excel con el sistema de diseño de IoT Tech / Electrocontrol. **Esta skill NO reemplaza la skill `ofimatica`** (seccion hojas de calculo; absorbio a la antigua `xlsx`) — la complementa.

---

## Regla de carpetas de trabajo (OBLIGATORIA)

```bash
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
WORKDIR=".tmp/xlsx-electrocontrol-$TIMESTAMP"
mkdir "$WORKDIR"
```

Genera el `.xlsx` en `WORKDIR`, luego cópialo al destino.

**Recalcular fórmulas:** Después de cualquier cambio, ejecuta OBLIGATORIAMENTE `scripts/recalc.py` (de la skill `ofimatica`):

```bash
python "<base-dir-skill-ofimatica>/scripts/recalc.py" "$WORKDIR\archivo.xlsx"
```

Esto recalcula todas las fórmulas y actualiza los valores cacheados, evitando que Excel muestre "0" o valores incorrectos al abrir.

---

## Limitaciones de Excel

Excel es **menos flexible** que web/PowerPoint para diseño. Lo que SÍ puedes hacer:

- ✅ Colores de fondo de celda (incluyendo degradados limitados en versiones recientes)
- ✅ Colores y estilos de fuente
- ✅ Bordes de celda
- ✅ Formato condicional con colores
- ✅ Temas de color del libro
- ✅ Imágenes insertadas (logo)
- ✅ Combinar celdas para crear "cards"

Lo que **NO puedes** hacer fácilmente:

- ❌ Degradados complejos en celdas individuales
- ❌ Bordes redondeados (esos son nativos de CSS, no de celdas Excel)
- ❌ Glassmorphism (no hay transparencia en celdas)
- ❌ Texto con degradado de fondo
- ❌ Esquinas redondeadas en cualquier forma

**Estrategia:** Excel con marca se logra con **paleta de colores consistente + tipografía bold + imágenes del logo** + estructura clara, no intentando replicar el dark mode de la web.

---

## Dos enfoques: Dark vs Light

| Caso de uso | Enfoque |
|---|---|
| **Hoja de presupuesto / cotización** | **Light** con acentos cyan (estándar) |
| **Hoja de reporte mensual** | **Light** con acentos cyan |
| **Dashboard ejecutivo** | **Dark** (para presentaciones) |
| **Plantilla de orden de servicio** | **Light** con acentos cyan |
| **Inventario** | **Light** con acentos cyan |
| **Cronograma de proyecto** | **Light** con acentos cyan |
| **Tracking de KPIs** | **Dark** (para presentación) |

**Regla:** si la hoja se va a imprimir → **light**. Si es para proyectar/presentar → **dark**.

---

## Tema de color del libro

Define el theme XML del libro con la paleta de marca. Esto afecta los colores disponibles en los selectores:

```xml
<!-- theme1.xml — añadir en la sección <a:clrScheme> -->
<a:clrScheme name="Electrocontrol">
  <a:lt1><a:srgbClr val="FFFFFF"/></a:lt1>      <!-- Light 1: blanco -->
  <a:dk1><a:srgbClr val="0F172A"/></a:dk1>      <!-- Dark 1: slate-900 -->
  <a:lt2><a:srgbClr val="CBD5E1"/></a:lt2>      <!-- Light 2: slate-300 -->
  <a:dk2><a:srgbClr val="1E293B"/></a:dk2>      <!-- Dark 2: slate-800 -->
  <a:accent1><a:srgbClr val="06B6D4"/></a:accent1>  <!-- Cyan 500 -->
  <a:accent2><a:srgbClr val="A855F7"/></a:accent2>  <!-- Purple 500 -->
  <a:accent3><a:srgbClr val="EC4899"/></a:accent3>  <!-- Pink 500 -->
  <a:accent4><a:srgbClr val="3B82F6"/></a:accent4>  <!-- Blue 500 (IoT) -->
  <a:accent5><a:srgbClr val="F97316"/></a:accent5>  <!-- Orange 500 (ECU) -->
  <a:accent6><a:srgbClr val="22C55E"/></a:accent6>  <!-- Green 500 (Auto) -->
  <a:hlink><a:srgbClr val="22D3EE"/></a:hlink>      <!-- Cyan 400 -->
  <a:folHlink><a:srgbClr val="C084FC"/></a:folHlink>  <!-- Purple 400 -->
</a:clrScheme>
```

---

## Paleta para celdas

### Light mode (recomendado)

| Token | HEX | Uso |
|---|---|---|
| **Header fondo** | `#06B6D4` cyan-500 | Header de tablas, secciones |
| **Header texto** | `#FFFFFF` blanco | Texto sobre header cyan |
| **Fondo alterno** | `#F1F5F9` slate-100 | Filas alternas (zebra striping) |
| **Fondo destacado** | `#CFFAFE` cyan-100 | Celdas con valor importante, totales |
| **Texto normal** | `#0F172A` slate-900 | Texto en celdas |
| **Texto destacado** | `#06B6D4` cyan-500 | Cifras importantes, valores clave |
| **Bordes** | `#E2E8F0` slate-200 | Bordes de celda |
| **Separador fuerte** | `#06B6D4` cyan-500 | Línea debajo del header |

### Dark mode (para dashboards)

| Token | HEX | Uso |
|---|---|---|
| **Header fondo** | `#06B6D4` cyan-500 | Header (igual que light) |
| **Fondo principal** | `#0F172A` slate-900 | Fondo de todas las celdas |
| **Fondo alterno** | `#1E293B` slate-800 | Filas alternas |
| **Fondo destacado** | `#164E63` cyan-900 | Celdas destacadas |
| **Texto normal** | `#FFFFFF` blanco | Texto |
| **Texto secundario** | `#94A3B8` slate-400 | Labels, metadatos |
| **Bordes** | `#334155` slate-700 | Bordes sutiles |

---

## Formato de celdas clave

### Header de tabla

```
Fondo:        #06B6D4 cyan-500
Texto:        #FFFFFF blanco
Fuente:       Inter / Calibri, 11pt
Peso:         Bold
Alineación:   Centro horizontal y vertical
Borde:        Sólido #0E7490 cyan-700, 1px abajo
Padding:      ~6px (configurar altura de fila a 24pt)
```

### Fila de datos (zebra)

```
Fila impar:   Fondo #FFFFFF
Fila par:     Fondo #F1F5F9 slate-100
Texto:        #0F172A slate-900
Fuente:       Inter / Calibri, 10pt
Alineación:   Izquierda para texto, derecha para números
```

### Fila de total

```
Fondo:        #CFFAFE cyan-100
Texto:        #0F172A slate-900, 12pt, bold
Borde superior: 2px #06B6D4 cyan-500
```

### Celdas de input

```
Fondo:        #FFFFFF
Borde:        1px #CBD5E1 slate-300
Borde focus:  2px #06B6D4 cyan-500 (configurar en validación)
Fuente:       Inter / Calibri, 10pt
```

### Celdas de cálculo (formulas)

```
Fondo:        #F8FAFC slate-50 (muy sutil)
Texto:        #0F172A
Borde:        ninguno
```

---

## Estructura típica de una hoja con marca

### Hoja de cotización (light mode)

```
┌────────────────────────────────────────────────────────────┐
│ A1:  [LOGO]  ← imagen, alineado a la izquierda           │
│ A2:  COTIZACIÓN                                              │ ← 18pt, bold
│ A3:  Cliente: {{nombre}}                                     │ ← 11pt
│ A4:  Referencia: COT-2026-001                                │
│ A5:  Fecha: {{fecha}}                                        │
│ A6:  Técnico: Malkom Daniel Cordoba                          │
│                                                             │
│ A8:  DETALLE (fila 8 vacía, sin contenido)                  │
│                                                             │
│     A9: ITEM  │ B9: DESCRIPCIÓN  │ C9: CANT │ D9: P.UNIT  │ E9: TOTAL  │ ← header cyan
│    ────────────────────────────────────────────────────────  │
│     A10: 1    │ IoT & Desarrollo │ 1        │ $1,500.00   │ $1,500.00 │ ← datos
│     A11: 2    │ Reparación ECU   │ 1        │   $800.00   │   $800.00 │
│     A12: 3    │ Automatización   │ 1        │ $2,000.00   │ $2,000.00 │
│     A13: 4    │ Programación     │ 1        │ $1,200.00   │ $1,200.00 │
│                                                             │
│     E15: SUBTOTAL                                  $5,500.00 │ ← bold
│     E16: ITBMS 7%                                    $385.00 │
│     E17: ════════ línea cyan ════════════                   │
│     E18: TOTAL                                     $5,885.00 │ ← 14pt, bold, fondo cyan-100
│                                                             │
│ A20:  Acepto los términos y condiciones                     │
│ A21:  Firma: ___________________                            │
│                                                             │
│ A23:  CONTACTO                                                │
│ A24:  Malkom Daniel Cordoba · +507 6250-9318                │
│ A25:  http://pag.electrocontrol.cloud/                       │
└────────────────────────────────────────────────────────────┘
```

### Dashboard de KPIs (dark mode)

```
┌────────────────────────────────────────────────────────────┐
│ A1: [LOGO pequeño] DASHBOARD IoT TECH · 2026          (header)
│ A2: Métricas operacionales · Actualizado: {{fecha}}        │ ← subtitle
│                                                             │
│ A4-E4: ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐         │ ← 4 stat cards
│         │+10 años│ │200+    │ │  4     │ │  98%   │         │
│         │Experien│ │Proyectos│ │Servic. │ │Satisfac│         │ fondo cyan-500/10
│         └────────┘ └────────┘ └────────┘ └────────┘         │ texto blanco
│                                                             │
│ A6: KPIs por servicio                                       │ ← H1
│                                                             │
│     A7:  Servicio  │ B7:  Proyectos │ C7:  Ingresos │ D7:  Margen │ ← header cyan
│    ───────────────────────────────────────────────────────  │
│     IoT            │   45          │  $45,000      │  32%        │ ← slate-800
│     ECU            │   60          │  $48,000      │  35%        │ ← slate-900
│     Automatización │   30          │  $60,000      │  28%        │ ← slate-800
│     Programación   │   50          │  $50,000      │  40%        │ ← slate-900
│                                                             │
│ A14: Gráfico de barras                                      │
│ A15-H28: [Gráfico nativo Excel]                              │ ← con colores cyan/purple/etc
│                                                             │
│ Footer: "IoT Tech · Electrocontrol · contacto..."           │
└────────────────────────────────────────────────────────────┘
```

---

## Gráficos

Excel permite gráficos nativos. Configura los colores de marca:

### Gráfico de barras / columnas

| Serie | Color | HEX |
|---|---|---|
| Serie 1 (principal) | Cyan | `#06B6D4` |
| Serie 2 | Purple | `#A855F7` |
| Serie 3 | Pink | `#EC4899` |
| Serie 4 | Green | `#22C55E` |
| Serie 5 | Orange | `#F97316` |
| Eje X | Blanco (dark) / Slate-900 (light) | — |
| Eje Y | Slate-400 | `#94A3B8` |
| Fondo del gráfico | Transparente (deja ver el fondo de la hoja) | — |
| Título | Inter/Calibri Bold, 14pt, blanco o slate-900 | — |
| Labels | Inter/Calibri Regular, 9pt, slate-300 o slate-500 | — |
| Leyenda | Mismos colores que series, fondo transparente | — |
| Bordes | Ninguno (limpiar bordes predeterminados) | — |

### Gráfico circular (pie)

Usar solo 2-4 categorías. Colores cyan, purple, pink, green. Labels fuera del pie, leader lines slate-400.

### Gráfico de línea

- Línea: 2.5pt, cyan-500
- Marcadores: circulares, 6pt, cyan-500 con borde blanco
- Área bajo la línea: gradient fill cyan-500 al 20% de opacidad (si la versión lo soporta)

---

## Formato condicional

Excel permite formatear celdas automáticamente según su valor. Usa los colores de marca:

| Condición | Formato |
|---|---|
| Valor > meta | Fondo `cyan-500/20`, texto blanco, bold |
| Valor = meta | Fondo `cyan-500/10`, texto blanco |
| Valor < meta | Fondo `slate-700/30`, texto slate-400 |
| Valor crítico (alto) | Fondo `pink-500/20`, texto pink-400 |
| Valor crítico (bajo) | Fondo `orange-500/20`, texto orange-400 |
| Tasa de crecimiento > 0 | Icono ↑ verde (`#22C55E`) |
| Tasa de crecimiento < 0 | Icono ↓ rojo (`#EF4444`) |
| Estado "Completado" | Fondo `green-500/20`, texto `green-400` |
| Estado "En progreso" | Fondo `cyan-500/20`, texto `cyan-400` |
| Estado "Pendiente" | Fondo `slate-500/20`, texto `slate-400` |
| Estado "Bloqueado" | Fondo `red-500/20`, texto `red-400` |

---

## Header / footer de impresión

Configurar en `Configurar página > Encabezado y pie de página`:

### Header
```
&"Inter,Bold"&12 IoT Tech · Electrocontrol         &[Fecha]
&"Inter,Regular"&10 http://pag.electrocontrol.cloud/
```

(alineado izquierda la marca, derecha la fecha)

### Footer
```
&"Inter,Regular"&9 Malkom Cordoba · +507 6250-9318          &Pág. &P de &N
```

(alineado izquierda contacto, derecha número de página)

---

## Imágenes y logos

- **Logo principal:** insertar en `A1`, altura ~60-80px
- **Para dashboard dark:** usar la versión original (fondo navy del logo se confunde con el dark)
- **Para hoja light:** usar la versión light (con fondo blanco) o PNG transparente
- **Posición:** esquina superior izquierda, padding 8px

**Para insertar el logo:**
```python
# usando openpyxl
from openpyxl.drawing.image import Image
from openpyxl import load_workbook
wb = load_workbook("archivo.xlsx")
ws = wb.active
img = Image("ruta/al/logo.png")  # convertir a PNG primero
img.width = 120  # px
img.height = 120
ws.add_image(img, "A1")
wb.save("archivo.xlsx")
```

---

## Vista protegida y validación

Para celdas de input:
- **Protección de hoja:** Revisar > Proteger hoja
- **Validación de datos:** Datos > Validación de datos
  - Listas desplegables: usar los 4 servicios de Electrocontrol
  - Rangos: fechas válidas, números positivos, etc.
- **Comentarios:** insertar tooltips explicativos con el ícono de info de Excel

---

## Gráficos sparkline

Los **sparklines** (mini gráficos en celda) son perfectos para dashboards compactos:

- Línea: cyan-500
- Columnas: cyan-500 (positivas), orange-500 (negativas)
- Win/Loss: green-500 / red-500

Insertar en: `Insertar > Sparkline > Línea/Columna/Perdido/Ganado`

---

## Recursos

- **Logo:** `assets/logo-electrocontrol.jpg` (convertir a PNG si se necesita)
- **Skill complementaria:** `ofimatica` (cargar ANTES — usar `scripts/recalc.py` para fórmulas)
- **Iconos:** no aplicables directamente, pero Lucide SVG puede convertirse a PNG

---

## Checklist antes de entregar

- [ ] ¿Fórmulas recalculadas con `scripts/recalc.py`?
- [ ] ¿Tema de color aplicado?
- [ ] ¿Header cyan en todas las tablas?
- [ ] ¿Zebra striping en filas de datos?
- [ ] ¿Fila de total con formato destacado?
- [ ] ¿Gráficos con colores de marca?
- [ ] ¿Logo insertado?
- [ ] ¿Header/footer de impresión configurados?
- [ ] ¿Datos de contacto correctos en header/footer?
- [ ] ¿Hojas protegidas si tiene celdas de input?
- [ ] ¿Tamaño de archivo razonable? (<2MB idealmente)
- [ ] ¿PDF de respaldo generado? (Archivo > Guardar como > PDF)
