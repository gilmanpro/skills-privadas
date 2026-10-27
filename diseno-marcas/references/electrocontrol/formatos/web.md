# Aplicación del diseño Electrocontrol a Web (HTML/CSS/JS)

Guía para crear páginas web, landing pages, dashboards y emails con el sistema de diseño de IoT Tech / Electrocontrol. **Esta skill NO reemplaza la skill `dev-stack`** (rama frontend-design) — la complementa. Carga ambas.

---

## Cuándo usar esta guía

| Tarea | Cargar también |
|---|---|
| Landing page para Electrocontrol | `dev-stack` |
| Dashboard interno | `dev-stack` + esta guía |
| Email HTML (newsletter) | `dev-stack` (adaptado a email) |
| Web app completa (React/Next) | `dev-stack` + esta guía |
| Email transaccional | Esta guía (sin Tailwind, solo CSS inline) |

---

## Stack recomendado (mismo que el sitio oficial)

| Componente | Tecnología |
|---|---|
| **Framework** | Next.js (igual que el sitio), o HTML+Tailwind vanilla |
| **CSS** | Tailwind CSS (mismo que el sitio) |
| **Iconos** | Lucide React (mismo que el sitio) |
| **Fuentes** | Inter o Geist (sistema) |
| **Animaciones** | Framer Motion o CSS keyframes (animate-pulse-slow) |
| **Sombras** | Box-shadow con tinte cyan |

**Si el sitio oficial usa Next.js + Tailwind + Lucide, replica exactamente ese stack** para máxima coherencia.

---

## Estructura HTML base

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>IoT Tech - {{Título}}</title>
  <meta name="description" content="{{descripción}}">

  <!-- Inter desde Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            sans: ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
          },
          colors: {
            // Slate (ya viene en Tailwind)
            // Cyan (ya viene)
            // Purple (ya viene)
            // Pink (ya viene)
          },
        }
      }
    }
  </script>

  <!-- Lucide icons -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <style>
    body { -webkit-font-smoothing: antialiased; }
    @keyframes pulse-slow {
      0%, 100% { opacity: 0.1; }
      50% { opacity: 0.2; }
    }
    .animate-pulse-slow { animation: pulse-slow 4s ease-in-out infinite; }
  </style>
</head>
<body class="antialiased min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 text-white">
  <!-- contenido -->
</body>
</html>
```

---

## Tailwind config extendido (recomendado)

Para proyectos Next.js o con build system, extender Tailwind con la paleta exacta:

```js
// tailwind.config.js
module.exports = {
  content: ['./src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
      },
      colors: {
        brand: {
          cyan: { 400: '#22D3EE', 500: '#06B6D4' },
          purple: { 400: '#C084FC', 500: '#A855F7' },
          pink: { 400: '#F472B6', 500: '#EC4899' },
        },
        slate: {
          900: '#0F172A',
          800: '#1E293B',
          700: '#334155',
          600: '#475569',
          500: '#64748B',
          400: '#94A3B8',
          300: '#CBD5E1',
        },
      },
      backgroundImage: {
        'gradient-brand': 'linear-gradient(to right, #22D3EE, #C084FC, #F472B6)',
        'gradient-button': 'linear-gradient(to right, #06B6D4, #A855F7)',
        'gradient-body': 'linear-gradient(to bottom right, #0F172A, #1E293B, #0F172A)',
      },
      boxShadow: {
        'cyan-glow': '0 10px 30px rgba(6, 182, 212, 0.25)',
        'cyan-glow-lg': '0 15px 40px rgba(6, 182, 212, 0.5)',
        'purple-glow': '0 10px 30px rgba(168, 85, 247, 0.3)',
      },
      animation: {
        'pulse-slow': 'pulse-slow 4s ease-in-out infinite',
      },
    },
  },
  plugins: [],
};
```

---

## Componentes reutilizables

### Hero section (firma de marca)

```html
<section class="relative min-h-screen flex items-center justify-center overflow-hidden bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900">
  <!-- Blobs decorativos -->
  <div class="absolute inset-0 overflow-hidden">
    <div class="absolute top-1/4 left-1/4 w-96 h-96 bg-cyan-500/10 rounded-full blur-3xl animate-pulse-slow"></div>
    <div class="absolute bottom-1/4 right-1/4 w-96 h-96 bg-purple-500/10 rounded-full blur-3xl animate-pulse-slow"></div>
  </div>

  <div class="relative z-10 text-center px-6 max-w-5xl">
    <!-- Logo -->
    <div class="flex justify-center mb-8">
      <img src="logo-electrocontrol.jpg" alt="IoT Tech Logo" class="w-32 h-32 md:w-40 md:h-40 rounded-2xl">
    </div>

    <!-- Título con degradado -->
    <h1 class="text-5xl md:text-7xl font-bold mb-6 bg-gradient-to-r from-cyan-400 via-purple-400 to-pink-400 bg-clip-text text-transparent">
      {{Título Principal}}
    </h1>

    <!-- Subtítulo -->
    <p class="text-xl md:text-2xl text-slate-300 mb-8 max-w-3xl mx-auto">
      {{Subtítulo descriptivo}}
    </p>

    <!-- CTA -->
    <a href="#contacto" class="inline-block bg-gradient-to-r from-cyan-500 to-purple-500 text-white px-8 py-4 rounded-full font-semibold text-lg shadow-lg shadow-cyan-500/25 hover:shadow-cyan-500/50 transition-all">
      Conócenos
    </a>
  </div>
