# Plantilla Web / HTML — ITSE

Guía para crear páginas web, landing pages, dashboards, emails HTML con el estilo ITSE usando la skill `dev-stack` (rama frontend-design) + esta skill.

---

## 🚨 REGLA: Logo del ITSE ARRIBA en headers y portadas

> **El logo del ITSE SIEMPRE va en la parte SUPERIOR de toda página web
> institucional (header sticky) y en portadas de landing pages — NUNCA en
> el centro vertical, NUNCA debajo del hero.**

- **Header principal:** Logo horizontal en la parte superior (sticky), alineado a la izquierda, alto 48–60 px
- **Portadas de landing:** Logo en el header (parte superior), seguido del hero
- **Dashboards:** Logo en el sidebar superior izquierdo o en el header superior
- **Emails HTML:** Logo en la parte superior del cuerpo del email (tabla centrada)

---

## Especificaciones técnicas

| Parámetro | Valor |
|---|---|
| Framework recomendado | HTML + Tailwind CSS (sin build) o HTML vanilla |
| Tipografía web | **Inter** (Google Fonts) — alternativa: system-ui |
| Paleta | CSS Variables en `:root` |
| Iconos | Lucide Icons (SVG) |
| Breakpoints | Mobile-first (sm 640, md 768, lg 1024, xl 1280) |
| Carrera de referencia | **T.S. en Big Data y Ciencia de Datos** (Área de Innovación Digital) |

---

## Sistema de design tokens (CSS variables)

```css
:root {
  /* Colores primarios */
  --color-primary: #FFB000;
  --color-primary-100: #FFB000;
  --color-primary-200: #FFBC00;
  --color-primary-300: #FFCE00;
  
  /* Texto y fondo */
  --color-text: #424242;
  --color-foreground: #424242;
  --color-background: #FFFFFF;
  --color-white: #FFFFFF;
  
  /* Colores secundarios */
  --color-alt-blue: #225082;
  --color-alt-green: #9EBE43;
  --color-alt-red: #CD2E26;
  
  /* Estados */
  --color-success: #00A63E;
  --color-error: #CD2E26;
  --color-warning: #F57C00;
  --color-info: #1A73E8;
  
  /* Grises */
  --color-gray-100: #7B7B7B;
  --color-gray-200: #9D9D9C;
  --color-gray-300: #AEAEAE;
  --color-gray-400: #F7F7F7;
  
  /* Tipografía */
  --font-h1: 2.5rem;
  --font-h2: 2rem;
  --font-h3: 1.5rem;
  --font-h4: 1.25rem;
  --font-h5: 1.125rem;
  --font-h6: 1rem;
  --font-p: 0.875rem;
  --font-small: 0.75rem;
  
  --font-weight-regular: 400;
  --font-weight-semi-bold: 500;
  --font-weight-bold: 700;
  
  /* Espaciado y bordes */
  --border-radius: 12px;
  --border-radius-sm: 8px;
  --border-radius-lg: 16px;
  
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.05);
  --shadow: 0 2px 8px rgba(0,0,0,0.08);
  --shadow-lg: 0 8px 24px rgba(0,0,0,0.12);
}
```

---

## Tipografía web (Google Fonts)

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">
```

```css
body {
  font-family: "Inter", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 14px;
  line-height: 1.5;
  color: var(--color-text);
  background: var(--color-background);
}

h1 { font-size: var(--font-h1); font-weight: 700; line-height: 1.5; }
h2 { font-size: var(--font-h2); font-weight: 700; line-height: 1; }
h3 { font-size: var(--font-h3); font-weight: 700; line-height: 1; }
h4 { font-size: var(--font-h4); font-weight: 700; line-height: 1.2; }
h5 { font-size: var(--font-h5); font-weight: 500; line-height: 1.3; }
h6 { font-size: var(--font-h6); font-weight: 500; line-height: 1.5; }
p  { font-size: var(--font-p); font-weight: 400; line-height: 1.7; }
.small { font-size: var(--font-small); }
```

---

## Logo en el header

```html
<header class="site-header">
  <div class="container">
    <a href="/">
      <img src="assets/logo-itse-horizontal.png" 
           alt="ITSE - Instituto Técnico Superior Especializado" 
           class="logo">
    </a>
    <nav><!-- menú --></nav>
  </div>
</header>
```

```css
.site-header {
  background: white;
  border-bottom: 1px solid var(--color-gray-300);
  padding: 16px 0;
  position: sticky;
  top: 0;
  z-index: 100;
}

.logo { height: 48px; display: block; }
```

---

## Componentes base

### Botones

```html
<button class="btn btn-primary">Inscribirme</button>
<button class="btn btn-outline">Ver más</button>
<button class="btn btn-ghost">Cancelar</button>
```

```css
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 12px 32px;
  font-size: 14px;
  font-weight: 500;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
  text-decoration: none;
}

