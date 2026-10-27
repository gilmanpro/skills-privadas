# Logo — Uso correcto del logo Electrocontrol

El logo es el activo más importante de la marca. **Usa siempre el archivo correcto** y respeta las zonas de seguridad y tamaños mínimos.

---

## Assets disponibles en esta skill

| Archivo | Ubicación | Uso |
|---|---|---|
| `logo-electrocontrol.jpg` | `assets/logo-electrocontrol.jpg` | Logo original descargado del sitio (cuadrado, fondo dark navy, "e" naranja pixelada + "ELECTROCONTROL") |

**Limitación actual:** solo tenemos la versión JPG cuadrada con fondo. Para entregas profesionales se recomienda generar variantes adicionales (ver "Generar variantes" abajo).

---

## Variantes necesarias (cuando el material lo requiera)

| Variante | Descripción | Cuándo usarla |
|---|---|---|
| **Logo claro sobre dark** (actual) | Logo naranja sobre fondo navy | Web, slides, dashboards (modo dark) |
| **Logo claro sobre blanco** | Logo naranja sobre fondo blanco | Papelería impresa, facturas, propuestas formales |
| **PNG transparente** | Logo sin fondo (transparencia en lugar de navy) | Composiciones sobre fotos, fondos de color |
| **SVG vectorial** | Versión vectorial del logo | Cualquier uso a alta resolución, animación |
| **Favicon** | Versión 32x32 / 16x16 | Web (favicon) |
| **Monocromático blanco** | Logo en blanco puro | Sobre fondos muy oscuros o fotos coloridas |
| **Monocromático negro** | Logo en negro puro | Sobre fondos claros / impresión |

---

## Generar variantes

### 1. Versión PNG transparente

**Opción A — ImageMagick (rápido):**
```bash
magick assets/logo-electrocontrol.jpg -fuzz 5% -transparent "#0a1a2e" assets/logo-electrocontrol-transparente.png
```