</section>
```

### Sección "Sobre Mí" con foto + stat cards

```html
<section id="sobre-mi" class="py-24 bg-slate-800">
  <div class="max-w-7xl mx-auto px-6">
    <!-- Título de sección con degradado -->
    <h2 class="text-4xl md:text-5xl font-bold text-center mb-16 bg-gradient-to-r from-cyan-400 to-purple-400 bg-clip-text text-transparent">
      Sobre Mí
    </h2>

    <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
      <!-- Foto -->
      <div class="flex justify-center">
        <div class="relative">
          <div class="w-72 h-72 md:w-96 md:h-96 rounded-full overflow-hidden border-4 border-cyan-500/30 shadow-2xl shadow-cyan-500/20">
            <img src="foto-perfil.jpg" alt="Malkom Daniel Cordoba" class="object-cover w-full h-full">
          </div>
          <div class="absolute -bottom-4 -right-4 bg-gradient-to-r from-cyan-500 to-purple-500 rounded-full p-4 shadow-lg">
            <i data-lucide="user" class="w-8 h-8 text-white"></i>
          </div>
        </div>
      </div>

      <!-- Bio + stats -->
      <div class="space-y-6">
        <div>
          <h3 class="text-3xl md:text-4xl font-bold text-white mb-2">Malkom Daniel Cordoba</h3>
          <p class="text-cyan-400 text-lg font-medium">Especialista en Mecatrónica & Electrónica Automotriz</p>
        </div>

        <p class="text-slate-300 text-lg leading-relaxed">
          Con más de 10 años de experiencia en ingeniería mecatrónica, electrónica automotriz
          y desarrollo de soluciones IoT...
        </p>

        <!-- Stat cards -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-4">
          <div class="flex items-center gap-3 bg-slate-700/50 rounded-xl p-4">
            <i data-lucide="award" class="w-8 h-8 text-yellow-400"></i>
            <div>
              <p class="text-white font-semibold">Experiencia</p>
              <p class="text-slate-400 text-sm">+10 años</p>
            </div>
          </div>
          <div class="flex items-center gap-3 bg-slate-700/50 rounded-xl p-4">
            <i data-lucide="briefcase" class="w-8 h-8 text-purple-400"></i>
            <div>
              <p class="text-white font-semibold">Proyectos</p>
              <p class="text-slate-400 text-sm">200+ completados</p>
            </div>
          </div>
          <div class="flex items-center gap-3 bg-slate-700/50 rounded-xl p-4">
            <i data-lucide="graduation-cap" class="w-8 h-8 text-green-400"></i>
            <div>
              <p class="text-white font-semibold">Formación</p>
              <p class="text-slate-400 text-sm">Ing. Mecatrónica</p>
            </div>
          </div>
          <div class="flex items-center gap-3 bg-slate-700/50 rounded-xl p-4">
            <i data-lucide="user" class="w-8 h-8 text-cyan-400"></i>
            <div>
              <p class="text-white font-semibold">Especialidad</p>
              <p class="text-slate-400 text-sm">Mecatrónica & ECU</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

