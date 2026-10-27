# Guía: Aplicar Diseño MiBus a Web (HTML/CSS/JS)

> Cómo crear páginas web, landings, dashboards, apps con la identidad visual de MiBus.

## 📋 Antes de empezar

1. Lee `assets/brand-mibus.json` y `assets/colors-mibus.md` de esta skill.
2. **Carga la skill `dev-stack`** del sistema opencode (rama frontend-design).
3. Usa la rama UI/UX Pro Max de esa misma skill (`dev-stack`) para referencias de diseño adicionales.
4. Combina: identidad MiBus (esta skill) + dev-stack/frontend-design (UI patterns) + dev-stack/ui-ux-pro-max (estilos).
5. **SIEMPRE** valida con Chrome DevTools (consola + network + Lighthouse).

## 🎨 CSS Custom Properties (base recomendada)

Incluir en el `<head>` de cada página o en el archivo CSS principal:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;600;700;900&family=Roboto:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

```css
:root {
  /* ==== COLORES MiBus ==== */
  --mibus-primary: #283c90;
  --mibus-primary-light: #4F5FB5;
  --mibus-primary-dark: #1B2A66;
  --mibus-secondary: #205CA7;
  --mibus-secondary-hover: #409EFF;
  --mibus-accent: #1DA1F2;
  --mibus-dark: #1A1A2E;
  --mibus-bg: #FFFFFF;
  --mibus-text: #333333;
  --mibus-text-light: #FFFFFF;
  --mibus-text-muted: #666666;
  --mibus-border: #E0E0E0;
  --mibus-border-subtle: #F0F0F0;
  --mibus-success: #B5D531;
  --mibus-error: #BC0C06;

  /* ==== TIPOGRAFÍAS ==== */
  --mibus-font-heading: 'Poppins', 'Arial', 'Helvetica', sans-serif;
  --mibus-font-body: 'Roboto', 'Arial', 'Helvetica', sans-serif;

  /* ==== ESPACIADO ==== */
  --mibus-radius: 4px;
  --mibus-radius-lg: 8px;
  --mibus-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  --mibus-shadow-md: 0 4px 16px rgba(0, 0, 0, 0.12);
  --mibus-shadow-lg: 0 8px 32px rgba(40, 60, 144, 0.16);

  /* ==== TRANSICIONES ==== */
  --mibus-transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  --mibus-transition-slow: all 0.3s ease-in-out;
}
```

