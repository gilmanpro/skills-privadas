# Aplicación a Web/HTML — gilman.pro

Cómo aplicar el branding gilman.pro a sitios web, landing pages, dashboards y apps. **Usa Tailwind CSS** (la skill `dev-stack`, rama frontend-design, ya tiene su propia base; aquí nos enfocamos en el overlay de marca).

## 1. SETUP MÍNIMO (Tailwind CDN)

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>gilman.pro | Mi sitio</title>
  
  <!-- Google Fonts: 4 familias gilman -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&family=Lato:wght@300;400;700&family=Orbitron:wght@400;500;600;700;800;900&family=Rajdhani:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  
  <!-- Tailwind -->
  <script src="https://cdn.tailwindcss.com?plugins=typography"></script>
  
  <!-- Tailwind config gilman -->
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            heading: ['Montserrat', 'sans-serif'],
            body: ['Lato', 'sans-serif'],
            display: ['Orbitron', 'sans-serif'],
            tech: ['Rajdhani', 'sans-serif'],
          }
        }
      }
    }
  </script>
  
  <!-- Estilos gilman -->
  <style>
    body { font-family: 'Lato', sans-serif; }
    .font-heading { font-family: 'Montserrat', sans-serif; }
    .font-body { font-family: 'Lato', sans-serif; }
    .font-display { font-family: 'Orbitron', sans-serif; }
    .font-tech { font-family: 'Rajdhani', sans-serif; }
    
    /* Scrollbar dark mode */
    .dark ::-webkit-scrollbar { width: 8px; }
    .dark ::-webkit-scrollbar-track { background: #0F172A; }
    .dark ::-webkit-scrollbar-thumb { background: #334155; border-radius: 4px; }
    .dark ::-webkit-scrollbar-thumb:hover { background: #475569; }
    
    html { scroll-behavior: smooth; }
    
    /* Smooth fade-in */
    @keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
    .animate-fade-in { animation: fadeIn 0.6s ease-out forwards; }
    
    /* Pulse glow para CTAs críticos */
    @keyframes pulse-glow-emerald {
      0%, 100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.4); }
      50% { box-shadow: 0 0 0 8px rgba(16, 185, 129, 0); }
    }
    .animate-pulse-glow-emerald { animation: pulse-glow-emerald 2s infinite; }
    
    @keyframes pulse-glow-indigo {
      0%, 100% { box-shadow: 0 0 0 0 rgba(99, 102, 241, 0.4); }
      50% { box-shadow: 0 0 0 8px rgba(99, 102, 241, 0); }
    }
    .dark .animate-pulse-glow-emerald { animation: pulse-glow-indigo 2s infinite; }
  </style>
</head>
<body class="bg-white dark:bg-slate-900 text-gray-900 dark:text-slate-100 font-body antialiased transition-colors duration-300">
  
  <!-- Toggle dark mode script -->
  <script>
    (function() {
      var theme = localStorage.getItem('theme');
      if (theme !== 'light') {
        document.documentElement.classList.add('dark');
      }
    })();
  </script>
  
  <!-- Tu contenido aquí -->
</body>
</html>
```

## 2. PALETA EN TAILWIND (RESUMEN DE TOKENS)

Tailwind ya tiene todos los colores que necesitamos. Solo úsalos directamente:

```html
<!-- Claro -->
<div class="bg-white text-gray-900 border-gray-200">
<div class="bg-slate-50 text-gray-700">
<div class="bg-emerald-500 text-white">Emerald primary</div>
<div class="bg-emerald-600 hover:bg-emerald-700 text-white">Botón primary</div>
<div class="text-emerald-600">Link/acentos</div>
<div class="bg-blue-600 text-white">Botón secondary</div>

<!-- Oscuro -->
<div class="dark:bg-slate-900 dark:text-white">
<div class="dark:bg-slate-800/80 dark:border-white/5">Card dark</div>
<div class="dark:bg-indigo-600 dark:hover:bg-indigo-700">Botón dark</div>
<div class="dark:text-indigo-400">Link dark</div>
<div class="dark:text-violet-500">Acento violet</div>
```

## 3. COMPONENTES REUTILIZABLES (copiar/pegar)

### 3.1 Navbar

```html
<nav class="fixed top-0 left-0 right-0 z-50 bg-slate-800 dark:bg-slate-900/80 dark:backdrop-blur-xl border-b border-slate-700/50 dark:border-slate-800/50">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-16">
      <a href="/" class="flex items-center space-x-2">
        <img src="logo_gilmanpro.svg" alt="gilman.pro" class="w-8 h-8">
        <span class="text-white font-heading font-bold text-lg">gilman.pro</span>
      </a>
      
      <div class="hidden md:flex items-center space-x-1">
        <a href="/" class="px-3 py-2 rounded-lg text-sm font-medium text-emerald-400 dark:text-cyan-400">Inicio</a>
        <a href="#about" class="px-3 py-2 rounded-lg text-sm font-medium text-gray-300 dark:text-slate-300 hover:text-white dark:hover:text-cyan-400 transition-colors">Sobre mí</a>
        <a href="#work" class="px-3 py-2 rounded-lg text-sm font-medium text-gray-300 dark:text-slate-300 hover:text-white dark:hover:text-cyan-400 transition-colors">Proyectos</a>
        <a href="#contact" class="px-3 py-2 rounded-lg text-sm font-medium text-gray-300 dark:text-slate-300 hover:text-white dark:hover:text-cyan-400 transition-colors">Contacto</a>
      </div>
      
      <button id="theme-toggle" class="p-2 rounded-lg text-gray-300 hover:text-white dark:text-slate-300 dark:hover:text-cyan-400 hover:bg-slate-700 dark:hover:bg-slate-800 transition-colors">
        <svg class="w-5 h-5 dark:hidden" fill="currentColor" viewBox="0 0 20 20"><path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/></svg>
        <svg class="w-5 h-5 hidden dark:block" fill="currentColor" viewBox="0 0 20 20"><path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z"/></svg>
      </button>
    </div>
  </div>
</nav>

<script>
  document.getElementById('theme-toggle').addEventListener('click', () => {
    document.documentElement.classList.toggle('dark');
    localStorage.setItem('theme', document.documentElement.classList.contains('dark') ? 'dark' : 'light');
  });
</script>
```

### 3.2 Hero / Portada

```html
<section class="relative min-h-screen flex items-center justify-center bg-emerald-500 dark:bg-indigo-600 overflow-hidden pt-16">
  <div class="absolute inset-0 bg-black/10 dark:bg-black/25 z-0"></div>
  
  <div class="relative z-10 max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-20 text-center">
    <img src="profile.jpg" alt="Profile" class="w-40 h-40 rounded-full border-4 border-white shadow-2xl mx-auto mb-8 object-cover">
    
    <h1 class="text-4xl md:text-6xl font-heading font-bold text-white mb-4 tracking-tight animate-fade-in">
      Tu Nombre
    </h1>
    <h2 class="text-lg md:text-2xl text-white/90 dark:text-white/80 font-body font-light mb-6 animate-fade-in">
      Tu cargo | Tu especialidad
    </h2>
    <p class="text-white/80 dark:text-white/70 max-w-2xl mx-auto text-base md:text-lg leading-relaxed mb-10 animate-fade-in">
      Descripción breve de tu propuesta de valor.
    </p>
    
    <div class="flex flex-col md:flex-row items-center justify-center gap-4 flex-wrap">
      <a href="#cta" class="inline-flex items-center gap-2 px-6 py-3 rounded-lg font-semibold text-sm bg-emerald-600 text-white shadow-lg hover:shadow-xl hover:bg-emerald-700 transition-all duration-200">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
        CTA Principal
      </a>
      <a href="#secundario" class="inline-flex items-center gap-2 px-6 py-3 rounded-lg font-medium text-sm bg-white text-emerald-700 hover:bg-slate-50 shadow-lg hover:shadow-xl transition-all duration-200">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
        CTA Secundario
      </a>
    </div>
  </div>
</section>
```

### 3.3 H2 con separador decorativo (signature)

```html
<div class="text-center mb-12">
  <h2 class="text-3xl md:text-4xl font-heading font-bold text-gray-900 dark:text-white mb-2">
    Experiencia
  </h2>
  <div class="mt-4 flex items-center justify-center">
    <span class="h-px w-10 bg-emerald-500 dark:bg-indigo-500"></span>
    <span class="mx-2 w-2 h-2 rounded-full bg-emerald-500 dark:bg-indigo-500"></span>
    <span class="h-px w-16 bg-emerald-500 dark:bg-indigo-500"></span>
    <span class="mx-2 w-2 h-2 rounded-full bg-emerald-500 dark:bg-violet-500"></span>
    <span class="h-px w-10 bg-emerald-500 dark:bg-violet-500"></span>
  </div>
</div>
```

### 3.4 Card de proyecto

```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
  <a href="#" class="group block bg-gray-50 dark:bg-slate-800/80 border border-gray-200 dark:border-white/10 rounded-2xl overflow-hidden shadow-md dark:shadow-lg dark:shadow-black/30 hover:border-emerald-300 dark:hover:border-indigo-500/30 hover:shadow-lg dark:hover:shadow-xl dark:hover:shadow-indigo-500/20 transition-all duration-300">
    <div class="h-40 overflow-hidden flex items-center justify-center bg-gray-100 dark:bg-slate-700 p-6">
      <img src="project.jpg" alt="Project" class="w-full h-full object-contain group-hover:scale-110 transition-transform duration-300">
    </div>
    <div class="p-5">
      <h4 class="font-heading font-semibold text-gray-900 dark:text-white mb-1 group-hover:text-emerald-600 dark:group-hover:text-indigo-400 transition-colors">
        Nombre del Proyecto
      </h4>
      <p class="text-gray-500 dark:text-slate-400 text-sm">Subtítulo breve</p>
      <p class="text-gray-400 dark:text-slate-500 text-xs mt-1 line-clamp-2">
        Descripción corta del proyecto en máximo 2 líneas.
      </p>
    </div>
  </a>
</div>
```

### 3.5 Sección de contacto (formulario)

```html
<section class="py-20 bg-white dark:bg-slate-900">
  <div class="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-12">
      <h2 class="text-3xl md:text-4xl font-heading font-bold text-gray-900 dark:text-white mb-2">Contáctame</h2>
      <div class="mt-4 flex items-center justify-center">
        <span class="h-px w-10 bg-emerald-500 dark:bg-indigo-500"></span>
        <span class="mx-2 w-2 h-2 rounded-full bg-emerald-500 dark:bg-indigo-500"></span>
        <span class="h-px w-16 bg-emerald-500 dark:bg-indigo-500"></span>
        <span class="mx-2 w-2 h-2 rounded-full bg-emerald-500 dark:bg-violet-500"></span>
        <span class="h-px w-10 bg-emerald-500 dark:bg-violet-500"></span>
      </div>
    </div>
    
    <form class="space-y-5">
      <div>
        <label for="name" class="block text-sm font-medium text-gray-700 dark:text-slate-300 mb-1.5">Nombre <span class="text-rose-500">*</span></label>
        <input type="text" id="name" name="name" required
          class="w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-slate-600 bg-white dark:bg-slate-800 text-gray-900 dark:text-white placeholder-gray-400 dark:placeholder-slate-500 focus:ring-2 focus:ring-emerald-500 dark:focus:ring-indigo-500 focus:border-transparent outline-none transition-all duration-200"
          placeholder="Tu nombre completo">
      </div>
      <div>
        <label for="email" class="block text-sm font-medium text-gray-700 dark:text-slate-300 mb-1.5">Email <span class="text-rose-500">*</span></label>
        <input type="email" id="email" name="email" required
          class="w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-slate-600 bg-white dark:bg-slate-800 text-gray-900 dark:text-white placeholder-gray-400 dark:placeholder-slate-500 focus:ring-2 focus:ring-emerald-500 dark:focus:ring-indigo-500 focus:border-transparent outline-none transition-all duration-200"
          placeholder="tu@email.com">
      </div>
      <div>
        <label for="msg" class="block text-sm font-medium text-gray-700 dark:text-slate-300 mb-1.5">Mensaje <span class="text-rose-500">*</span></label>
        <textarea id="msg" name="msg" rows="5" required
          class="w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-slate-600 bg-white dark:bg-slate-800 text-gray-900 dark:text-white placeholder-gray-400 dark:placeholder-slate-500 focus:ring-2 focus:ring-emerald-500 dark:focus:ring-indigo-500 focus:border-transparent outline-none transition-all duration-200 resize-none"
          placeholder="Escribe tu mensaje..."></textarea>
      </div>
      <button type="submit" class="inline-flex items-center gap-2 px-6 py-3 rounded-lg font-medium text-sm bg-emerald-600 dark:bg-indigo-600 text-white hover:bg-emerald-700 dark:hover:bg-indigo-700 shadow-lg hover:shadow-xl transition-all duration-200">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"/></svg>
        Enviar mensaje
      </button>
    </form>
  </div>
</section>
```

### 3.6 Footer

```html
<footer class="bg-slate-800 dark:bg-slate-900 border-t border-slate-700/50 dark:border-slate-800/50">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      <div>
        <div class="flex items-center space-x-2 mb-4">
          <img src="logo_gilmanpro.svg" alt="Logo" class="w-6 h-6">
          <span class="text-white font-heading font-bold text-lg">gilman.pro</span>
        </div>
        <p class="text-slate-400 text-sm">
          Gilberto Castillo<br>
          Ingeniero en Telecomunicaciones<br>
          Especialista en Big Data y Data Science<br>
          Panamá
        </p>
      </div>
      <div>
        <h3 class="text-white font-heading font-semibold text-sm uppercase tracking-wider mb-4">Enlaces</h3>
        <ul class="space-y-2">
          <li><a href="/" class="text-slate-400 hover:text-white dark:hover:text-cyan-400 text-sm transition-colors">Inicio</a></li>
          <li><a href="/about" class="text-slate-400 hover:text-white dark:hover:text-cyan-400 text-sm transition-colors">Sobre mí</a></li>
        </ul>
      </div>
      <div>
        <h3 class="text-white font-heading font-semibold text-sm uppercase tracking-wider mb-4">Social</h3>
        <div class="flex space-x-4">
          <a href="#" class="p-2 rounded-lg bg-slate-700 dark:bg-slate-800 text-slate-400 hover:text-white dark:hover:text-cyan-400 hover:bg-slate-600 dark:hover:bg-slate-700 transition-colors">
            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.063 2.063 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
          </a>
          <a href="#" class="p-2 rounded-lg bg-slate-700 dark:bg-slate-800 text-slate-400 hover:text-white dark:hover:text-cyan-400 hover:bg-slate-600 dark:hover:bg-slate-700 transition-colors">
            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.373 0 12c0 5.303 3.438 9.8 8.205 11.387.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61-.546-1.387-1.333-1.756-1.333-1.756-1.09-.745.082-.73.082-.73 1.205.084 1.84 1.236 1.84 1.236 1.07 1.835 2.81 1.305 3.495.998.108-.775.42-1.305.762-1.605-2.665-.305-5.466-1.334-5.466-5.93 0-1.31.467-2.382 1.235-3.22-.124-.303-.535-1.524.118-3.176 0 0 1.008-.323 3.3 1.23a11.5 11.5 0 016.003 0c2.29-1.553 3.297-1.23 3.297-1.23.655 1.652.244 2.873.12 3.176.77.838 1.233 1.91 1.233 3.22 0 4.608-2.807 5.62-5.48 5.92.43.37.815 1.103.815 2.222 0 1.604-.015 2.896-.015 3.286 0 .322.218.694.825.576C20.565 21.795 24 17.297 24 12c0-6.627-5.373-12-12-12z"/></svg>
          </a>
        </div>
      </div>
    </div>
    <div class="mt-10 pt-6 border-t border-slate-700/50 dark:border-slate-800/50 text-center">
      <p class="text-slate-500 text-sm">© 2026 Gilberto Castillo — Ing. Telecomunicaciones | Big Data y Data Science | Desarrollador de Soluciones</p>
    </div>
  </div>
</footer>
```

## 4. PALETA CUSTOM (opcional, via Tailwind config)

Si quieres tokens con nombres semánticos:

```js
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        gilman: {
          emerald:    '#10B981',
          'emerald-600': '#059669',
          'emerald-700': '#047857',
          'emerald-50':  '#ECFDF5',
          cyan:       '#22D3EE',
          'cyan-500': '#06B6D4',
          blue:       '#2563EB',
          violet:     '#8B5CF6',
          slate:      '#1E293B',
          'slate-50': '#F8FAFC',
        },
        dark: {
          primary:    '#6366F1',
          'primary-600': '#4F46E5',
          bg:         '#0F172A',
          'bg-alt':   '#1E293B',
        }
      }
    }
  }
}
```

Uso: `<div class="bg-gilman-emerald text-gilman-emerald-50">`

## 5. LANDING PAGE COMPLETA (template copy-paste)

```html
<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>gilman.pro | Landing</title>
  <link rel="icon" type="image/svg+xml" href="logo_gilmanpro.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&family=Lato:wght@300;400;700&family=Orbitron:wght@400;500;600;700;800;900&family=Rajdhani:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: { extend: { fontFamily: {
        heading: ['Montserrat', 'sans-serif'],
        body: ['Lato', 'sans-serif'],
        display: ['Orbitron', 'sans-serif'],
        tech: ['Rajdhani', 'sans-serif'],
      }}}
    }
  </script>
  <style>body { font-family: 'Lato', sans-serif; } html { scroll-behavior: smooth; }</style>
  <script>(function(){var t=localStorage.getItem('theme');if(t!=='light')document.documentElement.classList.add('dark');})();</script>
