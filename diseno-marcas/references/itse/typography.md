# Sistema Tipográfico — ITSE

Extraído del CSS oficial (https://www.itse.ac.pa/) en junio 2026.

---

## Familia tipográfica

```css
font-family: "Helvetica Neue", Inter, Helvetica, Arial, sans-serif;
```

**Reglas:**
- **Primera opción:** `Helvetica Neue` (sistema, presente en Mac/iOS y Windows moderno)
- **Segunda opción:** `Inter` (web open-source, muy similar a Helvetica, excelente en pantallas)
- **Fallbacks:** `Helvetica, Arial, sans-serif`

**Para web (HTML/CSS):** usa Inter (más legible en pantallas, disponible en Google Fonts).
**Para impresión (PDF/impresos):** usa Helvetica Neue o Arial.
**Para PowerPoint/Word:** usa Arial o Calibri como equivalente.

---

## Pesos disponibles

| Peso | Valor | Uso |
|---|---|---|
| Regular | 400 | Texto corrido, párrafos, body |
| Semi-bold | 500 | Subtítulos, labels destacados, navegación |
| Bold | 700 | Títulos, CTAs, números grandes |

⚠️ **NO uses pesos intermedios** (300 Light, 600 Semi-Bold distintos a 500). Mantén solo 3 pesos para coherencia.

---

## Escala tipográfica

La escala del ITSE está basada en rem (1rem = 16px).

| Nivel | Tamaño rem | Tamaño px | Peso | line-height | Uso típico |
|---|---|---|---|---|---|
| **H1** | 2.5rem | 40px | 700 | 60px (150%) | Título principal de página, hero, portada |
| **H2** | 2rem | 32px | 700 | 32px (100%) | Título de sección |
| **H3** | 1.5rem | 24px | 700 | 24px (100%) | Subtítulo, título de card |
| **H4** | 1.25rem | 20px | 700 | 24px (120%) | Subtítulo menor, título de item |
| **H5** | 1.125rem | 18px | 500 | 24px (133%) | Label destacado, navegación |
| **H6** | 1rem | 16px | 500 | 24px (150%) | Encabezado pequeño |
| **Párrafo** | 0.875rem | 14px | 400 | 24px (171%) | Body text, contenido general |
| **Small** | 0.75rem | 12px | 400 | 16px (133%) | Footnotes, captions, metadata |

**Observación importante:** El ITSE usa texto base de **14px** (no 16px como es estándar). Esto es porque su sitio web prioriza la densidad de información.

---

## Variables CSS oficiales

```css
:root {
  --font-h1: 2.5rem;
  --font-h2: 2rem;
  --font-h3: 1.5rem;
  --font-h4: 1.25rem;
  --font-h5: 1.125rem;
  --font-h6: 1rem;
  --font-p: 0.875rem;
  --font-small: 0.75rem;
  
  --font-weight-bold: 700;
  --font-weight-semi-bold: 500;
  --font-weight-regular: 400;
  
  --line-height: 100%;
  --letter-spacing: 0%;
}
```

---

## Aplicación por formato

### HTML / Web

```css
h1 { font-size: 2.5rem; font-weight: 700; line-height: 1.5; }
h2 { font-size: 2rem; font-weight: 700; line-height: 1; }
h3 { font-size: 1.5rem; font-weight: 700; line-height: 1; }
h4 { font-size: 1.25rem; font-weight: 700; line-height: 1.2; }
h5 { font-size: 1.125rem; font-weight: 500; line-height: 1.3; }
h6 { font-size: 1rem; font-weight: 500; line-height: 1.5; }
p { font-size: 0.875rem; font-weight: 400; line-height: 1.7; }
.small { font-size: 0.75rem; font-weight: 400; line-height: 1.3; }
```

### PowerPoint

Para presentaciones, escala los tamaños un poco hacia arriba (porque se ven a distancia):

| Nivel | Tamaño |
|---|---|
| Título de slide | 36-44 pt (bold) |
| Subtítulo | 28-32 pt (bold) |
| Contenido | 18-24 pt (regular) |
| Footer/nota | 12-14 pt (regular) |

**Tipografía:** Arial (presente en Office) o Calibri.

### Word / PDF

Usa los mismos tamaños rem convertidos a pt:

| Nivel | Tamaño pt |
|---|---|
| H1 | 32-40 pt |
| H2 | 26-32 pt |
| H3 | 20-24 pt |
| Párrafo | 11-12 pt |
| Small | 9-10 pt |

**Tipografía:** Arial o Calibri. (Word por defecto usa Calibri, que es perfectamente compatible con el sistema del ITSE).

### Excel

| Uso | Tamaño |
|---|---|
| Título del documento | 16-18 pt, bold |
| Encabezados de tabla | 11-12 pt, bold, fondo dorado #FFB000 |
| Datos | 10-11 pt, regular |
| Footer/notas | 8-9 pt, gris #7B7B7B |

---

## Colores de texto

| Uso | Color | HEX |
|---|---|---|
| Texto principal | Gris Carbón | `#424242` |
| Texto sobre fondo dorado | Blanco | `#FFFFFF` |
| Texto sobre fondo oscuro | Blanco | `#FFFFFF` |
| Texto secundario (labels, captions) | Gris 100 | `#7B7B7B` |
| Texto deshabilitado | Gris 200 | `#9D9D9C` |
| Texto invertido (oscuro sobre claro) | Negro puro | `#000000` (solo en casos extremos) |

**⚠️ NUNCA uses negro puro (#000000) como texto principal** — es demasiado agresivo. Usa siempre #424242.

---

## Espaciado y letter-spacing

```css
letter-spacing: 0%;  /* Normal */
```

El ITSE NO usa tracking expandido en sus textos. Letter-spacing siempre es 0% (normal).

---

## Estilos especiales

### Texto sobre imágenes (hero)

```css
.hero-text {
  color: #FFFFFF;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
  font-weight: 700;
}
```

### Texto destacado (highlight)

```css
.highlight {
  color: #FFB000;
  font-weight: 700;
}
```

### Texto con línea dorada debajo (subrayado decorativo)

```css
.title-underline {
  display: inline-block;
  padding-bottom: 8px;
  border-bottom: 3px solid #FFB000;
}
```

### Número grande (cifras destacadas)

```css
.big-number {
  font-size: 3.5rem;  /* 56px */
  font-weight: 700;
  color: #FFB000;
  line-height: 1;
}
```

El ITSE usa números grandes en dorado para estadísticas (ej: "15 carreras", "+4.000 estudiantes", "+80% inserción laboral").

---

## Pautas de uso correcto

✅ **SÍ:**
- Mantén un máximo de 2-3 niveles de jerarquía por slide/sección
- Usa peso 700 para títulos, 400 para body
- Deja respirar el texto (espaciado generoso)
- Usa Inter para web, Arial/Calibri para Office

❌ **NO:**
- NO uses más de 3 pesos de la misma fuente
- NO uses itálicas para énfasis (usa bold en su lugar)
- NO uses underlines decorativos (excepto enlaces)
- NO uses tamaños intermedios raros (15.5px, 17px) — quédate en la escala
- NO uses TODAS MAYÚSCULAS para textos largos (solo títulos cortos)

---

## Cheatsheet

```
ITSE TYPOGRAPHY
===============
Family: Helvetica Neue, Inter, Helvetica, Arial, sans-serif
Weights: 400 (regular), 500 (semi), 700 (bold)

SCALE (rem / px):
  H1     2.5rem / 40px  bold
  H2     2.0rem / 32px  bold
  H3     1.5rem / 24px  bold
  H4     1.25rem / 20px bold
  H5     1.125rem / 18px semi
  H6     1.0rem / 16px  semi
  P      0.875rem / 14px regular
  Small  0.75rem / 12px regular

COLORS:
  Text primary:    #424242
  Text on dark:    #FFFFFF
  Text on gold:    #FFFFFF
  Text secondary:  #7B7B7B
```
