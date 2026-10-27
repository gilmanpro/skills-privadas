# Componentes de Referencia

Ejemplos listos para copiar en proyectos frontend-design.

## Navbar

```html
<nav x-data="{ open: false }" class="fixed top-0 inset-x-0 z-50 bg-gray-950/80 backdrop-blur-xl border-b border-white/5">
  <div class="max-w-7xl mx-auto px-4 h-16 flex items-center justify-between">
    <a href="#" class="font-display font-bold text-xl">Logo</a>
    <div class="hidden md:flex items-center gap-8">
      <a href="#features" class="text-sm text-gray-300 hover:text-white transition-colors">Features</a>
      <a href="#pricing" class="text-sm text-gray-300 hover:text-white transition-colors">Pricing</a>
      <a href="#" class="px-4 py-2 bg-brand-500 hover:bg-brand-600 rounded-lg text-sm font-medium transition-all shadow-lg shadow-brand-500/25">Get Started</a>
    </div>
    <button @click="open = !open" class="md:hidden p-2"><i data-lucide="menu" class="w-6 h-6"></i></button>
  </div>
  <div x-show="open" x-transition class="md:hidden border-t border-white/5 bg-gray-950/95">
    <div class="px-4 py-4 space-y-3">
      <a href="#features" class="block text-sm py-2">Features</a>
      <a href="#pricing" class="block text-sm py-2">Pricing</a>
    </div>
  </div>
</nav>
```

## Hero

```html
<section class="min-h-screen flex flex-col justify-center items-center text-center px-4 relative overflow-hidden">
  <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-brand-500/20 via-transparent to-transparent"></div>
  <div class="relative z-10 max-w-4xl space-y-8 animate-fade-in">
    <span class="inline-flex items-center gap-2 px-4 py-1.5 bg-brand-500/10 text-brand-400 rounded-full text-sm font-medium border border-brand-500/20">
      <i data-lucide="sparkles" class="w-3.5 h-3.5"></i> Introducing Something New
    </span>
    <h1 class="font-display text-5xl md:text-7xl font-bold tracking-tight leading-[1.1]">
      Build products <span class="bg-gradient-to-r from-brand-400 via-violet-400 to-brand-400 bg-clip-text text-transparent">beautifully</span>
    </h1>
    <p class="text-lg md:text-xl text-gray-400 max-w-2xl mx-auto">Compelling value prop. Two lines max.</p>
    <div class="flex flex-wrap justify-center gap-4 pt-4">
      <a href="#" class="group inline-flex items-center gap-2 px-8 py-3.5 bg-brand-500 hover:bg-brand-600 rounded-xl font-semibold transition-all shadow-xl shadow-brand-500/25 hover:-translate-y-0.5">
        Start free trial <i data-lucide="arrow-right" class="w-4 h-4 group-hover:translate-x-1 transition-transform"></i>
      </a>
      <a href="#" class="inline-flex items-center gap-2 px-8 py-3.5 bg-white/5 hover:bg-white/10 rounded-xl font-semibold transition-all border border-white/10">
        <i data-lucide="play" class="w-4 h-4"></i> Watch demo
      </a>
    </div>
  </div>
</section>
```

## Features Bento Grid

```html
<section class="max-w-7xl mx-auto px-4 py-24">
  <h2 class="font-display text-4xl md:text-5xl font-bold text-center mb-16">Everything you need</h2>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
    <div class="md:col-span-2 p-8 rounded-3xl bg-white/[0.03] border border-white/5 hover:bg-white/[0.06] hover:border-brand-500/20 transition-all duration-500 group">
      <div class="w-12 h-12 bg-brand-500/10 rounded-2xl flex items-center justify-center mb-5 group-hover:scale-110 transition-transform">
        <i data-lucide="zap" class="w-6 h-6 text-brand-400"></i>
      </div>
      <h3 class="font-display font-semibold text-xl mb-2">Lightning Fast</h3>
      <p class="text-gray-400 text-sm">Sub-second response times globally.</p>
    </div>
    <div class="p-8 rounded-3xl bg-white/[0.03] border border-white/5 hover:bg-white/[0.06] hover:border-emerald-500/20 transition-all duration-500 group">
      <div class="w-12 h-12 bg-emerald-500/10 rounded-2xl flex items-center justify-center mb-5 group-hover:scale-110 transition-transform">
        <i data-lucide="shield" class="w-6 h-6 text-emerald-400"></i>
      </div>
      <h3 class="font-display font-semibold text-xl mb-2">Secure</h3>
      <p class="text-gray-400 text-sm">SOC 2 compliant, end-to-end encryption.</p>
    </div>
    <div class="p-8 rounded-3xl bg-white/[0.03] border border-white/5 hover:bg-white/[0.06] hover:border-violet-500/20 transition-all duration-500 group">
      <div class="w-12 h-12 bg-violet-500/10 rounded-2xl flex items-center justify-center mb-5 group-hover:scale-110 transition-transform">
        <i data-lucide="smartphone" class="w-6 h-6 text-violet-400"></i>
      </div>
      <h3 class="font-display font-semibold text-xl mb-2">Mobile First</h3>
      <p class="text-gray-400 text-sm">Stunning on every device.</p>
    </div>
    <div class="md:col-span-2 p-8 rounded-3xl bg-white/[0.03] border border-white/5 hover:bg-white/[0.06] hover:border-amber-500/20 transition-all duration-500 group">
      <div class="w-12 h-12 bg-amber-500/10 rounded-2xl flex items-center justify-center mb-5 group-hover:scale-110 transition-transform">
        <i data-lucide="bar-chart-3" class="w-6 h-6 text-amber-400"></i>
      </div>
      <h3 class="font-display font-semibold text-xl mb-2">Advanced Analytics</h3>
      <p class="text-gray-400 text-sm">Real-time dashboards with AI-powered insights.</p>
    </div>
  </div>
</section>
```