### Card de servicio (4 variantes con colores)

```html
<!-- Card IoT (cyan/blue) -->
<div class="relative h-64 md:h-80 rounded-2xl overflow-hidden group">
  <img src="{{imagen}}" alt="IoT" class="object-cover w-full h-full group-hover:scale-110 transition-transform duration-500">
  <div class="absolute inset-0 bg-gradient-to-br from-cyan-500 to-blue-500 opacity-20"></div>
  <div class="absolute top-4 left-4 w-14 h-14 rounded-xl bg-gradient-to-br from-cyan-500 to-blue-500 flex items-center justify-center">
    <i data-lucide="wifi" class="w-7 h-7 text-white"></i>
  </div>
</div>
```

```html
<!-- Card ECU (orange/red) -->
<div class="relative h-64 md:h-80 rounded-2xl overflow-hidden group">
  <img src="{{imagen}}" alt="ECU" class="object-cover w-full h-full group-hover:scale-110 transition-transform duration-500">
  <div class="absolute inset-0 bg-gradient-to-br from-orange-500 to-red-500 opacity-20"></div>
  <div class="absolute top-4 left-4 w-14 h-14 rounded-xl bg-gradient-to-br from-orange-500 to-red-500 flex items-center justify-center">
    <i data-lucide="car" class="w-7 h-7 text-white"></i>
  </div>
</div>
```

```html
<!-- Card Automatización (green/emerald) -->
<div class="relative h-64 md:h-80 rounded-2xl overflow-hidden group">
  <img src="{{imagen}}" alt="Automatización" class="object-cover w-full h-full group-hover:scale-110 transition-transform duration-500">
  <div class="absolute inset-0 bg-gradient-to-br from-green-500 to-emerald-500 opacity-20"></div>
  <div class="absolute top-4 left-4 w-14 h-14 rounded-xl bg-gradient-to-br from-green-500 to-emerald-500 flex items-center justify-center">
    <i data-lucide="settings" class="w-7 h-7 text-white"></i>
  </div>
</div>
```

```html
<!-- Card Programación (purple/pink) -->
<div class="relative h-64 md:h-80 rounded-2xl overflow-hidden group">
  <img src="{{imagen}}" alt="Programación" class="object-cover w-full h-full group-hover:scale-110 transition-transform duration-500">
  <div class="absolute inset-0 bg-gradient-to-br from-purple-500 to-pink-500 opacity-20"></div>
  <div class="absolute top-4 left-4 w-14 h-14 rounded-xl bg-gradient-to-br from-purple-500 to-pink-500 flex items-center justify-center">
    <i data-lucide="code" class="w-7 h-7 text-white"></i>
  </div>
</div>
```

### Sección de contacto (cards + form)