**Opción B — remove.bg (mejor calidad):**
1. Sube `logo-electrocontrol.jpg` a [remove.bg](https://remove.bg)
2. Descarga la versión con fondo transparente
3. Guárdala como `assets/logo-electrocontrol-transparente.png`

**Opción C — Usando la skill `svg-logo-designer`:**
- Describe el logo: "Logo cuadrado con letra 'e' estilizada en color naranja (#FF5722) con efecto pixelado/glitch a la izquierda, texto 'ELECTROCONTROL' debajo en mayúsculas, fondo navy/dark"
- Exporta como SVG → convierte a PNG con cualquier herramienta

### 2. Versión SVG vectorial

Usa la skill **`svg-logo-designer`** con este prompt:

```
Crea un logo para "ELECTROCONTROL" basado en la siguiente descripción:
- Símbolo: letra "e" minúscula estilizada, color naranja (#FF5722), con efecto 
  pixelado/glitch en la parte izquierda (cuadrados de varios tamaños que salen 
  de la letra como si se estuviera "descomponiendo" hacia la izquierda).
- Texto: "ELECTROCONTROL" debajo en mayúsculas, tipografía sans-serif bold 
  con tracking amplio, color naranja (#FF5722).
- Fondo: azul oscuro navy (#0A1A2E), cuadrado.
- Estilo: tecnológico, industrial, futurista.
- Guarda como SVG y exporta también a PNG 800x800.
```

### 3. Versión sobre blanco (light)

Genera la variante light sobre el único asset real disponible (JPG):
```bash
magick assets/logo-electrocontrol.jpg -background white -flatten assets/logo-electrocontrol-light.png
```

> **Nota:** en `assets/` solo existe `logo-electrocontrol.jpg`; no hay `logo-electrocontrol.svg`. Para vectorizar hay que convertir primero: genera el SVG con `svg-logo-designer` (sección 2) o traza el JPG, y luego aplica el mismo comando sobre el `.svg` para cambiar solo el fondo. Si se ejecuta sobre el JPG directamente, el fondo navy queda incrustado; para una variante light limpia, parte del PNG transparente de la sección 1.

O pide directamente a `svg-logo-designer`:
```
Genera una variante del logo ELECTROCONTROL sobre fondo BLANCO con el 
mismo símbolo y texto naranja. Guarda como logo-electrocontrol-light.svg.
```

### 4. Favicon

```bash
magick assets/logo-electrocontrol.jpg -resize 32x32 assets/favicon-32.png
magick assets/logo-electrocontrol.jpg -resize 16x16 assets/favicon-16.png
```

O usar [favicon.io](https://favicon.io/) con el PNG transparente.

---

## Reglas de uso

### Tamaño mínimo

| Contexto | Tamaño mínimo |
|---|---|
| **Web (header)** | 40px de alto |
| **Web (footer)** | 32px de alto |
| **Print (A4, papelería)** | 25mm de ancho |
| **PowerPoint (slide)** | 80px de alto (evita que se vea pixelado) |
| **Documentos Word** | 30mm de ancho |
| **Favicon** | 16x16 / 32x32 px |

### Zona de seguridad (clear space)

Mantén una zona de seguridad alrededor del logo equivalente al **25% de la altura del símbolo** (la "e"). En esta zona no debe haber texto, otros logos, ni elementos gráficos.

```
[-------- zona de seguridad --------]
[                                    ]
[        +---+ zona libre            ]
[        | e |                       ]
[        +---+                       ]
[   ELECTROCONTROL                   ]
[                                    ]
[-------- zona de seguridad --------]
```

### Posición y alineación

| Material | Posición recomendada |
|---|---|
| Web (header) | Esquina superior izquierda, alineado a la izquierda |
| Web (footer) | Esquina superior izquierda de la columna 1 |
| Slide (portada) | Centro, arriba del título |
| Slide (contenido) | Esquina superior izquierda o esquina inferior derecha (discreto) |
| Documento Word | Header centrado o esquina superior izquierda |
| Tarjeta de presentación | Esquina superior izquierda |
| Email | Inline, alineado a la izquierda |
| Firma de email | 100-150px de ancho, alineada a la izquierda |

### NO HACER

- ❌ **No deformes** el logo (no estires ni comprimas)
- ❌ **No cambies los colores** del logo (la "e" SIEMPRE naranja #FF5722, el texto SIEMPRE naranja)
- ❌ **No gires** el logo
- ❌ **No pongas el logo sobre fondos que dificulten su lectura** (ej. fotos muy coloridas sin overlay oscuro)
- ❌ **No uses el logo con un tamaño menor al mínimo**
- ❌ **No crees versiones del logo** sin usar `svg-logo-designer` o una herramienta de diseño
- ❌ **No uses el logo blanco/negro** si no lo has generado explícitamente
- ❌ **No coloques el logo dentro de cards o botones** (es un símbolo de marca, no un icono)

### SÍ HACER

- ✅ Usa el logo en su versión original (cuadrada, fondo navy) por defecto
- ✅ Mantén la zona de seguridad
- ✅ Usa la versión light si el material tiene fondo blanco/claro
- ✅ Genera el PNG transparente para composiciones sobre fotos
- ✅ En slides oscuras: usa el logo tal cual (fondo navy del logo se confunde con el slide)
- ✅ En slides claras: usa la versión light

---

## Uso combinado con texto

Si necesitas mostrar el logo junto al nombre "IoT Tech" o "Electrocontrol":

**Opción 1 — Solo logo (recomendado):**
```
[LOGO ELECTROCONTROL]
Bienvenido a IoT Tech
```

**Opción 2 — Logo + texto lado a lado:**
```
[LOGO] | IoT Tech
       | Innovación y Tecnología
```

**Opción 3 — Logo + tagline debajo (formato landing):**
```
       [LOGO]
Innovación IoT & Tecnología Automotriz
```

El sitio web usa la opción 3 en el footer.

---

## Watermark / Marca de agua

Si necesitas un watermark para documentos PDF o imágenes, usa el logo blanco con opacidad 10-20% sobre el fondo, en tamaño grande (40-50% del área):

```css
.watermark {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  opacity: 0.1;
  width: 50%;
  pointer-events: none;
}
```

---

## Logo en redes sociales (avatares)

| Red social | Tamaño |
|---|---|
| Instagram (foto perfil) | 320x320 |
| Facebook (foto perfil) | 170x170 |
| LinkedIn (logo empresa) | 300x300 |
| X / Twitter (avatar) | 400x400 |
| WhatsApp Business (foto perfil) | 640x640 |
| YouTube (icono canal) | 800x800 |

**Recomendación:** usa la versión PNG transparente sobre fondo de color sólido (cyan-500 o navy).

---

## Última actualización

Logo descargado de http://pag.electrocontrol.cloud/logo.jpg en junio 2026.
Si Malkom actualiza el logo en la web, re-descárgalo y reemplaza el asset.
