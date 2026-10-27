# Boilerplate HTML

Plantilla autocontenida para proyectos frontend-design.

```html
<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Page Title</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            display: ['Clash Display', 'system-ui', 'sans-serif'],
            body: ['Satoshi', 'system-ui', 'sans-serif'],
          },
          colors: {
            brand: { 50:'#eef2ff',100:'#e0e7ff',200:'#c7d2fe',300:'#a5b4fc',400:'#818cf8',500:'#6366f1',600:'#4f46e5',700:'#4338ca',800:'#3730a3',900:'#312e81',950:'#1e1b4b' }
          },
          animation: {
            'fade-in': 'fadeIn 0.6s ease-out',
            'slide-up': 'slideUp 0.6s ease-out',
          },
          keyframes: {
            fadeIn: { '0%':{opacity:'0'}, '100%':{opacity:'1'} },
            slideUp: { '0%':{opacity:'0',transform:'translateY(20px)'}, '100%':{opacity:'1',transform:'translateY(0)'} },
          }
        }
      }
    }
  </script>
  <link href="https://fonts.googleapis.com/css2?family=Satoshi:wght@400;500;700;900&display=swap" rel="stylesheet">
</head>
<body class="bg-gray-950 text-gray-100 antialiased font-body">

  <!-- CONTENT -->

  <script src="https://unpkg.com/lucide@latest"></script>
  <script>lucide.createIcons();</script>
  <!-- Alpine.js: opcional, incluirla solo si se requiere interactividad -->
  <!-- <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3/dist/cdn.min.js"></script> -->
</body>
</html>
```
