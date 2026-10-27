# Aplicación del diseño Electrocontrol a Word (.docx)

Guía para crear documentos Word con el sistema de diseño de IoT Tech / Electrocontrol. **Esta skill NO reemplaza la skill `docx`** — la complementa. Carga ambas.

---

## Regla de carpetas de trabajo (OBLIGATORIA)

```bash
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
WORKDIR=".tmp/docx-electrocontrol-$TIMESTAMP"
mkdir "$WORKDIR"
cp "<base-dir-skill>/assets/logo-electrocontrol.jpg" "$WORKDIR/"
```

Trabaja dentro de `WORKDIR`. Genera el `.docx` ahí y cópialo al destino al terminar.

---

## Cuándo usar dark mode vs. light mode

| Documento | Modo | Razón |
|---|---|---|
| **Cotización / propuesta formal** | **Light** (fondo blanco) | Estándar de negocios, imprimible |
| **Factura** | **Light** (fondo blanco) | Requerimiento legal/fiscal |
| **Reporte técnico** | **Light** (fondo blanco) | Imprimible, lectura en papel |
| **Contrato** | **Light** (fondo blanco) | Legal, imprimible |
| **Manual interno** | Light (con acentos de marca) | Imprimible, profesional |
| **White paper / dossier** | **Dark** (modo presentación) | Pieza de marketing |
| **Newsletter interno** | **Dark** (presentación) | Engagement |
| **One-pager promocional** | **Dark** (marketing) | Pieza de captación |
| **Currículum / portafolio** | Light con header dark | Profesional + personal |

**Regla:** si el documento se va a imprimir o enviar formalmente → **light**. Si es pieza de marketing o presentación → **dark**.

---

## Estilos de párrafo y carácter (styles.xml)

Word se basa en estilos. Define estos estilos personalizados con la nomenclatura `Electrocontrol X`:

### Estilos de párrafo

| Estilo | Fuente | Tamaño | Color | Peso | Alineación | Uso |
|---|---|---|---|---|---|---|
| `Electrocontrol Title` | Inter | 32pt | `#0F172A` (light) o `#FFFFFF` (dark) | Bold | Centro o izquierda | Título principal del documento |
| `Electrocontrol Subtitle` | Inter | 18pt | `#64748B` slate-500 | Regular | Centro | Subtítulo / fecha |
| `Electrocontrol H1` | Inter | 24pt | `#0F172A` / `#FFFFFF` | Bold | Izquierda | Encabezado nivel 1 |
| `Electrocontrol H2` | Inter | 18pt | `#06B6D4` cyan-500 | Bold | Izquierda | Encabezado nivel 2 (con color de marca) |
| `Electrocontrol H3` | Inter | 14pt | `#0F172A` / `#FFFFFF` | Semibold | Izquierda | Encabezado nivel 3 |
| `Electrocontrol Body` | Inter | 11pt | `#1E293B` slate-800 (light) / `#CBD5E1` slate-300 (dark) | Regular | Justificado | Párrafo normal |
| `Electrocontrol Quote` | Inter | 12pt | `#A855F7` purple-500 | Italic | Centro | Cita destacada |
| `Electrocontrol Caption` | Inter | 9pt | `#64748B` slate-500 | Regular | Centro | Caption de imagen |

### Estilos de carácter

| Estilo | Aplicación | Color | Peso |
|---|---|---|---|
| `Electrocontrol Accent` | Texto destacado inline | `#06B6D4` cyan-500 | Bold |
| `Electrocontrol Number` | Cifras grandes (+10 años, 200+) | `#06B6D4` | Bold, 16pt |

---

## Configuración de página

| Parámetro | Valor | Notas |
|---|---|---|
| **Tamaño** | A4 (21cm x 29.7cm) | Estándar Panamá/Latinoamérica |
| **Orientación** | Vertical (Portrait) | Horizontal solo para landscape/diagramas |
| **Márgenes** | Superior 2.5cm, Inferior 2.5cm, Izq 2.5cm, Der 2.5cm | Estándar corporativo |
| **Header** | Logo a la izquierda + título a la derecha | Repetir en todas las páginas |
| **Footer** | "IoT Tech · Electrocontrol" izquierda, página X de Y derecha | Repetir en todas las páginas |
| **Numeración** | Empezar en 1 | Estándar |

---

## Estructura típica de documentos

### Cotización / Propuesta comercial