## 🏗️ Estructura de layout (siguiendo mibus.com.pa)

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MiBus — [Página]</title>
  
  <!-- Favicon MiBus -->
  <link rel="icon" type="image/png" href="https://www.mibus.com.pa/wp-content/uploads/2020/05/favicon.png">
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;600;700;900&family=Roboto:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- 1. Top bar (dark) -->
  <div class="mibus-topbar">
    <div class="container">
      <div class="mibus-topbar__social">
        <a href="https://www.facebook.com/oficialmibuspty/" target="_blank">Facebook</a>
        <a href="https://pa.linkedin.com/company/mibus" target="_blank">LinkedIn</a>
        <a href="https://www.instagram.com/oficialmibus/" target="_blank">Instagram</a>
        <a href="https://www.youtube.com/channel/UCN0lsfIURO1hGIV3wBhpenw" target="_blank">YouTube</a>
      </div>
    </div>
  </div>

  <!-- 2. Header principal -->
  <header class="mibus-header">
    <div class="container mibus-header__inner">
      <a href="/" class="mibus-header__logo">
        <img src="https://www.mibus.com.pa/wp-content/uploads/2019/03/logo-1.png" alt="MiBus" height="60">
      </a>
      
      <nav class="mibus-nav">
        <a href="/" class="mibus-nav__link active">Inicio</a>
        <a href="/rutas" class="mibus-nav__link">Rutas</a>
        <a href="/nosotros" class="mibus-nav__link">Nosotros</a>
        <a href="/servicio" class="mibus-nav__link">Servicio al Cliente</a>
        <a href="/noticias" class="mibus-nav__link">Noticias</a>
      </nav>
      
      <div class="mibus-header__actions">
        <a href="/trabajadores" class="mibus-btn mibus-btn--secondary">
          <svg><!-- user icon --></svg>
          Trabajadores
        </a>
      </div>
    </div>
  </header>

  <!-- 3. Hero section -->
  <section class="mibus-hero">
    <div class="mibus-hero__content">
      <h1 class="mibus-hero__title">Transporte Masivo de Panamá</h1>
      <p class="mibus-hero__subtitle">Conectando Panamá, un viaje a la vez</p>
      <a href="/rutas" class="mibus-btn mibus-btn--primary mibus-btn--lg">Ver Rutas</a>
    </div>
  </section>

  <!-- 4. Stats counter -->
  <section class="mibus-stats">
    <div class="container">
      <div class="mibus-stats__grid">
        <div class="mibus-stat-card">
          <div class="mibus-stat-card__value">1436</div>
          <div class="mibus-stat-card__label">Unidades</div>
        </div>
        <div class="mibus-stat-card">
          <div class="mibus-stat-card__value">+4,000</div>
          <div class="mibus-stat-card__label">Trabajadores</div>
        </div>
        <div class="mibus-stat-card">
          <div class="mibus-stat-card__value">152</div>
          <div class="mibus-stat-card__label">Rutas</div>
        </div>
        <div class="mibus-stat-card">
          <div class="mibus-stat-card__value">450,000</div>
          <div class="mibus-stat-card__label">Pasajeros diarios</div>
        </div>
      </div>
    </div>
  </section>

  <!-- 5. Footer -->
  <footer class="mibus-footer">
    <div class="container">
      <div class="mibus-footer__grid">
        <div class="mibus-footer__col">
          <img src="https://www.mibus.com.pa/wp-content/uploads/2019/03/logo-1.png" alt="MiBus" height="50">
        </div>
        <div class="mibus-footer__col">
          <h4>Enlaces de Interés</h4>
          <ul>
            <li><a href="/preguntas-frecuentes">Preguntas frecuentes</a></li>
            <li><a href="/noticias">Noticias</a></li>
            <li><a href="/trabaja-con-nosotros">Trabaja con nosotros</a></li>
            <li><a href="/red-de-rutas">Red de rutas</a></li>
          </ul>
        </div>
        <div class="mibus-footer__col">
          <h4>Contáctenos</h4>
          <ul>
            <li><a href="/contactanos">Consultas</a></li>
            <li><a href="https://311.gob.pa" target="_blank">311 Panamá</a></li>
          </ul>
        </div>
      </div>
      <div class="mibus-footer__bottom">
        <p>MiBus TODOS LOS DERECHOS RESERVADOS © 2019. PANAMÁ, REP. DE PANAMÁ.</p>
      </div>
    </div>
  </footer>
</body>
</html>
```

## 🎨 CSS Component Styles

```css
/* ==== BASE ==== */
* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: var(--mibus-font-body);
  font-size: 16px;
  line-height: 1.6;
  color: var(--mibus-text);
  background: var(--mibus-bg);
}

h1, h2, h3, h4, h5, h6 {
  font-family: var(--mibus-font-heading);
  color: var(--mibus-primary);
  font-weight: 700;
  line-height: 1.2;
}

h1 { font-size: 2.5rem; }
h2 { font-size: 2rem; }
h3 { font-size: 1.5rem; }

a { color: var(--mibus-secondary); text-decoration: none; transition: var(--mibus-transition); }
a:hover { color: var(--mibus-secondary-hover); }

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

/* ==== TOPBAR ==== */
.mibus-topbar {
  background: var(--mibus-dark);
  color: var(--mibus-text-light);
  font-size: 0.875rem;
  padding: 0.5rem 0;
}

.mibus-topbar a {
  color: var(--mibus-text-light);
  margin-right: 1rem;
}

.mibus-topbar a:hover {
  color: var(--mibus-accent);
}

/* ==== HEADER ==== */
.mibus-header {
  background: var(--mibus-white);
  border-bottom: 1px solid var(--mibus-border);
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: var(--mibus-shadow);
}

.mibus-header__inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 1.5rem;
  gap: 2rem;
}

.mibus-header__logo img {
  display: block;
  height: 60px;
}

.mibus-nav {
  display: flex;
  gap: 1.5rem;
  flex: 1;
  justify-content: center;
}

.mibus-nav__link {
  font-family: var(--mibus-font-heading);
  font-weight: 600;
  color: var(--mibus-text);
  padding: 0.5rem 0;
  position: relative;
  transition: var(--mibus-transition);
}