```html
<section id="contacto" class="py-24 bg-gradient-to-b from-slate-900 to-slate-800">
  <div class="max-w-7xl mx-auto px-6">
    <h2 class="text-4xl md:text-5xl font-bold text-center mb-4 bg-gradient-to-r from-cyan-400 to-purple-400 bg-clip-text text-transparent">
      Contáctanos
    </h2>
    <p class="text-slate-400 text-lg text-center max-w-2xl mx-auto mb-16">
      ¿Listo para transformar tu negocio con tecnología? Escríbenos hoy mismo.
    </p>

    <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
      <!-- Info cards -->
      <div class="space-y-8">
        <div class="flex items-start gap-4">
          <div class="w-12 h-12 rounded-lg bg-cyan-500/20 flex items-center justify-center flex-shrink-0">
            <i data-lucide="phone" class="w-6 h-6 text-cyan-400"></i>
          </div>
          <div>
            <h3 class="text-white font-semibold mb-1">Teléfono</h3>
            <p class="text-slate-400">+507 6250-9318</p>
          </div>
        </div>
        <!-- ... email, ubicación, horario ... -->
      </div>

      <!-- Form -->
      <form class="space-y-6">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <label class="block text-slate-400 mb-2 text-sm">Nombre</label>
            <input type="text" class="w-full px-4 py-3 bg-slate-800/50 border border-slate-700/50 rounded-xl text-white focus:outline-none focus:border-cyan-500 transition-colors" placeholder="Tu nombre" required>
          </div>
          <div>
            <label class="block text-slate-400 mb-2 text-sm">Teléfono</label>
            <input type="tel" class="w-full px-4 py-3 bg-slate-800/50 border border-slate-700/50 rounded-xl text-white focus:outline-none focus:border-cyan-500 transition-colors" placeholder="Tu teléfono">
          </div>
        </div>
        <div>
          <label class="block text-slate-400 mb-2 text-sm">Email</label>
          <input type="email" class="w-full px-4 py-3 bg-slate-800/50 border border-slate-700/50 rounded-xl text-white focus:outline-none focus:border-cyan-500 transition-colors" placeholder="tu@email.com" required>
        </div>
        <div>
          <label class="block text-slate-400 mb-2 text-sm">Mensaje</label>
          <textarea rows="5" class="w-full px-4 py-3 bg-slate-800/50 border border-slate-700/50 rounded-xl text-white focus:outline-none focus:border-cyan-500 transition-colors resize-none" placeholder="¿En qué podemos ayudarte?" required></textarea>
        </div>
        <button type="submit" class="w-full bg-gradient-to-r from-cyan-500 to-purple-500 text-white py-4 rounded-xl font-semibold flex items-center justify-center gap-2 hover:shadow-lg hover:shadow-cyan-500/25 transition-all">
          <i data-lucide="send" class="w-5 h-5"></i>
          Enviar mensaje
        </button>
      </form>
    </div>
  </div>
</section>
```

### Botón flotante de WhatsApp (OBLIGATORIO)

```html
<a href="https://wa.me/50762509318" target="_blank" rel="noopener noreferrer"
   class="fixed bottom-6 right-6 z-50 w-16 h-16 bg-green-500 rounded-full flex items-center justify-center shadow-lg shadow-green-500/30 hover:shadow-green-500/50 transition-all hover:scale-110">
  <i data-lucide="message-circle" class="w-8 h-8 text-white"></i>
  <span class="absolute -top-2 -right-2 w-5 h-5 bg-red-500 rounded-full flex items-center justify-center">
    <span class="w-2 h-2 bg-white rounded-full animate-pulse"></span>
  </span>
</a>
```

### Footer