</head>
<body class="bg-white dark:bg-slate-900 text-gray-900 dark:text-slate-100 antialiased transition-colors duration-300">
  
  <!-- NAV -->
  <nav class="fixed top-0 left-0 right-0 z-50 bg-slate-800 dark:bg-slate-900/80 dark:backdrop-blur-xl border-b border-slate-700/50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <a href="#" class="flex items-center space-x-2">
          <img src="logo_gilmanpro.svg" alt="gilman.pro" class="w-8 h-8">
          <span class="text-white font-heading font-bold text-lg">gilman.pro</span>
        </a>
        <div class="hidden md:flex items-center space-x-1">
          <a href="#features" class="px-3 py-2 rounded-lg text-sm text-gray-300 hover:text-white dark:hover:text-cyan-400">Features</a>
          <a href="#pricing" class="px-3 py-2 rounded-lg text-sm text-gray-300 hover:text-white dark:hover:text-cyan-400">Precios</a>
          <a href="#contact" class="px-3 py-2 rounded-lg text-sm text-gray-300 hover:text-white dark:hover:text-cyan-400">Contacto</a>
        </div>
        <button onclick="document.documentElement.classList.toggle('dark');localStorage.setItem('theme',document.documentElement.classList.contains('dark')?'dark':'light')" class="p-2 rounded-lg text-gray-300 hover:text-white dark:text-slate-300 dark:hover:text-cyan-400">
          <svg class="w-5 h-5 dark:hidden" fill="currentColor" viewBox="0 0 20 20"><path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/></svg>
          <svg class="w-5 h-5 hidden dark:block" fill="currentColor" viewBox="0 0 20 20"><path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
        </button>
      </div>
    </div>
  </nav>
  
  <!-- HERO -->
  <section class="relative min-h-screen flex items-center justify-center bg-emerald-500 dark:bg-indigo-600 overflow-hidden pt-16">
    <div class="absolute inset-0 bg-black/10 dark:bg-black/25"></div>
    <div class="relative max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-20 text-center">
      <h1 class="text-4xl md:text-6xl font-heading font-bold text-white mb-4 tracking-tight">Tu Producto</h1>
      <p class="text-lg md:text-xl text-white/90 font-body font-light mb-10">Subtítulo que explica el valor en una línea.</p>
      <div class="flex flex-col md:flex-row items-center justify-center gap-4">
        <a href="#cta" class="inline-flex items-center gap-2 px-6 py-3 rounded-lg font-semibold text-sm bg-emerald-600 text-white shadow-lg hover:shadow-xl hover:bg-emerald-700 transition-all">Empezar gratis</a>
        <a href="#demo" class="inline-flex items-center gap-2 px-6 py-3 rounded-lg font-medium text-sm bg-white text-emerald-700 hover:bg-slate-50 shadow-lg hover:shadow-xl transition-all">Ver demo</a>
      </div>
    </div>
  </section>
  
  <!-- FEATURES -->
  <section id="features" class="py-20 bg-white dark:bg-slate-900">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-12">
        <h2 class="text-3xl md:text-4xl font-heading font-bold text-gray-900 dark:text-white mb-2">Features</h2>
        <div class="mt-4 flex items-center justify-center">
          <span class="h-px w-10 bg-emerald-500 dark:bg-indigo-500"></span>
          <span class="mx-2 w-2 h-2 rounded-full bg-emerald-500 dark:bg-indigo-500"></span>
          <span class="h-px w-16 bg-emerald-500 dark:bg-indigo-500"></span>
          <span class="mx-2 w-2 h-2 rounded-full bg-emerald-500 dark:bg-violet-500"></span>
          <span class="h-px w-10 bg-emerald-500 dark:bg-violet-500"></span>
        </div>
      </div>
      
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <!-- Repite esta card por cada feature -->
        <div class="block bg-gray-50 dark:bg-slate-800/80 border border-gray-100 dark:border-white/5 rounded-xl p-6 hover:border-emerald-300 dark:hover:border-indigo-500/30 hover:shadow-md dark:hover:shadow-lg dark:hover:shadow-indigo-500/10 transition-all duration-300 group">
          <div class="w-12 h-12 rounded-lg bg-emerald-100 dark:bg-indigo-500/20 flex items-center justify-center mb-4 group-hover:bg-emerald-500 dark:group-hover:bg-indigo-500 transition-colors">
            <svg class="w-6 h-6 text-emerald-600 dark:text-indigo-400 group-hover:text-white dark:group-hover:text-white transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
          </div>
          <h3 class="font-heading font-semibold text-gray-900 dark:text-white mb-2 group-hover:text-emerald-600 dark:group-hover:text-indigo-400 transition-colors">Feature 1</h3>
          <p class="text-gray-500 dark:text-slate-400 text-sm">Descripción del feature en una o dos líneas.</p>
        </div>
      </div>
    </div>
  </section>
  
  <!-- CTA / CONTACTO -->
  <section id="contact" class="py-20 bg-gray-50 dark:bg-slate-800">
    <div class="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <h2 class="text-3xl md:text-4xl font-heading font-bold text-gray-900 dark:text-white mb-4">¿Listo para empezar?</h2>
      <p class="text-gray-500 dark:text-slate-400 text-lg mb-8">Contáctame y te respondo en menos de 24 horas.</p>
      <a href="mailto:contacto@gilman.pro" class="inline-flex items-center gap-2 px-8 py-4 rounded-lg font-semibold text-base bg-emerald-600 dark:bg-indigo-600 text-white hover:bg-emerald-700 dark:hover:bg-indigo-700 shadow-lg hover:shadow-xl transition-all duration-200 animate-pulse-glow-emerald">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
        Enviar mensaje
      </a>
    </div>
  </section>
  
  <!-- FOOTER -->
  <footer class="bg-slate-800 dark:bg-slate-900 border-t border-slate-700/50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 text-center">
      <p class="text-slate-500 text-sm">© 2026 gilman.pro | Gilberto Castillo — Ing. Telecomunicaciones | Big Data y Data Science</p>
    </div>
  </footer>