```
┌────────────────────────────────────────────────┐
│ [LOGO]                                  Fecha  │  ← Header
│────────────────────────────────────────────────│
│                                                │
│  PROPUESTA COMERCIAL                            │  ← Title, 32pt, bold
│  Cliente: {{nombre}}                            │  ← Subtitle
│  Referencia: PROP-2026-001                      │
│  Fecha: {{fecha}}                               │
│                                                │
│  ════════════════════════════                   │  ← Línea accent cyan
│                                                │
│  1. INTRODUCCIÓN                                │  ← H1
│  Texto introductorio sobre Electrocontrol,     │  ← Body
│  experiencia, servicios...                      │
│                                                │
│  2. OBJETIVO DEL PROYECTO                       │  ← H1
│  2.1 Objetivo general                          │  ← H2 (cyan)
│  2.2 Objetivos específicos                      │
│                                                │
│  3. ALCANCE                                    │  ← H1
│  • IoT & Desarrollo Tecnológico                │  ← Bullet
│  • Reparación de ECU                           │
│  • Automatización Industrial                   │
│  • Programación                                │
│                                                │
│  4. INVERSIÓN                                  │  ← H1
│  ┌──────────────────────────────────────────┐  │
│  │ Item      │ Cantidad │ Precio │ Total   │  │  ← Tabla con header cyan
│  ├──────────────────────────────────────────┤  │
│  │ Servicio1 │    1     │  $X    │   $X    │  │
│  │ Servicio2 │    1     │  $X    │   $X    │  │
│  └──────────────────────────────────────────┘  │
│  Total: $X,XXX.XX                              │  ← Bold, 14pt
│                                                │
│  5. PLAZOS                                     │
│  ...                                            │
│                                                │
│  6. DATOS DE CONTACTO                          │
│  Malkom Daniel Cordoba                          │
│  📞 +507 6250-9318                             │
│  🌐 http://pag.electrocontrol.cloud/           │
│  💬 https://wa.me/50762509318                  │
│                                                │
│────────────────────────────────────────────────│
│ IoT Tech · Electrocontrol        Página 1 de 5  │  ← Footer
└────────────────────────────────────────────────┘
```

### Factura

```
┌────────────────────────────────────────────────┐
│ [LOGO]                              FACTURA N° │  ← Header
│────────────────────────────────────────────────│  FECHA: 2026-XX-XX
│                                                │
│  FACTURA: FAC-2026-001                         │  ← Title
│                                                │
│  EMISOR                  CLIENTE               │
│  IoT Tech                {{nombre}}            │
│  Panamá                  {{dirección}}         │
│  +507 6250-9318          {{RUC/ID}}            │
│                                                │
│  ┌──────────────────────────────────────────┐  │
│  │ # │ Descripción  │ Cant │ P.Unit │ Total │  │  ← Tabla
│  ├───┼──────────────┼──────┼────────┼───────┤  │
│  │ 1 │ Servicio A   │  1   │ $XXX   │ $XXX  │  │
│  │ 2 │ Servicio B   │  1   │ $XXX   │ $XXX  │  │
│  └───┴──────────────┴──────┴────────┴───────┘  │
│                                                │
│                            Subtotal: $XXX.XX  │
│                            ITBMS (7%): $XX.XX │
│                            ─────────────────  │
│                            TOTAL:    $XXX.XX │  ← 16pt, bold
│                                                │
│  Forma de pago: Transferencia / Yappy / Efectivo │
│                                                │
│────────────────────────────────────────────────│
│ ¡Gracias por su preferencia!                  │
│ IoT Tech · Electrocontrol        Página 1 de 1  │
└────────────────────────────────────────────────┘
```

### Reporte técnico (light mode)

```
┌────────────────────────────────────────────────┐
│ [LOGO]                                REF: XX  │
│────────────────────────────────────────────────│
│                                                │
│  REPORTE TÉCNICO                               │  ← Title
│  Servicio: Reparación de ECU                   │  ← Subtitle
│  Cliente: {{nombre}}                           │
│  Fecha: {{fecha}}                              │
│  Técnico: Malkom Daniel Cordoba                │
│                                                │
│  1. DIAGNÓSTICO                                │  ← H1
│  Diagnóstico realizado con escáner OBD-II...   │
│                                                │
│  2. TRABAJO REALIZADO                          │
│  2.1 Reprogramación de ECU                     │  ← H2 (cyan)
│  2.2 Reset de inmovilizador                    │
│                                                │
│  3. RESULTADOS                                 │
│  Pruebas funcionales OK...                     │
│                                                │
│  [Imagen 1]      [Imagen 2]                    │  ← Imágenes con caption
│  Antes           Después                       │
│                                                │
│  4. RECOMENDACIONES                            │
│  ...                                            │
│                                                │
│────────────────────────────────────────────────│
│ Firma técnico: _________________              │
│ IoT Tech · Electrocontrol        Página 1 de 3  │
└────────────────────────────────────────────────┘
```

### Dossier / White paper (dark mode)