```html
<footer class="bg-slate-950 py-12 border-t border-slate-800">
  <div class="max-w-7xl mx-auto px-6">
    <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
      <div class="md:col-span-2">
        <div class="flex items-center gap-3 mb-4">
          <div class="w-10 h-10 rounded-lg bg-gradient-to-br from-cyan-500 to-purple-500 flex items-center justify-center">
            <i data-lucide="cpu" class="w-6 h-6 text-white"></i>
          </div>
          <span class="text-xl font-bold text-white">IoT Tech</span>
        </div>
        <p class="text-slate-400 max-w-sm">
          Empresa dedicada al desarrollo de tecnología IoT, reparación de ECU automotriz,
          automatización y programación innovadora en Panamá.
        </p>
      </div>
      <div>
        <h4 class="text-white font-semibold mb-4">Contacto</h4>
        <div class="space-y-3 text-slate-400 text-sm">
          <p>📞 +507 6250-9318</p>
          <p>📍 Panamá</p>
        </div>
      </div>
      <div>
        <h4 class="text-white font-semibold mb-4">Enlaces</h4>
        <ul class="space-y-2">
          <li><a href="#servicios" class="text-slate-400 hover:text-cyan-400 transition-colors">Servicios</a></li>
          <li><a href="#contacto" class="text-slate-400 hover:text-cyan-400 transition-colors">Contacto</a></li>
        </ul>
      </div>
    </div>
    <div class="mt-12 pt-8 border-t border-slate-800 text-center">
      <p class="text-slate-500 text-sm">© 2026 IoT Tech. Todos los derechos reservados.</p>
    </div>
  </div>
</footer>
```

---

## Inicializar Lucide icons

```html
<script>
  // Inicializar todos los iconos Lucide en la página
  lucide.createIcons();
</script>
```

Si añades iconos dinámicamente, llama `lucide.createIcons()` después de añadirlos.

---

## Estilos CSS personalizados (no disponibles en Tailwind)

```css
/* Degradado signature en texto (alternativa a bg-clip-text) */
.gradient-text {
  background: linear-gradient(to right, #22D3EE, #C084FC, #F472B6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  color: transparent;
}

/* Glassmorphism (alternativa a bg-slate-800/50) */
.glass {
  background: rgba(30, 41, 59, 0.5);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(51, 65, 85, 0.5);
}

/* Pulse-slow (animación de blobs) */
@keyframes pulse-slow {
  0%, 100% { opacity: 0.1; }
  50% { opacity: 0.2; }
}

.animate-pulse-slow {
  animation: pulse-slow 4s ease-in-out infinite;
}

/* Scroll suave */
html { scroll-behavior: smooth; }

/* Selección de texto en color de marca */
::selection {
  background-color: rgba(6, 182, 212, 0.3);
  color: #FFFFFF;
}

/* Scrollbar personalizada (opcional) */
::-webkit-scrollbar { width: 10px; }
::-webkit-scrollbar-track { background: #0F172A; }
::-webkit-scrollbar-thumb { background: #334155; border-radius: 5px; }
::-webkit-scrollbar-thumb:hover { background: #06B6D4; }
```

---

## Emails HTML

Los emails NO soportan Tailwind directamente. Usa CSS inline + tablas (regla universal de email HTML).

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Asunto del email</title>
</head>
<body style="margin: 0; padding: 0; background-color: #0F172A; font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background: linear-gradient(135deg, #0F172A 0%, #1E293B 50%, #0F172A 100%);">
    <tr>
      <td align="center" style="padding: 40px 20px;">
        <table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width: 600px;">
          <!-- Header con logo -->
          <tr>
            <td align="center" style="padding: 20px 0;">
              <img src="logo-electrocontrol.jpg" alt="IoT Tech" width="120" height="120" style="border-radius: 16px; display: block;">
            </td>
          </tr>
          <!-- Título con color sólido (no degradado, mala compatibilidad email) -->
          <tr>
            <td align="center" style="padding: 20px;">
              <h1 style="margin: 0; color: #22D3EE; font-size: 36px; font-weight: 700; line-height: 1.2;">
                {{Título}}
              </h1>
            </td>
          </tr>
          <!-- Body -->
          <tr>
            <td style="padding: 20px; color: #CBD5E1; font-size: 16px; line-height: 1.6;">
              {{Contenido}}
            </td>
          </tr>
          <!-- CTA -->
          <tr>
            <td align="center" style="padding: 30px 20px;">
              <a href="https://wa.me/50762509318" style="display: inline-block; background: linear-gradient(to right, #06B6D4, #A855F7); color: #FFFFFF; text-decoration: none; padding: 14px 32px; border-radius: 12px; font-weight: 600; font-size: 16px;">
                Contáctanos por WhatsApp
              </a>
            </td>
          </tr>
          <!-- Footer -->
          <tr>
            <td align="center" style="padding: 20px; border-top: 1px solid #334155;">
              <p style="margin: 0; color: #64748B; font-size: 12px;">
                IoT Tech · Electrocontrol · +507 6250-9318
              </p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>
