# Snippets Rápidos MiBus

> Bloques de código listos para copiar-pegar con la identidad visual de MiBus.

## 🎨 CSS Variables (copiar-pegar)

```css
:root {
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
  --mibus-warning: #F39C12;
  
  --mibus-font-heading: 'Poppins', 'Arial', 'Helvetica', sans-serif;
  --mibus-font-body: 'Roboto', 'Arial', 'Helvetica', sans-serif;
  
  --mibus-radius: 4px;
  --mibus-radius-lg: 8px;
  --mibus-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  --mibus-shadow-md: 0 4px 16px rgba(0, 0, 0, 0.12);
  --mibus-shadow-lg: 0 8px 32px rgba(40, 60, 144, 0.16);
  
  --mibus-transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}
```

## 🎨 SCSS Variables

```scss
// Colors
$mibus-primary: #283c90;
$mibus-primary-light: #4F5FB5;
$mibus-primary-dark: #1B2A66;
$mibus-secondary: #205CA7;
$mibus-secondary-hover: #409EFF;
$mibus-accent: #1DA1F2;
$mibus-dark: #1A1A2E;
$mibus-bg: #FFFFFF;
$mibus-text: #333333;
$mibus-text-light: #FFFFFF;
$mibus-text-muted: #666666;
$mibus-border: #E0E0E0;
$mibus-border-subtle: #F0F0F0;
$mibus-success: #B5D531;
$mibus-error: #BC0C06;

// Fonts
$mibus-font-heading: 'Poppins', 'Arial', 'Helvetica', sans-serif;
$mibus-font-body: 'Roboto', 'Arial', 'Helvetica', sans-serif;

// Mixins
@mixin mibus-button-primary {
  background: $mibus-secondary;
  color: $mibus-text-light;
  border: 2px solid $mibus-secondary;
  padding: 0.625rem 1.5rem;
  font-family: $mibus-font-body;
  font-weight: 700;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s ease;
  
  &:hover {
    background: $mibus-secondary-hover;
    border-color: $mibus-secondary-hover;
  }
}

@mixin mibus-card {
  background: $mibus-bg;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  padding: 1.5rem;
  transition: all 0.2s ease;
  
  &:hover {
    box-shadow: 0 8px 32px rgba(40, 60, 144, 0.16);
    transform: translateY(-2px);
  }
}
```

## ⚛️ JSX / React Components

```jsx
// MibusButton.jsx
export const MibusButton = ({ children, variant = 'primary', size = 'md', onClick, ...props }) => {
  const baseClass = 'mibus-btn';
  const variantClass = `mibus-btn--${variant}`;
  const sizeClass = size === 'lg' ? 'mibus-btn--lg' : '';
  
  return (
    <button 
      className={`${baseClass} ${variantClass} ${sizeClass}`}
      onClick={onClick}
      {...props}
    >
      {children}
    </button>
  );
};

// MibusCard.jsx
export const MibusCard = ({ title, children, footer }) => {
  return (
    <div className="mibus-card">
      {title && <div className="mibus-card__header">{title}</div>}
      <div className="mibus-card__body">{children}</div>
      {footer && <div className="mibus-card__footer">{footer}</div>}
    </div>
  );
};

// MibusStatCard.jsx
export const MibusStatCard = ({ value, label }) => {
  return (
    <div className="mibus-stat-card">
      <div className="mibus-stat-card__value">{value}</div>
      <div className="mibus-stat-card__label">{label}</div>
    </div>
  );
};
```

## 🟦 Vue 3 Components

```vue
<!-- MibusButton.vue -->
<template>
  <button :class="['mibus-btn', `mibus-btn--${variant}`, { 'mibus-btn--lg': size === 'lg' }]">
    <slot />
  </button>
</template>

<script setup>
defineProps({
  variant: { type: String, default: 'primary' },
  size: { type: String, default: 'md' }
});
</script>
```

## 🅰️ Angular Component

```typescript
// mibus-button.component.ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'mibus-button',
  template: `
    <button 
      [class]="'mibus-btn mibus-btn--' + variant + (size === 'lg' ? ' mibus-btn--lg' : '')">
      <ng-content></ng-content>
    </button>
  `
})
export class MibusButtonComponent {
  @Input() variant: 'primary' | 'secondary' = 'primary';
  @Input() size: 'md' | 'lg' = 'md';
}
```

## 📱 React Native Styles

