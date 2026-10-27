# Logo ITSE — Guía de Uso

---

## 🚨 REGLA: Logo del ITSE ARRIBA en portadas

> **El logo del ITSE SIEMPRE va en la parte SUPERIOR de toda portada
> institucional (PPTX, DOCX, PDF, posters, banners, tarjetas, diplomas,
> diplomas digitales, etc.) — NUNCA en el centro vertical, NUNCA debajo
> del título.** El logo preside la composición.

- **Portadas de cualquier formato:** Logo en el TOP (header o parte superior de la página/slide)
- **Documentos con varias páginas / slides de contenido:** Logo en el header (esquina superior izquierda)
- **Diplomas y certificados:** Logo en el TOP centrado
- **Iconos pequeños (24–48 px):** No llevan el logo completo; usan los iconos institucionales

---

## Variantes disponibles

Esta skill incluye 3 variantes del logo PNG (descargadas del sitio oficial):

| Archivo | Dimensiones aprox. | Uso |
|---|---|---|
| `assets/logo-itse-horizontal.png` | ~270 × 75 px | **Header principal**, slides, documentos (uso general) |
| `assets/logo-itse-vertical.png` | ~150 × 80 px | Móviles, espacios verticales estrechos, firmas |
| `assets/logo-itse-footer.png` | ~280 × 75 px | Pie de página, áreas oscuras (footer) |

⚠️ **Para uso en impresión de alta calidad** (offset, gran formato, vallas), se recomienda obtener los archivos vectoriales (SVG/AI/EPS) directamente del ITSE. Estos PNG son para uso digital estándar.

---

## Anatomía del logo

El logo del ITSE consta de:
1. **Acrónimo "ITSE"** en tipografía bold sans-serif
2. **Línea divisoria** sutil
3. **Tagline "DE CICLO CORTO"** debajo
4. **Acento de color:** las letras "ITSE" usan una combinación de negro/gris con acento dorado o detalles destacados

**No recargues ni modifiques**:
- ❌ NO cambies los colores del logo
- ❌ NO cambies la tipografía
- ❌ NO agregues sombras, brillos o efectos
- ❌ NO estires ni deformes las proporciones
- ❌ NO agregues el logo dentro de un círculo/forma a menos que sea una variante oficial

---

## Zona de seguridad

Mantén un área libre alrededor del logo equivalente a la **altura de la "I"** del acrónimo. En esta zona no debe haber texto, otros logos ni elementos gráficos.

```
┌──────────────────────────┐
│                          │  ← espacio superior
│   ┌──────────────┐       │
│   │              │       │
│   │   ITSE       │       │  ← altura de I
│   │   DE CICLO   │       │  ← espacio lateral
│   │   CORTO      │       │
│   └──────────────┘       │
│                          │  ← espacio inferior
└──────────────────────────┘
```

---

## Tamaño mínimo

| Variante | Tamaño mínimo (alto) |
|---|---|
| Horizontal | 24 px / 6 mm |
| Vertical | 32 px / 8 mm |
| Footer | 24 px / 6 mm |

Por debajo de este tamaño el tagline "DE CICLO CORTO" se vuelve ilegible.

---

## Colores de fondo permitidos

| Fondo | Logo a usar | Notas |
|---|---|---|
| Blanco (`#FFFFFF`) | Horizontal o Footer | **El más común** — usar por defecto |
| Gris claro (`#F7F7F7`) | Horizontal o Footer | OK en secciones alternas |
| Gris carbón (`#424242`) | Footer (preferido) | Para fondos oscuros — el footer tiene mejor contraste |
| Dorado (`#FFB000`) | NO recomendado | El logo no contrasta bien sobre dorado |
| Imagen/foto | Horizontal con overlay blanco translúcido | Poner sobre `rgba(255,255,255,0.9)` |

---

## Posición en el diseño

### En headers (parte superior)

```
┌─────────────────────────────────────┐
│  [LOGO ITSE]              Menú...   │  ← esquina superior izquierda
│                                     │
│  Contenido...                       │
└─────────────────────────────────────┘
```

### En footers (parte inferior)

```
┌─────────────────────────────────────┐
│                                     │
│  Contenido...                       │
│                                     │
│  [LOGO ITSE]      © {año} ITSE       │  ← esquina inferior izquierda (año actual)
└─────────────────────────────────────┘
```

### En documentos (portada o primera página)

- **Portada:** Logo **ARRIBA** (parte superior de la página, alineado a la izquierda en el header o centrado arriba del título), tamaño grande (~50–70mm de ancho)
- **Documentos:** Logo en header + texto "Instituto Técnico Superior Especializado" debajo
- **Diapositivas:** Logo esquina superior IZQUIERDA, nunca centrado

### En presentaciones (PowerPoint)

- **Slide de título:** Logo **ARRIBA** (en el header del slide, alineado a la izquierda o centrado arriba), tamaño medio (~1.5–2 cm de alto) — NUNCA en el centro vertical
- **Slides de contenido:** Logo esquina superior IZQUIERDA, tamaño pequeño (1–1.2 cm de alto)
- **Slide final ("Gracias"):** Logo **ARRIBA** centrado, tamaño medio

---

## NO usar el logo para

- ❌ Patrones de fondo repetidos
- ❌ Marcas de agua (a menos que sea explícitamente oficial)
- ❌ Como parte de un texto (ej: "el ITSE creo que...")
- ❌ En colores personalizados
- ❌ Rotado o volteado
- ❌ Con otros elementos gráficos encima
- ❌ Recortado (mostrar solo parte)

---

## Variante oficial en SVG (si necesitas una versión vectorial limpia)

El ITSE no publica oficialmente un SVG editable, pero el logo PNG es suficiente para uso digital. Si necesitas un SVG editable, puedes:

1. Vectorizar el PNG con [Inkscape](https://inkscape.org/) o Adobe Illustrator (trazar bitmap)
2. Pedir al departamento de comunicación del ITSE el archivo maestro (recomendado para uso comercial o institucional oficial)

---

## Frase de identificación institucional

Cuando el logo aparece junto a texto, usa esta descripción oficial:

> **Instituto Técnico Superior Especializado (ITSE)**
> Educación superior de ciclo corto | Panamá

O simplemente:

> **ITSE — Instituto Técnico Superior Especializado**

---

## Ejemplo de header institucional

```html
<header style="background: white; padding: 16px 32px; border-bottom: 1px solid #AEAEAE;">
  <img src="assets/logo-itse-horizontal.png" 
       alt="ITSE - Instituto Técnico Superior Especializado" 
       style="height: 48px;">
</header>
```

---

## Ejemplo de footer institucional

```html
<footer style="background: #424242; color: white; padding: 32px;">
  <img src="assets/logo-itse-footer.png" 
       alt="ITSE" 
       style="height: 48px;">
  <p>© {año} Instituto Técnico Superior Especializado — Panamá</p>
  <!-- {año} = año actual -->
  <p>https://www.itse.ac.pa/</p>
</footer>
```
