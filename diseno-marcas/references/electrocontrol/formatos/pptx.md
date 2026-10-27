# Aplicación del diseño Electrocontrol a PowerPoint (.pptx)

Guía para crear presentaciones PowerPoint con el sistema de diseño de IoT Tech / Electrocontrol. **Esta skill NO reemplaza la skill `pptx`** — la complementa. Carga ambas: `pptx` para la mecánica + `diseno-electrocontrol` para el estilo.

---

## Regla de carpetas de trabajo (OBLIGATORIA)

Antes de crear cualquier .pptx, crea una carpeta temporal dedicada:

```bash
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
WORKDIR=".tmp/pptx-electrocontrol-$TIMESTAMP"
mkdir "$WORKDIR"
# Copia assets de la marca al workdir
cp "<base-dir-skill>/assets/logo-electrocontrol.jpg" "$WORKDIR/"
```

Trabaja SIEMPRE dentro de `WORKDIR`. Al terminar, copia el `.pptx` final a la carpeta destino del usuario. La carpeta temporal puede borrarse después (preguntar antes).

---

## Tema base (theme.xml)

PowerPoint permite definir colores, fuentes y efectos a nivel de tema. Configura así:

### Colores del tema (theme1.xml → `<a:clrScheme>`)

```xml
<a:clrScheme name="Electrocontrol">
  <a:dk1>      <!-- Texto principal (oscuro) — sobre fondos claros -->
    <a:srgbClr val="FFFFFF"/>  <!-- Blanco (porque el tema es dark) -->
  </a:dk1>
  <a:lt1>      <!-- Fondo (claro) — es nuestro fondo dark -->
    <a:srgbClr val="0F172A"/>  <!-- Slate 900 -->
  </a:lt1>
  <a:dk2>      <!-- Texto secundario oscuro -->
    <a:srgbClr val="CBD5E1"/>  <!-- Slate 300 -->
  </a:dk2>
  <a:lt2>      <!-- Fondo alterno -->
    <a:srgbClr val="1E293B"/>  <!-- Slate 800 -->
  </a:lt2>
  <a:accent1>  <!-- Acento 1: Cyan 500 -->
    <a:srgbClr val="06B6D4"/>
  </a:accent1>
  <a:accent2>  <!-- Acento 2: Purple 500 -->
    <a:srgbClr val="A855F7"/>
  </a:accent2>
  <a:accent3>  <!-- Acento 3: Pink 500 -->
    <a:srgbClr val="EC4899"/>
  </a:accent3>
  <a:accent4>  <!-- Acento 4: Blue 500 (servicio IoT) -->
    <a:srgbClr val="3B82F6"/>
  </a:accent4>
  <a:accent5>  <!-- Acento 5: Orange 500 (servicio ECU) -->
    <a:srgbClr val="F97316"/>
  </a:accent5>
  <a:accent6>  <!-- Acento 6: Green 500 (servicio Automatización) -->
    <a:srgbClr val="22C55E"/>
  </a:accent6>
  <a:hlink>    <!-- Link -->
    <a:srgbClr val="22D3EE"/>  <!-- Cyan 400 -->
  </a:hlink>
  <a:folHlink> <!-- Link visitado -->
    <a:srgbClr val="C084FC"/>  <!-- Purple 400 -->
  </a:folHlink>
</a:clrScheme>
```

### Fuentes del tema

```xml
<a:fontScheme name="Electrocontrol">
  <a:majorFont>  <!-- Títulos (headings) -->
    <a:latin typeface="Inter"/>
    <a:ea typeface=""/>
    <a:cs typeface=""/>
  </a:majorFont>
  <a:minorFont>  <!-- Body -->
    <a:latin typeface="Inter"/>
    <a:ea typeface=""/>
    <a:cs typeface=""/>
  </a:minorFont>
</a:fontScheme>
```

**Si Inter no está disponible en el sistema, PowerPoint usará Calibri por defecto** (que es muy similar). Para máxima fidelidad, instala Inter antes de empezar.

---

## Slide master (diseño de fondo)

### Diapositiva master (SlideMaster)

- **Fondo:** degradado diagonal de `#0F172A` → `#1E293B` → `#0F172A` (simular con un rectángulo de fondo que ocupe toda la slide y aplicar degradado)
- **Decoración:** 2 blobs difuminados (cyan y purple) en esquinas opuestas
- **Header:** logo pequeño en esquina superior izquierda
- **Footer:** número de página (cyan-400) + texto "IoT Tech · Electrocontrol" en slate-500

### Layouts estándar