.btn-primary {
  background: linear-gradient(135deg, #FFCE00 0%, #FFB000 100%);
  color: white;
  font-weight: 700;
}

.btn-primary:hover {
  background: #FFB000;
  box-shadow: 0 4px 12px rgba(255, 176, 0, 0.3);
}

.btn-outline {
  background: white;
  color: var(--color-text);
  border: 1.5px solid var(--color-text);
}

.btn-outline:hover {
  background: var(--color-text);
  color: white;
}

.btn-ghost {
  background: transparent;
  color: var(--color-text);
}

.btn-ghost:hover {
  background: var(--color-gray-400);
}
```

### Cards

```html
<div class="card">
  <img src="..." alt="..." class="card-img">
  <div class="card-body">
    <h3 class="card-title">Título de la card</h3>
    <p class="card-text">Contenido de la card...</p>
    <a href="#" class="btn btn-primary">Ver más</a>
  </div>
</div>
```

```css
.card {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
}

.card:hover {
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  transform: translateY(-2px);
}

.card-img { width: 100%; height: 200px; object-fit: cover; }
.card-body { padding: 24px; }
.card-title { font-size: 20px; font-weight: 700; color: var(--color-text); margin-bottom: 12px; }
.card-text { font-size: 14px; color: var(--color-gray-100); margin-bottom: 16px; line-height: 1.6; }
.card-highlight { border-top: 4px solid var(--color-primary); }
```

### Hero Banner

```html
<section class="hero">
  <div class="hero-content">
    <h1 class="hero-title">Educación Superior de Ciclo Corto</h1>
    <p class="hero-subtitle">Formamos profesionales en 2-3 años.</p>
    <a href="#" class="btn btn-primary">Conoce más</a>
  </div>
  <div class="hero-overlay"></div>
</section>
```

```css
.hero {
  position: relative;
  min-height: 500px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-image: url('hero-bg.jpg');
  background-size: cover;
  background-position: center;
  color: white;
  text-align: center;
  padding: 80px 20px;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: rgba(66, 66, 66, 0.65);
}

.hero-content { position: relative; z-index: 1; max-width: 800px; }

.hero-title {
  font-size: 48px;
  font-weight: 700;
  margin-bottom: 16px;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
}

.hero-subtitle { font-size: 20px; margin-bottom: 32px; opacity: 0.95; }
```

### Sección de cifras (KPI)

```html
<section class="kpi-section">
  <div class="container">
    <h2 class="section-title">Resultados que respaldan nuestro compromiso</h2>
    <p class="section-subtitle">Con Panamá</p>
    <div class="kpi-grid">
      <div class="kpi"><div class="kpi-number">15</div><div class="kpi-label">Carreras</div></div>
      <div class="kpi"><div class="kpi-number">+4.000</div><div class="kpi-label">Estudiantes activos</div></div>
      <div class="kpi"><div class="kpi-number">+10</div><div class="kpi-label">Clubes diferentes</div></div>
      <div class="kpi"><div class="kpi-number">+80%</div><div class="kpi-label">Inserción laboral</div></div>
    </div>
  </div>
</section>
```

```css
.kpi-section {
  background: var(--color-text);
  color: white;
  padding: 80px 20px;
}

.kpi-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 40px;
  margin-top: 60px;
}

.kpi { text-align: center; }

.kpi-number {
  font-size: 64px;
  font-weight: 700;
  color: var(--color-primary);
  line-height: 1;
  margin-bottom: 12px;
}

.kpi-label { font-size: 16px; color: white; font-weight: 500; }
```

### Línea decorativa bajo títulos

```html
<h2 class="title-underline">Título de sección</h2>
```

```css
.title-underline {
  display: inline-block;
  padding-bottom: 12px;
  border-bottom: 3px solid var(--color-primary);
  font-size: 32px;
  font-weight: 700;
  color: var(--color-text);
  margin-bottom: 24px;
}
```

### Formularios

```html
<form class="itse-form">
  <div class="form-group">
    <label for="nombre">Nombre completo</label>
    <input type="text" id="nombre" class="form-input" placeholder="Tu nombre">
  </div>
  <div class="form-group">
    <label for="email">Correo electrónico</label>
    <input type="email" id="email" class="form-input" placeholder="tu@correo.com">
  </div>
  <button type="submit" class="btn btn-primary">Enviar</button>
</form>
```

```css
.itse-form { max-width: 500px; }
.form-group { margin-bottom: 20px; }
.form-group label {
  display: block;
  font-size: 14px;
  font-weight: 500;
  color: var(--color-text);
  margin-bottom: 8px;
}
.form-input {
  width: 100%;
  padding: 12px 16px;
  font-size: 14px;
  font-family: inherit;
  color: var(--color-text);
  background: white;
  border: 1px solid var(--color-gray-300);
  border-radius: 8px;
  transition: border-color 0.2s;
}
.form-input:focus {
  outline: none;
  border-color: var(--color-primary);
  box-shadow: 0 0 0 3px rgba(255, 176, 0, 0.15);
}
.form-input::placeholder { color: var(--color-gray-100); }
```

### Footer

```html
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-col">
        <img src="assets/logo-itse-vertical.png" alt="ITSE" class="footer-logo">
        <p class="footer-tagline">Instituto Técnico Superior Especializado</p>
      </div>
      <div class="footer-col">
        <h5>Enlaces</h5>
        <ul>
          <li><a href="#">Acerca de</a></li>
          <li><a href="#">Oferta académica</a></li>
          <li><a href="#">Admisiones</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Contacto</h5>
        <p>https://www.itse.ac.pa/</p>
        <div class="footer-social">
          <a href="#">FB</a><a href="#">IG</a><a href="#">YT</a><a href="#">X</a>
        </div>
      </div>
    </div>
  </div>