```javascript
// styles.js
export const mibusStyles = {
  colors: {
    primary: '#283c90',
    primaryLight: '#4F5FB5',
    primaryDark: '#1B2A66',
    secondary: '#205CA7',
    secondaryHover: '#409EFF',
    accent: '#1DA1F2',
    dark: '#1A1A2E',
    bg: '#FFFFFF',
    text: '#333333',
    textLight: '#FFFFFF',
    textMuted: '#666666',
    border: '#E0E0E0',
    success: '#B5D531',
    error: '#BC0C06',
  },
  fonts: {
    heading: 'Poppins',
    body: 'Roboto',
  },
  spacing: {
    xs: 4,
    sm: 8,
    md: 16,
    lg: 24,
    xl: 32,
  },
  radius: {
    sm: 4,
    md: 8,
    lg: 16,
  }
};

export const mibusButton = {
  backgroundColor: mibusStyles.colors.secondary,
  color: mibusStyles.colors.textLight,
  paddingVertical: 12,
  paddingHorizontal: 24,
  borderRadius: mibusStyles.radius.sm,
  fontWeight: '700',
  fontSize: 14,
  fontFamily: mibusStyles.fonts.body,
};
```

## 🏗️ Header HTML reusable

```html
<header class="mibus-header">
  <div class="mibus-header__inner">
    <a href="/" class="mibus-header__logo">
      <img src="https://www.mibus.com.pa/wp-content/uploads/2019/03/logo-1.png" 
           alt="MiBus" height="60">
    </a>
    
    <nav class="mibus-nav">
      <a href="/" class="mibus-nav__link active">Inicio</a>
      <a href="/rutas" class="mibus-nav__link">Rutas</a>
      <a href="/nosotros" class="mibus-nav__link">Nosotros</a>
      <a href="/servicio" class="mibus-nav__link">Servicio al Cliente</a>
    </nav>
    
    <a href="/trabajadores" class="mibus-btn mibus-btn--secondary">
      Trabajadores
    </a>
  </div>
</header>
```

## 🔘 Botones HTML

```html
<!-- Primary -->
<button class="mibus-btn mibus-btn--primary">SUSCRIBIRSE</button>

<!-- Primary Large -->
<button class="mibus-btn mibus-btn--primary mibus-btn--lg">Ver Rutas</button>

<!-- Secondary -->
<button class="mibus-btn mibus-btn--secondary">Conocer más</button>

<!-- Solo texto -->
<button class="mibus-btn mibus-btn--text">Cancelar</button>
```

## 📊 KPI Card HTML

```html
<div class="mibus-stats">
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
```

## 🎨 Estilos CSS completos (mínimo viable)

```css
/* Base */
* { box-sizing: border-box; }
body {
  font-family: 'Roboto', Arial, sans-serif;
  color: #333;
  margin: 0;
  padding: 0;
}
h1, h2, h3 { font-family: 'Poppins', Arial, sans-serif; color: #283c90; }
a { color: #205CA7; text-decoration: none; }
a:hover { color: #409EFF; }

/* Buttons */
.mibus-btn {
  display: inline-block;
  padding: 10px 24px;
  font-family: 'Roboto', Arial, sans-serif;
  font-weight: 700;
  font-size: 14px;
  border: 2px solid transparent;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s;
}
.mibus-btn--primary {
  background: #205CA7;
  color: #fff;
  border-color: #205CA7;
}
.mibus-btn--primary:hover {
  background: #409EFF;
  border-color: #409EFF;
}
.mibus-btn--secondary {
  background: transparent;
  color: #205CA7;
  border-color: #205CA7;
}
.mibus-btn--secondary:hover {
  background: #205CA7;
  color: #fff;
}
.mibus-btn--lg { padding: 14px 32px; font-size: 16px; }

/* Stats */
.mibus-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 24px;
  padding: 48px 24px;
  background: #283c90;
  color: #fff;
}
.mibus-stat-card { text-align: center; }
.mibus-stat-card__value {
  font-family: 'Poppins', sans-serif;
  font-size: 56px;
  font-weight: 900;
  line-height: 1;
}
.mibus-stat-card__label {
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-top: 8px;
  color: #1DA1F2;
}

/* Header */
.mibus-header {
  background: #fff;
  border-bottom: 1px solid #E0E0E0;
  position: sticky;
  top: 0;
  z-index: 100;
}
.mibus-header__inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  max-width: 1200px;
  margin: 0 auto;
  padding: 16px 24px;
  gap: 24px;
}
.mibus-header__logo img { display: block; height: 60px; }
.mibus-nav { display: flex; gap: 24px; }
.mibus-nav__link {
  font-family: 'Poppins', sans-serif;
  font-weight: 600;
  color: #333;
  padding: 8px 0;
  position: relative;
}
.mibus-nav__link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: #205CA7;
  transform: scaleX(0);
  transition: transform 0.2s;
}
.mibus-nav__link:hover::after,
.mibus-nav__link.active::after { transform: scaleX(1); }
.mibus-nav__link:hover,
.mibus-nav__link.active { color: #283c90; }
```