| Layout | Uso | Contenido |
|---|---|---|
| **Portada** | Slide 1 | Fondo degradado, logo centrado, título con degradado cyan→purple→pink, subtítulo, línea accent |
| **Contenido** | Slides 2-N | Título H2 (blanco o con degradado), contenido (cards de glass), footer |
| **Dos columnas** | Comparativas, antes/después | Título arriba, 2 columnas con cards |
| **Imagen + texto** | Servicios, productos | Imagen a un lado, texto con bullets a otro |
| **Cita destacada** | Frase importante, testimonio | Fondo degradado, cita grande con degradado, autor |
| **Cierre/CTA** | Última slide | Logo + "Contáctanos" + datos (tel, email, web, WhatsApp) + QR |

---

## Especificaciones de slide (16:9, 1280x720 px)

### Slide 1 — Portada

```
[ Fondo: degradado slate-900 → slate-800 → slate-900 ]
[ Blobs: cyan top-left, purple bottom-right, blur 64px, opacidad 10% ]

     [LOGO ELECTROCONTROL — 200x200, centrado]

     ╔══════════════════════════════════════╗
     ║  TÍTULO DE LA PRESENTACIÓN           ║  ← Degradado cyan→purple→pink
     ║  (Inter Bold, 60pt)                  ║     text-fill gradient
     ╚══════════════════════════════════════╝

     Subtítulo descriptivo
     (Inter Regular, 24pt, slate-300)

     ═════════════════  ← Línea 60x4px con degradado cyan→purple

     [ Nombre del cliente / Fecha / Versión ]
```

### Slide de contenido

```
[ Fondo: slate-900 sólido ]
[ Header: logo pequeño (40x40) + breadcrumb opcional ]

     TÍTULO DE LA SECCIÓN                            ← H2, 40pt, blanco
     ════                                            ← Línea 40x3px cyan-500
                                                     (espacio 16px)

     ┌──────────────────────────────────────────────┐
     │                                              │
     │   Contenido de la slide (texto,             │  ← Card con
     │   bullets, cards, tablas)                    │     bg-slate-800/50
     │                                              │     border slate-700/50
     │                                              │     rounded-2xl
     └──────────────────────────────────────────────┘

[ Footer: "IoT Tech · Electrocontrol" slate-500 | "2" cyan-400 ]
```

### Slide de servicios (4 cards)

```
[ Fondo: slate-900 ]

     NUESTROS SERVICIOS                              ← H2 blanco
     Soluciones integrales...                        ← Subtítulo slate-400

     ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐
     │ [icono]    │  │ [icono]    │  │ [icono]    │  │ [icono]    │
     │ (gradient) │  │ (gradient) │  │ (gradient) │  │ (gradient) │
     │            │  │            │  │            │  │            │
     │ IoT        │  │ ECU        │  │ Automatiz. │  │ Program.   │
     │            │  │            │  │            │  │            │
     │ Texto...   │  │ Texto...   │  │ Texto...   │  │ Texto...   │
     │ ✓ feature  │  │ ✓ feature  │  │ ✓ feature  │  │ ✓ feature  │
     │ ✓ feature  │  │ ✓ feature  │  │ ✓ feature  │  │ ✓ feature  │
     └────────────┘  └────────────┘  └────────────┘  └────────────┘
       cyan→blue     orange→red   green→emerald  purple→pink
```

### Slide de cierre / CTA

```
[ Fondo: degradado slate-900 → slate-800 ]

     ¿LISTO PARA TRANSFORMAR TU NEGOCIO?            ← Degradado cyan→purple→pink

     [LOGO]

     📞 +507 6250-9318
     📧 contacto (ver branding.md)
     🌐 http://pag.electrocontrol.cloud/
     💬 https://wa.me/50762509318
```

---

## Aplicar degradados en PowerPoint

PowerPoint **SÍ soporta gradient fill** en formas y texto.

### Degradado en texto (signature)

1. Selecciona el texto
2. **Formato de texto** → **Relleno de texto** → **Degradado**
3. Configura 3 stops:
   - Stop 1: `#22D3EE` (cyan-400) — posición 0%
   - Stop 2: `#C084FC` (purple-400) — posición 50%
   - Stop 3: `#F472B6` (pink-400) — posición 100%
4. Ángulo: 0° (horizontal, left to right)
5. **Truco:** en PowerPoint el degradado en texto se ve un poco diferente al web. Si el resultado no es convincente, usa una imagen PNG con el texto pre-renderizado con el degradado (exporta desde Figma/Canva).

### Degradado en formas (botones, cards)

1. Selecciona la forma
2. **Formato de forma** → **Relleno** → **Degradado**
3. Configura los stops según el color de servicio

### Degradado en fondo de slide

