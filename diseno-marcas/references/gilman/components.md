# Componentes — gilman.pro

Librería de componentes reutilizables. Todos siguen el sistema de diseño gilman.

## 1. BOTONES

### Primary (sólido, fondo de marca)

**HTML/Tailwind:**
```html
<a class="inline-flex items-center gap-2 px-6 py-3 rounded-lg font-semibold text-sm bg-emerald-600 dark:bg-indigo-600 text-white shadow-lg hover:shadow-xl hover:bg-emerald-700 dark:hover:bg-indigo-700 transition-all duration-200">
  <i data-lucide="sparkles" class="w-5 h-5"></i>Acción principal
</a>
```

**Reglas:**
- Fondo: `emerald-600` (claro) / `indigo-600` (dark)
- Hover: `emerald-700` / `indigo-700` + `shadow-xl`
- Padding: `px-6 py-3`
- Border-radius: `rounded-lg` (8px)
- Font: Lato 600, `text-sm` (14px)
- Icono Lucide a la izquierda, `gap-2`
- Transition: `all duration-200`

### Secondary (outline, borde de marca)

```html
<a class="inline-flex items-center gap-2 px-6 py-3 rounded-lg font-medium text-sm border-2 border-emerald-600 dark:border-indigo-500 text-emerald-600 dark:text-indigo-400 hover:bg-emerald-600 dark:hover:bg-indigo-600 hover:text-white shadow-lg hover:shadow-xl transition-all duration-200">
  <i data-lucide="arrow-right" class="w-4 h-4"></i>Acción secundaria
</a>
```

### Ghost (texto + icono, sin borde)

```html
<a class="inline-flex items-center gap-2 px-4 py-2 rounded-lg text-sm text-gray-500 dark:text-slate-400 hover:text-emerald-600 dark:hover:text-cyan-400 transition-colors duration-200">
  <i data-lucide="chevron-right" class="w-4 h-4"></i>Ver más
</a>
```

### Tamaños

| Tamaño | Padding | Font-size | Uso |
|---|---|---|---|
| `sm` | `px-4 py-2` | `text-xs` (12px) | Botones inline, pills |
| `md` | `px-6 py-3` | `text-sm` (14px) | Default — CTAs |
| `lg` | `px-8 py-4` | `text-base` (16px) | Hero CTA |

## 2. CARDS

### Card básica (contenido)

```html
<div class="block bg-gray-50 dark:bg-slate-800/80 rounded-xl p-5 shadow-sm border border-gray-100 dark:border-white/5 hover:border-emerald-300 dark:hover:border-indigo-500/30 hover:shadow-md dark:hover:shadow-lg dark:hover:shadow-indigo-500/10 transition-all duration-300 group">
  <span class="inline-block text-xs font-medium text-emerald-600 dark:text-indigo-400 mb-1">Fecha / categoría</span>
  <h4 class="font-heading font-semibold text-gray-900 dark:text-white group-hover:text-emerald-600 dark:group-hover:text-indigo-400 transition-colors duration-200">Título de la card</h4>
  <p class="text-gray-500 dark:text-slate-400 text-sm">Descripción breve del contenido</p>
</div>
```

### Card con imagen (artículos, certificaciones)

```html
<a class="group block bg-gray-50 dark:bg-slate-800/80 border border-gray-200 dark:border-white/10 rounded-2xl overflow-hidden shadow-md dark:shadow-lg dark:shadow-black/30 hover:border-emerald-300 dark:hover:border-indigo-500/30 hover:shadow-lg dark:hover:shadow-xl dark:hover:shadow-indigo-500/20 transition-all duration-300">
  <div class="h-40 overflow-hidden flex items-center justify-center bg-gray-50 dark:bg-slate-700 p-6">
    <img src="..." alt="..." class="w-full h-full object-contain group-hover:scale-110 transition-transform duration-300">
  </div>
  <div class="p-5">
    <h4 class="font-heading font-semibold text-gray-900 dark:text-white mb-1 group-hover:text-emerald-600 dark:group-hover:text-indigo-400 transition-colors duration-200">Título</h4>
    <p class="text-gray-500 dark:text-slate-400 text-sm">Subtítulo</p>
    <p class="text-gray-400 dark:text-slate-500 text-xs mt-1 line-clamp-2">Descripción...</p>
  </div>
</a>
```

**Reglas de cards:**
- Sin imagen: `rounded-xl` (12px)
- Con imagen: `rounded-2xl` (16px) + `overflow-hidden`
- Padding interno: `p-5` (20px)
- Background: `bg-gray-50` / `dark:bg-slate-800/80`
- Border: `1px gray-100` / `1px white/5`
- Hover: border color → `emerald-300` / `indigo-500/30`
- Sombra: `shadow-sm` → `shadow-md` en hover