```

**Reglas email:**
- ❌ NO usar Tailwind (no se aplica en clientes email)
- ❌ NO usar `background-clip: text` (degradado en texto) — usar color sólido
- ❌ NO usar flexbox/grid — usar tablas
- ❌ NO usar `position: fixed` (botón flotante) — poner CTA en el body
- ✅ CSS inline (no `<style>` externo)
- ✅ Tablas anidadas para layout
- ✅ Atributos `width`, `height`, `alt` en todas las imágenes
- ✅ Versión web del email como link alternativo

---

## Responsive design

Tailwind tiene breakpoints estándar. Para Electrocontrol:

| Breakpoint | Tailwind | Uso |
|---|---|---|
| Mobile | (default, < 640px) | 1 columna, todo apilado |
| Tablet | `sm:` (640px+) `md:` (768px+) | 2 columnas para cards |
| Desktop | `lg:` (1024px+) | Layout completo, 2-3 columnas |
| Wide | `xl:` (1280px+) | Contenido max-width 7xl |

**Mobile-first**: empieza con layout mobile, añade `md:`, `lg:` para pantallas más grandes.

---

## Accesibilidad

- `lang="es"` en `<html>`
- `alt` en todas las imágenes (descriptivo, no "imagen1")
- `aria-label` en botones solo con icono
- Contraste WCAG AA mínimo (slate-300+ sobre dark, slate-700+ sobre light)
- Skip link: `<a href="#main" class="sr-only">Saltar al contenido</a>`
- Focus visible: `focus:outline-none focus:ring-2 focus:ring-cyan-500`
- Texto del logo: `alt="IoT Tech - Ir al inicio"`

---

## SEO básico

```html
<head>
  <title>IoT Tech - {{Título}} | Panamá</title>
  <meta name="description" content="{{descripción única, 150-160 chars}}">
  <meta name="keywords" content="IoT, mecatrónica, ECU, automatización, Panamá, Malkom Córdoba">
  <meta property="og:title" content="{{Título}}">
  <meta property="og:description" content="{{descripción}}">
  <meta property="og:image" content="{{URL absoluta al logo}}">
  <meta property="og:url" content="{{URL canónica}}">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="canonical" href="{{URL canónica}}">
  <link rel="icon" type="image/png" href="/favicon-32.png">
</head>
```

---

## Recursos

- **Logo:** `assets/logo-electrocontrol.jpg` (convertir a PNG para web)
- **Tailwind CSS:** [tailwindcss.com](https://tailwindcss.com)
- **Lucide icons:** [lucide.dev](https://lucide.dev)
- **Inter font:** Google Fonts
- **Imágenes:** [unsplash.com](https://unsplash.com), [pexels.com](https://pexels.com)
- **Skill complementaria:** `dev-stack` (rama frontend-design; cargar ANTES)

---

## Checklist antes de entregar

- [ ] ¿Fondo dark en todas las páginas?
- [ ] ¿Degradado cyan→purple→pink en máximo 2 H1?
- [ ] ¿Logo en header?
- [ ] ¿WhatsApp flotante?
- [ ] ¿Botón flotante con `https://wa.me/50762509318`?
- [ ] ¿Datos de contacto correctos?
- [ ] ¿Iconos Lucide con stroke-width 2?
- [ ] ¿Antialiasing activado?
- [ ] ¿Responsive (mobile, tablet, desktop)?
- [ ] ¿Contraste WCAG AA?
- [ ] ¿SEO meta tags completos?
- [ ] ¿Performance (lazy loading imágenes, fuentes preloaded)?