1. **Diseño** → **Formato del fondo** → **Relleno** → **Degradado**
2. Para slate-900 → slate-800 → slate-900: 3 stops con el color del medio más claro
3. Aplicar a "Todas las diapositivas"

---

## Tipos de gráficos (para PPTX)

PowerPoint permite gráficos nativos. Aplica los colores de marca:

| Serie | Color |
|---|---|
| Serie 1 (primaria) | `#06B6D4` cyan-500 |
| Serie 2 | `#A855F7` purple-500 |
| Serie 3 | `#EC4899` pink-500 |
| Serie 4 | `#22C55E` green-500 |
| Serie 5 | `#F97316` orange-500 |
| Eje / labels | `#94A3B8` slate-400 |
| Fondo del gráfico | transparente (deja ver el slate-900) |
| Títulos | blanco, Inter Bold |
| Texto | slate-300, Inter Regular |

Para **degradados en barras/áreas**, PowerPoint permite gradient fill en series individuales.

---

## Iconos

PowerPoint tiene iconos propios pero son limitados. Opciones:

1. **Iconos SVG inlineados** — convertir SVG a PNG con `magick` y pegar como imagen
2. **Lucide icons** — bajar de [lucide.dev](https://lucide.dev) en SVG, convertir a PNG transparente
3. **PowerPoint native icons** — usar los de la pestaña "Insertar > Iconos", cambian a color cyan-500 con formato

**Recomendación:** descargar iconos Lucide relevantes del sitio:
- Wifi (IoT)
- Car (ECU)
- Settings (Automatización)
- Code (Programación)
- Mail, Phone, MapPin (Contacto)
- Award, Briefcase, GraduationCap, User (Sobre Mí)

Convertir a PNG 96x96 con fondo transparente y pegar.

---

## Imágenes y fotos

Si necesitas fotos, las mejores fuentes:
- [unsplash.com](https://unsplash.com) — buscar "IoT", "automotive", "automation", "programming", "circuit board"
- [pexels.com](https://pexels.com) — alternativa

Aplicar **overlay con degradado** encima para mantener la estética dark:
- Capa 1: foto (opacidad 100%)
- Capa 2: rectángulo negro al 30-50% de opacidad, O un degradado con el color de servicio al 20% de opacidad

---

## Animaciones (opcional, no abusar)

- **Entrada:** Fade (250ms) o Slide Up (350ms)
- **Énfasis:** Pulse (para iconos de check, badges de estado)
- **Salida:** Fade Out
- **NO usar:** transiciones 3D, rotaciones, "efectos especiales"

Mantén las animaciones **sutiles y profesionales**. La marca es tecnológica, no infantil.

---

## Exportación

Para mejor calidad:
- **PDF:** Archivo → Guardar como → PDF (mantiene colores y degradados)
- **Imágenes PNG:** Archivo → Exportar → Cambiar tipo de archivo → PNG (cada slide)
- **PowerPoint Show (.ppsx):** para presentar sin abrir PowerPoint

**Resolución recomendada:** 1920x1080 si vas a usar en pantalla grande; 1280x720 si es estándar.

---

## Plantilla base recomendada

Si vas a crear muchas presentaciones, vale la pena crear una **plantilla .potx** con:

1. Slide master con fondo degradado
2. 6-8 layouts predefinidos
3. Theme con colores y fuentes Electrocontrol
4. Logo en header
5. Footer con número de página y marca
6. Cards, botones y elementos decorativos ya formateados

Una vez creada, duplica la plantilla y solo cambia contenido para cada presentación nueva.

---

## Recursos en esta skill

- **Logo:** `assets/logo-electrocontrol.jpg`
- **Iconos Lucide:** descargar desde [lucide.dev](https://lucide.dev) según necesidad
- **Photos:** descargar de Unsplash/Pexels
- **Skill complementaria:** `pptx` (cargar ANTES de esta skill)

---

## Checklist antes de entregar

- [ ] ¿Fondo dark en TODAS las slides? (no mezclar con blanco)
- [ ] ¿Degradado cyan→purple→pink en H1 y máximo 1 H2?
- [ ] ¿Logo en header o portada?
- [ ] ¿Datos de contacto correctos? (+507 6250-9318, web, WhatsApp)
- [ ] ¿Información técnica correcta? (Malkom Córdoba, +10 años, 200+ proyectos)
- [ ] ¿Colores de servicio respetados? (IoT cyan, ECU orange, etc.)
- [ ] ¿Esquinas redondeadas en cards? (no esquinas rectas)
- [ ] ¿Tipografía consistente? (Inter o Calibri, bold para títulos)
- [ ] ¿Footer con número de página y marca?
- [ ] ¿Animaciones sutiles o ninguna?