</body>
</html>
```

## 6. DASHBOARD

Para dashboards con marca gilman:

```html
<div class="min-h-screen bg-slate-50 dark:bg-slate-900">
  <!-- Sidebar -->
  <aside class="fixed top-0 left-0 w-64 h-full bg-slate-800 dark:bg-slate-900 border-r border-slate-700/50">
    <div class="p-6 border-b border-slate-700/50">
      <div class="flex items-center space-x-2">
        <img src="logo_gilmanpro.svg" class="w-8 h-8">
        <span class="text-white font-heading font-bold">gilman.pro</span>
      </div>
    </div>
    <nav class="p-4 space-y-1">
      <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg bg-emerald-500/10 text-emerald-400">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
        Dashboard
      </a>
      <a href="#" class="flex items-center gap-3 px-3 py-2 rounded-lg text-slate-300 hover:bg-slate-700/50">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>
        Reportes
      </a>
    </nav>
  </aside>
  
  <!-- Main -->
  <main class="ml-64 p-8">
    <h1 class="text-3xl font-heading font-bold text-gray-900 dark:text-white mb-2">Dashboard</h1>
    <div class="mt-4 flex items-center mb-8">
      <span class="h-px w-10 bg-emerald-500 dark:bg-indigo-500"></span>
      <span class="mx-2 w-2 h-2 rounded-full bg-emerald-500 dark:bg-indigo-500"></span>
      <span class="h-px w-16 bg-emerald-500 dark:bg-indigo-500"></span>
      <span class="mx-2 w-2 h-2 rounded-full bg-emerald-500 dark:bg-violet-500"></span>
      <span class="h-px w-10 bg-emerald-500 dark:bg-violet-500"></span>
    </div>
    
    <!-- Stats cards -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
      <div class="bg-white dark:bg-slate-800/80 rounded-xl p-5 border border-gray-100 dark:border-white/5">
        <p class="text-sm text-gray-500 dark:text-slate-400">Usuarios</p>
        <p class="text-3xl font-display font-bold text-emerald-600 dark:text-indigo-400 mt-1">12,458</p>
      </div>
    </div>
  </main>