## 📧 Email HTML template

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    body { font-family: 'Roboto', Arial, sans-serif; margin: 0; padding: 0; background: #F0F0F0; }
    .container { max-width: 600px; margin: 0 auto; background: #fff; }
    .header { background: #283c90; padding: 24px; text-align: center; }
    .header img { max-width: 200px; }
    .content { padding: 32px 24px; color: #333; line-height: 1.6; }
    .button { 
      display: inline-block; 
      background: #205CA7; 
      color: #fff; 
      padding: 12px 32px; 
      text-decoration: none; 
      border-radius: 4px; 
      font-weight: 700;
    }
    .footer { 
      background: #1A1A2E; 
      color: #fff; 
      padding: 24px; 
      text-align: center; 
      font-size: 12px; 
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <img src="https://www.mibus.com.pa/wp-content/uploads/2019/03/logo-1.png" alt="MiBus">
    </div>
    <div class="content">
      <h1 style="color: #283c90; font-family: Poppins, sans-serif;">Título del Email</h1>
      <p>Hola,</p>
      <p>Contenido del correo electrónico...</p>
      <p style="text-align: center; margin: 32px 0;">
        <a href="#" class="button">LLAMADA A LA ACCIÓN</a>
      </p>
    </div>
    <div class="footer">
      <p>MiBus · Transporte Masivo de Panamá</p>
      <p><a href="https://www.mibus.com.pa/" style="color: #1DA1F2;">www.mibus.com.pa</a></p>
    </div>
  </div>
</body>
</html>
```

## 🔍 Logo URL constants

```javascript
// constants/logos.js
export const MIBUS_LOGOS = {
  primary: 'https://www.mibus.com.pa/wp-content/uploads/2019/03/logo-1.png',
  retina: 'https://www.mibus.com.pa/wp-content/uploads/2020/05/retina-logo.png',
  footer: 'https://www.mibus.com.pa/wp-content/themes/composer-child/_images/logo-1.png',
  favicon: 'https://www.mibus.com.pa/wp-content/uploads/2020/05/favicon.png',
  bgStats: 'https://www.mibus.com.pa/wp-content/uploads/2023/08/1920x566.jpg',
  bgNewsletter: 'https://www.mibus.com.pa/wp-content/uploads/2019/04/bg-Newsletter.png',
};
```

## 🐍 Python constants

```python
# constants.py
MIBUS_LOGOS = {
    "primary": "https://www.mibus.com.pa/wp-content/uploads/2019/03/logo-1.png",
    "retina": "https://www.mibus.com.pa/wp-content/uploads/2020/05/retina-logo.png",
    "footer": "https://www.mibus.com.pa/wp-content/themes/composer-child/_images/logo-1.png",
    "favicon": "https://www.mibus.com.pa/wp-content/uploads/2020/05/favicon.png",
    "bg_stats": "https://www.mibus.com.pa/wp-content/uploads/2023/08/1920x566.jpg",
    "bg_newsletter": "https://www.mibus.com.pa/wp-content/uploads/2019/04/bg-Newsletter.png",
}

MIBUS_COLORS = {
    "primary":      "#283C90",
    "primary_lt":   "#4F5FB5",
    "primary_dk":   "#1B2A66",
    "secondary":    "#205CA7",
    "secondary_h":  "#409EFF",
    "accent":       "#1DA1F2",
    "dark":         "#1A1A2E",
    "white":        "#FFFFFF",
    "text":         "#333333",
    "text_muted":   "#666666",
    "border":       "#E0E0E0",
    "border_subtle":"#F0F0F0",
    "success":      "#B5D531",
    "error":        "#BC0C06",
}
```