</footer>
```

```css
.site-footer {
  background: var(--color-gray-400);
  border-top: 3px solid var(--color-primary);
  padding: 60px 20px 30px;
}

.footer-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr 1fr;
  gap: 40px;
}

.footer-logo { height: 60px; margin-bottom: 12px; }
.footer-tagline { color: var(--color-gray-100); font-size: 12px; }
.footer-col h5 {
  font-size: 16px;
  font-weight: 700;
  color: var(--color-text);
  margin-bottom: 16px;
}
.footer-col ul { list-style: none; padding: 0; margin: 0; }
.footer-col li { margin-bottom: 8px; }
.footer-col a {
  color: var(--color-text);
  text-decoration: none;
  font-size: 14px;
}
.footer-col a:hover { color: var(--color-primary); }
```

---

## Tailwind CSS — configuración

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#FFB000',
          100: '#FFB000',
          200: '#FFBC00',
          300: '#FFCE00',
        },
        text: '#424242',
        alt: { blue: '#225082', green: '#9EBE43', red: '#CD2E26' },
        gray: { 100: '#7B7B7B', 200: '#9D9D9C', 300: '#AEAEAE', 400: '#F7F7F7' }
      },
      fontFamily: {
        sans: ['Inter', 'Helvetica Neue', 'Helvetica', 'Arial', 'sans-serif'],
      },
      borderRadius: { DEFAULT: '12px' }
    }
  }
}
```

Uso:
```html
<button class="bg-gradient-to-br from-primary-300 to-primary text-white font-bold px-8 py-3 rounded-lg">
  Inscribirme
</button>
```

---

## Página completa de ejemplo (HTML mínimo)

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ITSE — Instituto Técnico Superior Especializado</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    /* CSS de los componentes de arriba */
  </style>
</head>
<body>
  <header class="site-header">
    <div class="container">
      <img src="assets/logo-itse-horizontal.png" alt="ITSE" class="logo">
    </div>
  </header>
  
  <section class="hero">
    <div class="hero-overlay"></div>
    <div class="hero-content">
      <h1>Educación Superior de Ciclo Corto</h1>
      <p>Formamos profesionales en 2-3 años.</p>
      <a href="#" class="btn btn-primary">Conoce más</a>
    </div>
  </section>
  
  <section class="kpi-section">
    <div class="container">
      <div class="kpi-grid">
        <div class="kpi"><div class="kpi-number">15</div><div class="kpi-label">Carreras</div></div>
        <div class="kpi"><div class="kpi-number">+4.000</div><div class="kpi-label">Estudiantes</div></div>
        <div class="kpi"><div class="kpi-number">+80%</div><div class="kpi-label">Inserción laboral</div></div>
      </div>
    </div>
  </section>
  
  <footer class="site-footer">
    <div class="container">
      <p>© {año} Instituto Técnico Superior Especializado</p>
      <!-- {año} = año actual (dinámico) -->
    </div>
  </footer>
</body>
</html>
```

---

## Cheatsheet

```
ITSE WEB
========
Tipografía: Inter (Google Fonts)
Fondo: blanco, secciones alternas #F7F7F7
Acento: #FFB000 con gradiente
Carrera de referencia: T.S. en Big Data y Ciencia de Datos

CSS VARIABLES:
  --color-primary: #FFB000
  --color-text: #424242
  --color-background: #FFFFFF

LOGO: ARRIBA en header sticky (48-60px alto)
      Header en emails HTML (tabla centrada)

COMPONENTES:
  Header:    sticky, white, border-bottom 1px #AEAEAE
  Botones:   rounded-8px, gradient para primary
  Cards:     rounded-12px, shadow sutil
  Hero:      imagen + overlay rgba(66,66,66,0.65) + texto blanco
  KPI:       números 64pt bold #FFB000 sobre #424242
  Footer:    bg #F7F7F7, border-top 3px #FFB000

BREAKPOINTS:
  sm: 640px
  md: 768px
  lg: 1024px
  xl: 1280px
```

---

## Recursos adicionales

- `references/itse/colors.md` — paleta completa
- `references/itse/typography.md` — sistema tipográfico
- `references/itse/logo.md` — uso del logo
- `references/itse/branding.md` — datos institucionales
- `assets/logo-itse-horizontal.png` — logo principal
- Skill complementaria: `dev-stack` (rama frontend-design)