## 3. INPUTS / FORMULARIOS

### Input de texto

```html
<div>
  <label for="email" class="block text-sm font-medium text-gray-700 dark:text-slate-300 mb-1.5">Correo electrónico <span class="text-rose-500">*</span></label>
  <input type="email" id="email" name="email" required
    class="w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-slate-600 bg-white dark:bg-slate-800 text-gray-900 dark:text-white placeholder-gray-400 dark:placeholder-slate-500 focus:ring-2 focus:ring-emerald-500 dark:focus:ring-indigo-500 focus:border-transparent outline-none transition-all duration-200"
    placeholder="tu@email.com">
</div>
```

### Textarea

```html
<textarea rows="5"
  class="w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-slate-600 bg-white dark:bg-slate-800 text-gray-900 dark:text-white placeholder-gray-400 dark:placeholder-slate-500 focus:ring-2 focus:ring-emerald-500 dark:focus:ring-indigo-500 focus:border-transparent outline-none transition-all duration-200 resize-none"
  placeholder="Escribe tu mensaje aquí..."></textarea>
```

### Select / dropdown

```html
<select class="w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-slate-600 bg-white dark:bg-slate-800 text-gray-900 dark:text-white focus:ring-2 focus:ring-emerald-500 dark:focus:ring-indigo-500 focus:border-transparent outline-none">
  <option>Opción 1</option>
  <option>Opción 2</option>
</select>
```

**Reglas de inputs:**
- Border-radius: `rounded-xl` (12px)
- Padding: `px-4 py-3`
- Border: `1px gray-200` / `1px slate-600`
- Focus: `ring-2 ring-emerald-500` (claro) / `ring-indigo-500` (dark) + `border-transparent`
- Label: `text-sm font-medium text-gray-700 dark:text-slate-300 mb-1.5`
- Requerido: asterisco `text-rose-500`

## 4. BADGES / PILLS

```html
<span class="inline-block text-xs font-medium text-emerald-600 dark:text-indigo-400">Categoría</span>

<!-- Pill completo -->
<span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium bg-emerald-100 dark:bg-indigo-500/20 text-emerald-700 dark:text-indigo-300">
  <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 dark:bg-indigo-400"></span>
  Activo
</span>
```

## 5. NAVBAR

```html
<nav class="fixed top-0 left-0 right-0 z-50 bg-slate-800 dark:bg-slate-900/80 dark:backdrop-blur-xl border-b border-slate-700/50 dark:border-slate-800/50">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-16">
      <!-- Logo + wordmark -->
      <a href="/" class="flex items-center space-x-2">
        <img src="logo_gilmanpro.svg" alt="Logo" class="w-8 h-8">
        <span class="text-white font-heading font-bold text-lg">gilman.pro</span>
      </a>
      <!-- Links -->
      <div class="hidden md:flex items-center space-x-0.5">
        <a href="/" class="px-3 py-2 rounded-lg text-sm font-medium text-emerald-400 dark:text-cyan-400">Inicio</a>
        <a href="/about" class="px-3 py-2 rounded-lg text-sm font-medium text-gray-300 dark:text-slate-300 hover:text-white dark:hover:text-cyan-400">Sobre mí</a>
      </div>
    </div>
  </div>
</nav>
```

## 6. HERO / PORTADA

```html
<section class="relative min-h-screen flex items-center justify-center bg-emerald-500 dark:bg-indigo-600 overflow-hidden">
  <div class="absolute inset-0 bg-black/10 dark:bg-black/25 z-0"></div>
  <div class="relative z-10 max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-20 text-center">
    <img src="profile.jpg" alt="Profile" class="w-40 h-40 rounded-full border-4 border-white shadow-2xl mx-auto mb-8 object-cover">
    <h1 class="text-4xl md:text-6xl font-heading font-bold text-white mb-4 tracking-tight">Nombre Apellido</h1>
    <h2 class="text-lg md:text-xl text-white/90 dark:text-white/80 font-body font-light mb-6">Cargo | Especialidad | Rol</h2>
    <p class="text-white/80 dark:text-white/70 max-w-2xl mx-auto text-base md:text-lg leading-relaxed mb-10">Descripción breve...</p>
    <div class="flex flex-col md:flex-row items-center justify-center gap-4 flex-wrap">
      <a class="btn-cv-visual inline-flex items-center gap-2 px-6 py-3 rounded-lg font-semibold text-sm bg-emerald-600 text-white shadow-lg hover:shadow-xl"><i data-lucide="sparkles" class="w-5 h-5"></i>CTA Principal</a>
      <a class="inline-flex items-center gap-2 px-6 py-3 rounded-lg font-medium text-sm bg-blue-600 dark:bg-emerald-600 text-white hover:bg-blue-700 shadow-lg hover:shadow-xl"><i data-lucide="file-text" class="w-5 h-5"></i>CTA Secundario</a>
    </div>
  </div>
</section>
```