## Pricing

```html
<section class="max-w-7xl mx-auto px-4 py-24">
  <h2 class="font-display text-4xl md:text-5xl font-bold text-center mb-16">Simple, transparent pricing</h2>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-5xl mx-auto">
    <div class="p-8 rounded-3xl bg-white/[0.02] border border-white/5 flex flex-col">
      <h3 class="font-display font-semibold text-lg mb-2">Starter</h3>
      <p class="text-gray-400 text-sm mb-6">For individuals.</p>
      <div class="mb-6"><span class="font-display text-5xl font-bold">$0</span><span class="text-gray-400 text-sm">/mo</span></div>
      <ul class="space-y-3 mb-8 flex-1">
        <li class="flex gap-3 text-sm"><i data-lucide="check" class="w-4 h-4 text-emerald-400"></i> Up to 5 projects</li>
        <li class="flex gap-3 text-sm"><i data-lucide="check" class="w-4 h-4 text-emerald-400"></i> Basic analytics</li>
      </ul>
      <a href="#" class="block text-center py-3 bg-white/5 hover:bg-white/10 rounded-xl font-semibold text-sm border border-white/10">Get Started</a>
    </div>
    <div class="p-8 rounded-3xl bg-brand-500/5 border border-brand-500/20 ring-1 ring-brand-500/50 flex flex-col relative">
      <span class="absolute -top-3 left-1/2 -translate-x-1/2 px-4 py-1 bg-brand-500 text-white text-xs font-semibold rounded-full">Popular</span>
      <h3 class="font-display font-semibold text-lg mb-2">Pro</h3>
      <p class="text-gray-400 text-sm mb-6">For teams.</p>
      <div class="mb-6"><span class="font-display text-5xl font-bold">$29</span><span class="text-gray-400 text-sm">/mo</span></div>
      <ul class="space-y-3 mb-8 flex-1">
        <li class="flex gap-3 text-sm"><i data-lucide="check" class="w-4 h-4 text-emerald-400"></i> Unlimited projects</li>
        <li class="flex gap-3 text-sm"><i data-lucide="check" class="w-4 h-4 text-emerald-400"></i> Advanced analytics</li>
        <li class="flex gap-3 text-sm"><i data-lucide="check" class="w-4 h-4 text-emerald-400"></i> Priority support</li>
      </ul>
      <a href="#" class="block text-center py-3 bg-brand-500 hover:bg-brand-600 rounded-xl font-semibold text-sm shadow-lg shadow-brand-500/25">Start Trial</a>
    </div>
    <div class="p-8 rounded-3xl bg-white/[0.02] border border-white/5 flex flex-col">
      <h3 class="font-display font-semibold text-lg mb-2">Enterprise</h3>
      <p class="text-gray-400 text-sm mb-6">For organizations.</p>
      <div class="mb-6"><span class="font-display text-5xl font-bold">$99</span><span class="text-gray-400 text-sm">/mo</span></div>
      <ul class="space-y-3 mb-8 flex-1">
        <li class="flex gap-3 text-sm"><i data-lucide="check" class="w-4 h-4 text-emerald-400"></i> Everything in Pro</li>
        <li class="flex gap-3 text-sm"><i data-lucide="check" class="w-4 h-4 text-emerald-400"></i> SSO & SAML</li>
      </ul>
      <a href="#" class="block text-center py-3 bg-white/5 hover:bg-white/10 rounded-xl font-semibold text-sm border border-white/10">Contact Sales</a>
    </div>
  </div>
</section>
```

## Footer

```html
<footer class="border-t border-white/5">
  <div class="max-w-7xl mx-auto px-4 py-16">
    <div class="grid grid-cols-2 md:grid-cols-5 gap-8 mb-12">
      <div class="col-span-2">
        <a href="#" class="font-display font-bold text-xl mb-4 block">Logo</a>
        <p class="text-gray-400 text-sm max-w-xs">Building the future with design-first engineering.</p>
      </div>
      <div><h4 class="font-semibold text-sm mb-4">Product</h4>
        <ul class="space-y-2.5"><li><a href="#" class="text-sm text-gray-400 hover:text-white">Features</a></li><li><a href="#" class="text-sm text-gray-400 hover:text-white">Pricing</a></li></ul></div>
      <div><h4 class="font-semibold text-sm mb-4">Company</h4>
        <ul class="space-y-2.5"><li><a href="#" class="text-sm text-gray-400 hover:text-white">About</a></li><li><a href="#" class="text-sm text-gray-400 hover:text-white">Blog</a></li></ul></div>
      <div><h4 class="font-semibold text-sm mb-4">Legal</h4>
        <ul class="space-y-2.5"><li><a href="#" class="text-sm text-gray-400 hover:text-white">Privacy</a></li><li><a href="#" class="text-sm text-gray-400 hover:text-white">Terms</a></li></ul></div>
    </div>
    <div class="border-t border-white/5 pt-8 flex flex-col sm:flex-row justify-between gap-4">
      <p class="text-sm text-gray-500">&copy; 2026 Company. All rights reserved.</p>
      <div class="flex gap-4">
        <a href="#" class="text-gray-400 hover:text-white"><i data-lucide="twitter" class="w-5 h-5"></i></a>
        <a href="#" class="text-gray-400 hover:text-white"><i data-lucide="github" class="w-5 h-5"></i></a>
      </div>
    </div>
  </div>
</footer>
```
