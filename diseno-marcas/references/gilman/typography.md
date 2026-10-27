# Tipografía — gilman.pro

Sistema tipográfico de 4 familias, una para cada rol. **No sustituyas por sans-serif genéricas (Arial, Helvetica).**

## Familias

### 1. `heading` — **Montserrat**
- **Rol:** títulos (H1–H4), navbar, navegación, headings de cards
- **Pesos:** 400, 500, 600, 700, 800
- **Uso típico:** `font-heading font-bold` (Tailwind)
- **Tracking:** `tracking-tight` en títulos grandes
- **Google Fonts:** `https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap`

### 2. `body` — **Lato**
- **Rol:** texto corrido, párrafos, descripciones, body de cards
- **Pesos:** 300, 400, 700
- **Uso típico:** `font-body` (Tailwind) o implícito como default
- **Line-height:** 1.6 (leading-relaxed)
- **Google Fonts:** `https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&display=swap`

### 3. `display` — **Orbitron**
- **Rol:** números grandes, hero, impacto visual, stats
- **Pesos:** 400, 500, 600, 700, 800, 900
- **Uso típico:** "Circuit G" en el logo, números de impacto
- **Tracking:** `tracking-wider` para mayúsculas
- **Google Fonts:** `https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&display=swap`

### 4. `tech` — **Rajdhani**
- **Rol:** wordmark "gilman.pro", headings tech, labels condensadas, números secundarios
- **Pesos:** 300, 400, 500, 600, 700
- **Uso típico:** texto del logo, headings con look "tech"
- **Google Fonts:** `https://fonts.googleapis.com/css2?family=Rajdhani:wght@300;400;500;600;700&display=swap`

## URL combinada (las 4 familias)

```html
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&family=Lato:wght@300;400;700&family=Orbitron:wght@400;500;600;700;800;900&family=Rajdhani:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

## Escala tipográfica

| Elemento | Familia | Peso | Tamaño (mobile) | Tamaño (desktop) | Line-height | Tracking |
|---|---|---|---|---|---|---|
| H1 (Hero) | Montserrat | 800 | 2.25rem (36px) | 3.75rem (60px) | 1.1 | -0.025em (tight) |
| H2 (sección) | Montserrat | 700 | 1.875rem (30px) | 2.25rem (36px) | 1.2 | -0.025em (tight) |
| H3 (subsección) | Montserrat | 600 | 1.5rem (24px) | 1.875rem (30px) | 1.3 | normal |
| H4 (card title) | Montserrat | 600 | 1.125rem (18px) | 1.25rem (20px) | 1.4 | normal |
| H5 / label | Rajdhani | 600 | 0.875rem (14px) | 1rem (16px) | 1.4 | 0.05em (wide) |
| Body / párrafo | Lato | 400 | 1rem (16px) | 1rem (16px) | 1.6 (relaxed) | normal |
| Body emphasis | Lato | 700 | 1rem | 1rem | 1.6 | normal |
| Caption / small | Lato | 400 | 0.875rem (14px) | 0.875rem (14px) | 1.5 | normal |
| Tiny | Lato | 300 | 0.75rem (12px) | 0.75rem (12px) | 1.4 | normal |
| Display number | Orbitron | 700 | 3rem (48px) | 5rem (80px) | 1.0 | 0.05em (wide) |
| Wordmark "gilman.pro" | Rajdhani | 700 | 1.125rem (18px) | 1.5rem (24px) | 1.0 | normal |
| Button label | Lato | 600 | 0.875rem (14px) | 0.875rem (14px) | 1.0 | 0.025em |

## Reglas

1. **Títulos = Montserrat, siempre.** No usar Lato ni Rajdhani para H1–H4.
2. **Cuerpo = Lato, siempre.** El párrafo SIEMPRE es Lato.
3. **Wordmark "gilman.pro" = Rajdhani 700** (alternativa: Orbitron 700). Color: `#10B981`.
4. **Numerales en impacto** (ej. "5 años de experiencia", "100+ proyectos") = Orbitron 700.
5. **NUNCA** usar Comic Sans, Papyrus, Times New Roman, ni sans-serif genéricas.
6. **Fallbacks siempre:** `font-family: 'Montserrat', system-ui, sans-serif;`
7. **Carga:** preferir Google Fonts CDN. Para PowerPoint/Word: descargar .ttf y embeber.
8. **Tracking:** `tracking-tight` en H1/H2, `tracking-wider` en headings uppercase tipo label.
9. **Anti-pattern:** NO mezclar más de 2 familias en un mismo bloque visible. Típico: H1 Montserrat + body Lato. Solo agregar Orbitron/Rajdhani para acentos puntuales.

## Configuración Tailwind (referencia)

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        heading: ['Montserrat', 'system-ui', 'sans-serif'],
        body: ['Lato', 'system-ui', 'sans-serif'],
        display: ['Orbitron', 'system-ui', 'sans-serif'],
        tech: ['Rajdhani', 'system-ui', 'sans-serif'],
      }
    }
  }
}
```

## Aplicación por formato

| Formato | Cómo se cargan las fuentes |
|---|---|
| **Web (HTML/Tailwind)** | `<link>` Google Fonts + `font-family` en CSS |
| **PowerPoint** | Descargar .ttf de Google Fonts → "Insertar fuente" en Office |
| **Word** | Descargar .ttf + instalar en Windows + seleccionar en estilos |
| **Excel** | Descargar .ttf + instalar en Windows + aplicar por celda |
| **PDF** | Si se genera desde HTML: heredar del template. Si es nativo: incrustar en el editor |
| **SVG** | Usar `font-family` en `<text>` con fallback a `sans-serif`; o convertir a paths |

## Pesos preferidos

- **Montserrat:** usar 700 por defecto; 800 solo en H1 hero; 500-600 en subtítulos.
- **Lato:** usar 400 por defecto; 700 solo para emphasis puntual; 300 para captions.
- **Orbitron:** usar 700; nunca 400 (se ve débil en digital).
- **Rajdhani:** usar 600-700; 300-400 para texto secundario condensado.