**Reglas del hero:**
- Fondo: `emerald-500` (claro) / `indigo-600` (dark)
- Overlay: `bg-black/10` / `bg-black/25` para suavizar
- Imagen de perfil: circular, `w-40 h-40`, border `4px white`, `shadow-2xl`
- H1: Montserrat 800, `text-4xl md:text-6xl`, blanco
- H2: Lato 300, `text-lg md:text-xl`, blanco/90
- CTAs: centrados, `gap-4`, separados en columnas en desktop

## 7. SEPARADOR DECORATIVO (signature)

```html
<div class="mt-4 flex items-center justify-center">
  <span class="h-px w-10 bg-emerald-500 dark:bg-indigo-500"></span>
  <span class="mx-2 w-2 h-2 rounded-full bg-emerald-500 dark:bg-indigo-500"></span>
  <span class="h-px w-16 bg-emerald-500 dark:bg-indigo-500"></span>
  <span class="mx-2 w-2 h-2 rounded-full bg-emerald-500 dark:bg-violet-500"></span>
  <span class="h-px w-10 bg-emerald-500 dark:bg-violet-500"></span>
</div>
```

**Siempre bajo cada H2** — es el elemento de marca más distintivo. Línea + punto + línea + punto (violet) + línea.

## 8. FOOTER

```html
<footer class="bg-slate-800 dark:bg-slate-900 border-t border-slate-700/50 dark:border-slate-800/50">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      <div>
        <div class="flex items-center space-x-2 mb-4">
          <img src="logo_gilmanpro.svg" alt="Logo" class="w-6 h-6">
          <span class="text-white font-heading font-bold text-lg">gilman.pro</span>
        </div>
        <p class="text-slate-400 text-sm">Nombre<br>Cargo<br>Ubicación</p>
      </div>
      <div>
        <h3 class="text-white font-heading font-semibold text-sm uppercase tracking-wider mb-4">Enlaces</h3>
        <ul class="space-y-2">
          <li><a href="/" class="text-slate-400 hover:text-white dark:hover:text-cyan-400 text-sm">Inicio</a></li>
        </ul>
      </div>
      <div>
        <h3 class="text-white font-heading font-semibold text-sm uppercase tracking-wider mb-4">Social</h3>
        <div class="flex space-x-4">
          <a class="p-2 rounded-lg bg-slate-700 dark:bg-slate-800 text-slate-400 hover:text-white dark:hover:text-cyan-400"><i data-lucide="linkedin" class="w-5 h-5"></i></a>
        </div>
      </div>
    </div>
    <div class="mt-10 pt-6 border-t border-slate-700/50 dark:border-slate-800/50 text-center">
      <p class="text-slate-500 text-sm">&copy; 2026 Gilberto Castillo — Ing. Telecomunicaciones | Big Data y Data Science | Desarrollador de Soluciones</p>
    </div>
  </div>
</footer>
```

## 9. TIMELINE (línea de tiempo)

Usado en sección "Experiencia":

```html
<div class="relative">
  <div class="absolute left-5 md:left-1/2 top-0 bottom-0 w-px bg-gray-200 dark:bg-slate-700 transform md:-translate-x-px"></div>
  
  <div class="relative flex flex-col md:flex-row items-start mb-10 pl-14 md:pl-0">
    <div class="absolute left-0 md:left-1/2 w-10 h-10 rounded-full bg-emerald-500 dark:bg-indigo-500 flex items-center justify-center shadow-lg transform md:-translate-x-1/2 z-10">
      <i data-lucide="briefcase" class="w-5 h-5 text-white"></i>
    </div>
    <div class="md:w-1/2 md:pr-12 md:text-right">
      <!-- contenido de la card -->
    </div>
  </div>
</div>
```

## 10. SISTEMA DE SOMBRAS

| Token | Tailwind | CSS | Uso |
|---|---|---|---|
| `shadow-sm` | `shadow-sm` | `0 1px 2px 0 rgb(0 0 0 / 0.05)` | Card default |
| `shadow-md` | `shadow-md` | `0 4px 6px -1px rgb(0 0 0 / 0.1)` | Card hover |
| `shadow-lg` | `shadow-lg` | `0 10px 15px -3px rgb(0 0 0 / 0.1)` | Botón default |
| `shadow-xl` | `shadow-xl` | `0 20px 25px -5px rgb(0 0 0 / 0.1)` | Botón hover, card hover dark |
| `shadow-2xl` | `shadow-2xl` | `0 25px 50px -12px rgb(0 0 0 / 0.25)` | Solo en hero/imagen de perfil |
| `shadow-indigo-glow` | custom | `0 10px 15px -3px rgba(99,102,241,0.1)` | Glow dark mode |