.mibus-nav__link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: var(--mibus-secondary);
  transform: scaleX(0);
  transition: var(--mibus-transition);
}

.mibus-nav__link:hover::after,
.mibus-nav__link.active::after {
  transform: scaleX(1);
}

.mibus-nav__link:hover,
.mibus-nav__link.active {
  color: var(--mibus-primary);
}

/* ==== BUTTONS ==== */
.mibus-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.625rem 1.5rem;
  font-family: var(--mibus-font-body);
  font-weight: 700;
  font-size: 0.875rem;
  border-radius: var(--mibus-radius);
  border: 2px solid transparent;
  cursor: pointer;
  transition: var(--mibus-transition);
  text-decoration: none;
  white-space: nowrap;
}

.mibus-btn--primary {
  background: var(--mibus-secondary);
  color: var(--mibus-text-light);
  border-color: var(--mibus-secondary);
}

.mibus-btn--primary:hover {
  background: var(--mibus-secondary-hover);
  border-color: var(--mibus-secondary-hover);
  color: var(--mibus-text-light);
  transform: translateY(-1px);
  box-shadow: var(--mibus-shadow-md);
}

.mibus-btn--secondary {
  background: transparent;
  color: var(--mibus-primary);
  border-color: var(--mibus-primary);
}

.mibus-btn--secondary:hover {
  background: var(--mibus-primary);
  color: var(--mibus-text-light);
}

.mibus-btn--lg {
  padding: 0.875rem 2rem;
  font-size: 1rem;
}

/* ==== HERO ==== */
.mibus-hero {
  position: relative;
  min-height: 500px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  background: linear-gradient(135deg, var(--mibus-primary), var(--mibus-primary-dark));
  color: var(--mibus-text-light);
  padding: 4rem 1.5rem;
  overflow: hidden;
}

.mibus-hero::before {
  content: '';
  position: absolute;
  inset: 0;
  background: url('https://www.mibus.com.pa/wp-content/uploads/2023/08/1920x566.jpg') center / cover;
  opacity: 0.3;
  z-index: 0;
}

.mibus-hero__content {
  position: relative;
  z-index: 1;
  max-width: 800px;
}

.mibus-hero__title {
  font-size: 3.5rem;
  font-weight: 900;
  color: var(--mibus-text-light);
  margin-bottom: 1rem;
  text-shadow: 0 2px 8px rgba(0,0,0,0.3);
}

.mibus-hero__subtitle {
  font-size: 1.25rem;
  font-weight: 300;
  margin-bottom: 2rem;
  opacity: 0.95;
}

/* ==== STATS ==== */
.mibus-stats {
  background: url('https://www.mibus.com.pa/wp-content/uploads/2023/08/1920x566.jpg') center / cover;
  position: relative;
  padding: 4rem 0;
}

.mibus-stats::before {
  content: '';
  position: absolute;
  inset: 0;
  background: rgba(40, 60, 144, 0.85);
}

.mibus-stats__grid {
  position: relative;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 2rem;
  text-align: center;
  color: var(--mibus-text-light);
}

.mibus-stat-card__value {
  font-family: var(--mibus-font-heading);
  font-size: 3.5rem;
  font-weight: 900;
  color: var(--mibus-text-light);
  margin-bottom: 0.5rem;
  line-height: 1;
}

.mibus-stat-card__label {
  font-size: 1rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  opacity: 0.9;
}

/* ==== FOOTER ==== */
.mibus-footer {
  background: var(--mibus-dark);
  color: var(--mibus-text-light);
  padding: 3rem 0 1.5rem;
}

.mibus-footer__grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: 2rem;
  margin-bottom: 2rem;
}

.mibus-footer h4 {
  color: var(--mibus-text-light);
  font-size: 1.125rem;
  margin-bottom: 1rem;
}

.mibus-footer ul {
  list-style: none;
}

.mibus-footer li {
  margin-bottom: 0.5rem;
}

.mibus-footer a {
  color: rgba(255, 255, 255, 0.7);
  transition: var(--mibus-transition);
}

.mibus-footer a:hover {
  color: var(--mibus-accent);
}

.mibus-footer__bottom {
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  padding-top: 1.5rem;
  text-align: center;
  font-size: 0.875rem;
  color: rgba(255, 255, 255, 0.6);
}