```
┌────────────────────────────────────────────────┐
│ [FONDO DARK: #0F172A]                          │
│                                                │
│         [LOGO]                                 │
│                                                │
│  ╔══════════════════════════════════╗           │
│  ║  IoT EN PANAMÁ                  ║           │  ← Title, 36pt, gradient
│  ║  El futuro de la conectividad   ║           │
│  ╚══════════════════════════════════╝           │
│                                                │
│  White Paper · 2026                            │
│  Malkom Daniel Cordoba                         │
│                                                │
│  [Página siguiente]                            │
└────────────────────────────────────────────────┘

┌────────────────────────────────────────────────┐
│ [FONDO DARK]                                   │
│                                                │
│  Introducción                                  │  ← H1 blanco
│  ─────                                         │  ← Línea cyan
│                                                │
│  Panamá está experimentando una revolución     │  ← Body slate-300
│  tecnológica sin precedentes. La adopción de   │
│  IoT en sectores industriales...               │
│                                                │
│  ┌──────────────────────────────────────────┐  │
│  │ +10 años  │  200+   │  4 servicios      │  │  ← Card con stat
│  │ experiencia│ proyectos│ principales      │  │
│  └──────────────────────────────────────────┘  │
│                                                │
└────────────────────────────────────────────────┘
```

---

## Tablas

Las tablas son la parte más customizable. Configura:

### Tabla "servicio / cantidad / precio"

| Elemento | Estilo |
|---|---|
| **Header row** | Fondo `cyan-500` (#06B6D4), texto blanco bold, padding 6px |
| **Body rows** | Fondo alterno: blanco / `#F1F5F9` slate-100 (light) o `#1E293B` slate-800 / `#0F172A` slate-900 (dark) |
| **Bordes** | `#CBD5E1` slate-300 (light) o `#334155` slate-700 (dark), 0.5pt |
| **Total row** | Fondo `cyan-500/10` o `#E0F2FE` (light), texto bold, 14pt |
| **Alineación números** | Derecha |
| **Alineación texto** | Izquierda |

**Para dark mode:** el header de la tabla debe ser cyan-500 (sólido) para mantener legibilidad. El resto con fondos slate-800/900 alternos.

---

## Imágenes y figuras

| Regla | Cómo |
|---|---|
| Caption | Estilo "Electrocontrol Caption", 9pt, slate-500, centrado |
| Alineación | Centrado en la página |
| Borde | Sutil: 1px `#E2E8F0` slate-200 (light) o `#334155` slate-700 (dark) |
| Tamaño | Máximo 80% del ancho de página |
| Logo en header | 25mm de alto, alineado a la izquierda |

---

## Numeración de páginas y header/footer

### Header (todas las páginas excepto portada)

```
[LOGO 25mm]   [Texto del documento]              [Fecha]
```

### Footer (todas las páginas)

```
IoT Tech · Electrocontrol · http://pag.electrocontrol.cloud/    Página X de Y
```

Configurar:
- **Diferente primera página:** SÍ (la portada no tiene header/footer)
- **Alineación:** izquierda para texto de marca, derecha para número de página
- **Fuente:** Inter 9pt slate-500
- **Línea separadora:** 0.5pt `#E2E8F0` (light) o `#334155` (dark), solo arriba del footer

---

## Degradados en Word

Word **NO soporta degradados de fondo en párrafos** directamente. Opciones:

1. **Cuadro de texto con relleno degradado** — Insertar > Cuadro de texto > Formato > Relleno degradado
2. **WordArt con degradado** — Insertar > WordArt, editar el formato del texto para aplicar degradado
3. **Imagen pre-renderizada** — Exportar el texto con degradado como PNG desde Figma/Canva e insertar como imagen
4. **Forma con degradado** — Insertar > Formas > Rectángulo, aplicar degradado al relleno

**Recomendación:** para títulos con degradado signature (cyan→purple→pink), usa la opción 3 (imagen PNG pre-renderizada). Es la más confiable.

---

## Conversión desde PowerPoint / Canva / Figma

Si ya tienes un diseño en otra herramienta y lo pasas a Word:

1. **Desde PowerPoint:** Archivo > Exportar > Crear handouts > Páginas de notas (mantiene diseño)
2. **Desde Canva:** Compartir > Descargar > PDF Print, luego convierte PDF a Word con Adobe Acrobat
3. **Desde Figma:** Exporta cada página como PNG, insértalas en Word como imágenes
4. **Word permite insertar PDFs como objetos** — el formato se mantiene, pero no es editable

---

## Recursos

- **Logo:** `assets/logo-electrocontrol.jpg`
- **Skill complementaria:** `docx` (cargar ANTES)
- **Iconos:** descargar de [lucide.dev](https://lucide.dev) e insertar como PNG
- **Imágenes:** Unsplash, Pexels (tema: IoT, automotive, automation, code)

---

## Checklist antes de entregar

- [ ] ¿Estilos personalizados aplicados consistentemente?
- [ ] ¿Header con logo en todas las páginas (excepto portada)?
- [ ] ¿Footer con número de página y marca?
- [ ] ¿Datos de contacto correctos?
- [ ] ¿Datos de Malkom Córdoba correctos? (sin tildes inventadas)
- [ ] ¿Colores de marca en acentos? (cyan, purple, pink)
- [ ] ¿Tablas con header cyan si es light, slate-800 si es dark?
- [ ] ¿Imágenes con caption y borde sutil?
- [ ] ¿Tamaño de archivo razonable? (<5MB idealmente)
- [ ] ¿PDF de respaldo generado?