</div>
```

## 7. REGLAS

1. **Tailwind CSS** via CDN (más rápido) o compilado (mejor performance).
2. **Google Fonts** para las 4 familias.
3. **Logo SVG** en navbar, footer y favicon.
4. **Separador signature** bajo cada H2.
5. **Modo dark/light** con toggle en navbar (persistido en localStorage).
6. **Imágenes** en `object-contain` (logos) o `object-cover` (fotos).
7. **Iconos** Lucide (mismo set que gilman.pro oficial).
8. **Transiciones** `duration-200` o `duration-300`, NUNCA más de 500ms.
9. **Responsive:** mobile-first; usar `md:` y `lg:` para breakpoints.
10. **Tipografía:**
    - Body: `font-body` o implícito
    - H1-H4: `font-heading`
    - Números de impacto: `font-display`
    - Wordmark: `font-tech`
11. **Espaciado:** `py-20` (5rem) en secciones, `gap-6` en grids.
12. **Container:** `max-w-7xl mx-auto px-4 sm:px-6 lg:px-8`.

## 8. PERFORMANCE

- Cargar Google Fonts con `display=swap` para evitar FOIT.
- Preconnect a `fonts.googleapis.com` y `fonts.gstatic.com`.
- Para producción: NO uses Tailwind CDN, compílalo con PostCSS.
- Comprimir SVG con SVGO antes de producción.
- Lazy load de imágenes con `loading="lazy"`.

## 9. ERRORES COMUNES

- ❌ Olvidar `darkMode: 'class'` en tailwind config → dark mode no funciona
- ❌ Usar `bg-blue-500` (azul claro) en lugar de `bg-blue-600` → fuera de marca
- ❌ Olvidar `prefers-reduced-motion` → mala accesibilidad
- ❌ Texto blanco sobre `bg-emerald-500` (contraste 3.16) → ilegible para párrafo
- ❌ Olvidar `pt-16` en el hero → el navbar fixed lo tapa
- ❌ Usar `font-bold` con Montserrat 400 → se ve igual (no hay 400 bold)
- ❌ No poner `lang="es"` en `<html>` → problemas de accesibilidad
- ❌ `text-gray-500` para texto principal → contraste pobre sobre blanco