/* ==== RESPONSIVE ==== */
@media (max-width: 768px) {
  .mibus-header__inner {
    flex-direction: column;
    gap: 1rem;
  }
  
  .mibus-nav {
    flex-wrap: wrap;
    justify-content: center;
  }
  
  .mibus-hero__title {
    font-size: 2rem;
  }
  
  .mibus-stats__grid {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .mibus-footer__grid {
    grid-template-columns: 1fr;
  }
}
```

## 🎨 Tailwind Config

```js
// tailwind.config.js
module.exports = {
  content: ['./src/**/*.{html,js,jsx,ts,tsx,vue,svelte}'],
  theme: {
    extend: {
      colors: {
        mibus: {
          primary: '#283c90',
          'primary-light': '#4F5FB5',
          'primary-dark': '#1B2A66',
          secondary: '#205CA7',
          'secondary-hover': '#409EFF',
          accent: '#1DA1F2',
          dark: '#1A1A2E',
          bg: '#FFFFFF',
          text: '#333333',
          'text-muted': '#666666',
          border: '#E0E0E0',
          success: '#B5D531',
          error: '#BC0C06',
        }
      },
      fontFamily: {
        heading: ['Poppins', 'Arial', 'sans-serif'],
        body: ['Roboto', 'Arial', 'sans-serif'],
      },
      boxShadow: {
        mibus: '0 2px 8px rgba(0, 0, 0, 0.08)',
        'mibus-md': '0 4px 16px rgba(0, 0, 0, 0.12)',
        'mibus-lg': '0 8px 32px rgba(40, 60, 144, 0.16)',
      },
      borderRadius: {
        mibus: '4px',
      }
    }
  }
}
```

```html
<!-- Uso con Tailwind -->
<button class="bg-mibus-secondary text-white px-6 py-2.5 rounded-mibus font-bold hover:bg-mibus-secondary-hover transition-all">
  SUSCRIBIRSE
</button>
```

## 📱 Componentes UI específicos MiBus

### Card de Noticia

```html
<article class="mibus-news-card">
  <img src="noticia.jpg" alt="Título" class="mibus-news-card__img">
  <div class="mibus-news-card__body">
    <span class="mibus-news-card__date">15 Junio 2026</span>
    <h3 class="mibus-news-card__title">Nueva ruta hacia el Este</h3>
    <p class="mibus-news-card__excerpt">Resumen de la noticia...</p>
    <a href="/noticias/ruta-este" class="mibus-news-card__link">Leer más →</a>
  </div>
</article>

<style>
.mibus-news-card {
  background: var(--mibus-bg);
  border-radius: var(--mibus-radius);
  overflow: hidden;
  box-shadow: var(--mibus-shadow);
  transition: var(--mibus-transition);
}
.mibus-news-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--mibus-shadow-lg);
}
.mibus-news-card__img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}
.mibus-news-card__body { padding: 1.5rem; }
.mibus-news-card__date {
  color: var(--mibus-text-muted);
  font-size: 0.875rem;
}
.mibus-news-card__title {
  color: var(--mibus-primary);
  margin: 0.5rem 0;
}
.mibus-news-card__link {
  color: var(--mibus-secondary);
  font-weight: 600;
}
</style>
```

## ✅ Checklist para Web MiBus

- [ ] Logo MiBus en header con link a home
- [ ] Favicon MiBus
- [ ] Google Fonts (Poppins + Roboto) preloaded
- [ ] CSS variables con paleta MiBus
- [ ] Top bar dark con redes sociales
- [ ] Header sticky con nav highlight
- [ ] Botones con estilo primary/secondary
- [ ] Hero con imagen de fondo o gradiente primary
- [ ] Stats con números grandes Poppins 900
- [ ] Footer dark con 4 columnas
- [ ] Responsive: mobile-first
- [ ] Validar en Chrome DevTools (consola sin errores)

## 🚫 Errores comunes

- ❌ Usar fuentes default (Arial, Helvetica) sin Google Fonts
- ❌ Header con fondo blanco plano sin contraste
- ❌ Botones cuadrados sin border-radius
- ❌ Stats con números pequeños (deben ser grandes)
- ❌ Footer con fondo blanco
- ❌ Sin favicon o favicon genérico
- ❌ No validar responsive en mobile
- ❌ Logo sin espacio de respeto
