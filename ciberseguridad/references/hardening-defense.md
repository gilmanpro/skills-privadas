# Hardening y defensa en profundidad

> Alcance: endurecimiento y defensa de proyectos PROPIOS (web/API/infra). Configuración segura, detección y mitigación. Sin catálogos ofensivos de Kali; se excepcionan `testssl.sh`/`sslyze` como verificadores de configuración TLS propia.

## Índice

1. [Security headers — guía completa](#1-security-headers--guía-completa)
2. [CORS — configuración segura y verificación](#2-cors--configuración-segura-y-verificación)
3. [Rate limiting — estrategias de protección](#3-rate-limiting--estrategias-de-protección)
4. [Honeypots — implementación](#4-honeypots--implementación)
5. [File upload seguro](#5-file-upload-seguro)
6. [Deserialización insegura (detección)](#6-deserialización-insegura-detección)
7. [Abuso de lógica de negocio](#7-abuso-de-lógica-de-negocio)
8. [Race conditions](#8-race-conditions)
9. [Parameter tampering](#9-parameter-tampering)
10. [Envenenamiento de cadena de suministro](#10-envenenamiento-de-cadena-de-suministro)
11. [Mass assignment](#11-mass-assignment)
12. [Unrestricted Resource Consumption (API4:2023)](#12-unrestricted-resource-consumption-api42023)
13. [DoS como vulnerabilidad a detectar](#13-denegación-de-servicio-dos-como-vulnerabilidad-a-detectar)
14. [Subdomain takeover](#14-subdomain-takeover)
15. [Directory browsing](#15-directory-browsing--listing)
16. [Server banner grabbing](#16-server-banner-grabbing)
17. [SSL/TLS débil](#17-ssltls-débil)
---
## 1. Security headers — guía completa

```http
# Content Security Policy — EVITA XSS y data injection
Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; font-src 'self'; connect-src 'self'; frame-ancestors 'none'; form-action 'self'; base-uri 'self'; object-src 'none'
# HTTP Strict Transport Security — EVITA downgrade a HTTP
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
# Evita MIME type sniffing
X-Content-Type-Options: nosniff
# Evita clickjacking
X-Frame-Options: DENY
# o mas moderno (en CSP): frame-ancestors 'none'
# Controla referrer info enviada
Referrer-Policy: strict-origin-when-cross-origin
# Permisos del navegador (camara, micro, geolocalizacion)
Permissions-Policy: camera=(), microphone=(), geolocation=()
# Cross-Origin isolation para SharedArrayBuffer
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Embedder-Policy: require-corp
# Cache-Control para datos sensibles
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
```

### Verificar headers con Chrome DevTools

```javascript
// Chrome DevTools MCP — evaluate_script
async () => {
  const r = await fetch(window.location.href);
  const headers = {};
  const securityHeaders = ['content-security-policy', 'strict-transport-security',
    'x-content-type-options', 'x-frame-options', 'referrer-policy',
    'permissions-policy', 'cross-origin-opener-policy', 'cross-origin-embedder-policy'];
  for (const h of securityHeaders) {
    headers[h] = r.headers.get(h) || 'MISSING';
  }
  return headers;
}
```
---
## 2. CORS — configuración segura y verificación

### Matriz de verificación

| Condición observada | Riesgo |
|---------------------|--------|
| `Access-Control-Allow-Origin: *` | Permite cualquier origen (peligroso con credenciales) |
| `Access-Control-Allow-Origin: null` | Bypass con sandboxed iframe |
| Origin reflejado dinámicamente sin validación | Cualquier origen lee respuestas autenticadas |
| `Access-Control-Allow-Credentials: true` con wildcard origin | Robo de datos con sesión de la víctima |

### Configuración segura

```http
# Solo origenes confiables (NO wildcard con credenciales)
Access-Control-Allow-Origin: https://trusted-site.com
Access-Control-Allow-Methods: GET, POST, OPTIONS
Access-Control-Allow-Headers: Content-Type, Authorization
Access-Control-Allow-Credentials: true
Access-Control-Max-Age: 86400
```

Test dinámico con Chrome DevTools (`evaluate_script`): pedir `/api/data` con cabecera `Origin: https://evil.com` y `credentials: 'include'`; VULNERABLE si `status === 200` y `access-control-allow-origin` devuelve el origin enviado (reflejo) o `*` junto con `access-control-allow-credentials: true`.

### Script incluido: `scripts/cors-test.sh`

Prueba exhaustiva de configuración CORS desde curl (7 orígenes distintos). Uso (desde la cabecera del script):

```bash
./cors-test.sh <url>    # Ej: ./cors-test.sh https://api.target.com/data
# Sin argumento usa http://localhost:3000/api/data
```

Escenarios: [1] origin legítimo (same-origin), [2] origin malicioso (`https://evil.com`), [3] `null` origin, [4] subdomain attack (`trusted-site.com.evil.com`), [5] origin con `@` (`trusted-site.com@evil.com`), [6] origin vacío, [7] preflight `OPTIONS` con `Access-Control-Request-Method: GET`.

Veredicto: si algún origin no autorizado aparece en `Access-Control-Allow-Origin` (o se refleja el enviado) → VULNERABLE.
---
## 3. Rate limiting — estrategias de protección

### Algoritmos

| Algoritmo | Descripción | Uso |
|-----------|------------|-----|
| Token Bucket | Tokens se regeneran a tasa fija. Cada request consume 1 token. Sin tokens → 429 | APIs REST |
| Fixed Window | Contador se resetea cada N segundos. Si excede límite en ventana → 429 | Simple, pero permite bursts en bordes |
| Sliding Window Log | Registra timestamp de cada request. Cuenta requests en ventana móvil | Preciso, más costoso |
| Sliding Window Counter | Combina fixed window + weighted previous window | Balance precisión/costo |
| Leaky Bucket | Cola FIFO procesa requests a tasa constante | Suavizar tráfico |

### Implementación recomendada (Token Bucket)

```javascript
// Express.js rate limiter con token bucket
const rateLimit = new Map();

function tokenBucket(req, res, next) {
  const key = req.ip;
  const now = Date.now();
  const bucket = rateLimit.get(key) || { tokens: 10, lastRefill: now };
  const elapsed = (now - bucket.lastRefill) / 1000;
  bucket.tokens = Math.min(10, bucket.tokens + elapsed * (10 / 60)); // 10 tokens/min
  bucket.lastRefill = now;
  if (bucket.tokens >= 1) {
    bucket.tokens -= 1;
    rateLimit.set(key, bucket);
    next();
  } else {
    res.status(429).json({ error: 'Too Many Requests', retryAfter: 60 });
  }
}
```

### Rate Limiting Headers (RFC)

```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 85
X-RateLimit-Reset: 1620000000
Retry-After: 60
```

### Protección anti-DDoS

Rate limiting por IP + por endpoint; CAPTCHA después de N intentos fallidos; progressive delays (exponential backoff): 1s, 2s, 4s, 8s...; account lockout temporal (no permanente — causa DoS en la cuenta); CDN/WAF: Cloudflare, AWS Shield.
---
## 4. Honeypots — implementación

**Honeypot de formulario (Anti-spam)**:

```html
<!-- Campo invisible para usuarios reales, bots lo llenan -->
<div style="position:absolute;left:-9999px" aria-hidden="true">
  <input type="text" name="website" tabindex="-1" autocomplete="off">
</div>
```

Si el campo `website` tiene valor → es bot → rechazar silenciosamente.

**Honeypot endpoint (Detección de escaneo)**: endpoints falsos que activan alerta al ser accedidos — `GET /wp-admin`, `GET /admin`, `GET /.env`, `GET /config.php`, `GET /actuator/health` (Spring Boot), `GET /.git/config`, `GET /phpinfo.php`. Cualquier acceso → loggear IP, User-Agent, y potencialmente banear.

**Honeypot de credenciales (Decoy)**:

```javascript
// Credenciales falsas en comentarios/JS que un atacante usaria
// Dev comment: admin:SuperSecret123!  ← honeytoken
```

Si alguien intenta login con estas credenciales → alerta de brecha.

**Honeypot de sesión (Canary token)**: token falso en localStorage/cookie que al ser usado fuera del contexto normal activa alerta; base de datos con registro "trampa" que al ser leído dispara webhook.
---
## 5. File upload seguro

**Riesgos**: RCE por subir `.php`, `.jsp`, `.aspx`, `.war`, `.py`, `.exe`; XSS client-side por `.html`/`.svg` con scripts; server compromise por `.htaccess`/`.config` maliciosos; overwrite de archivos del sistema (path traversal en filename); DoS por archivos enormes o ZIP bombs.

**Validaciones**:

```javascript
// Whitelist, NO blacklist
const allowedTypes = ['image/jpeg', 'image/png', 'image/webp', 'application/pdf'];
const allowedExt = ['.jpg', '.jpeg', '.png', '.webp', '.pdf'];
const maxSize = 10 * 1024 * 1024; // 10 MB

// Validar tipo real (magic bytes), no solo extension/MIME
// Guardar fuera de web root
// Renombrar archivo (UUID o hash, no usar nombre original)
// Escanear con antivirus (ClamAV)
// Servir desde dominio separado (sandbox domain)
```

Verificación: subir archivos con diferentes extensiones, content types y nombres con path traversal; todo debe ser rechazado o neutralizado (renombrado, tipo real validado).

Ref: OWASP File Upload Cheat Sheet.
---
## 6. Deserialización insegura (detección)

**Qué es**: Deserializar datos controlados por el atacante puede llevar a RCE, inyección de objetos, bypass de autenticación.

**Formatos peligrosos**: PHP serialization, Java serialization, Python pickle, Ruby Marshal, .NET BinaryFormatter, NodeJS serialize.

**Firmas a detectar en inputs, colas o tráfico** (aquí no se generan payloads: se buscan sus marcas):

| Entorno | Indicador |
|---------|-----------|
| Java | Base64 que empieza `rO0ABX...` (magic bytes de serialized object) |
| PHP | Cadenas `O:<len>:"Class":{...}` (ej. `O:4:"User":1:{s:8:"isAdmin";b:1;}`) |
| Python | Pickle cuyo contenido referencia `__reduce__` (método que ejecuta código al deserializar, p. ej. `(os.system, ("id",))`) |

**Gadget chains**: la presencia en el stack de librerías asociadas a generadores de payloads (ysoserial en Java, PHPGGC en PHP) señala riesgo: si hay deserialización reachable, hay superficie RCE. Detectar en dependency manifests.

**Mitigación**: No deserializar datos no confiables. Usar firmas digitales. Usar formatos simples (JSON) que no soportan objetos complejos.

Ref: OWASP Deserialization Cheat Sheet, PortSwigger.
---
## 7. Abuso de lógica de negocio

**Qué es**: Explotar la lógica de la aplicación de formas que el desarrollador no anticipó: precio negativo, cupones aplicados múltiples veces, saltar pasos de workflow (pagar sin checkout), stock negativo, registro con rol "admin", voting/rating ilimitado.

**Verificación propia**: mapear workflows completos, probar valores extremos, manipular pasos, race conditions.

**Mitigación**: Validar workflows server-side, validar estados de transacciones, no confiar en step order del cliente.
---
## 8. Race conditions

**Qué es**: Múltiples requests concurrentes causan estados inconsistentes en datos compartidos.

- **Limit overrun**: usar cupón múltiples veces, retirar dinero > balance
- **Multi-endpoint**: agregar items al carrito después de pago pero antes de confirmación
- **Single-endpoint**: password reset con dos usuarios simultáneos — token para la víctima enviado al atacante
- **Partial construction race**: aprovechar estado temporal durante creación de objeto

**Verificación**: enviar 20-30 requests paralelas al mismo endpoint con estado compartido (HTTP/2 single-packet: varias requests en un solo paquete TCP) y revisar inconsistencias.

**Mitigación**: transacciones atómicas en BD, locking de sesión, evitar estados inconsistentes, uniqueness constraints.

Ref: PortSwigger Research - Smashing the State Machine.
---
## 9. Parameter tampering

**Qué es**: Manipulación de parámetros para cambiar el comportamiento (precios, cantidades, descuentos, roles).

**Verificación**: modificar valores ocultos de formularios, cambiar parámetros en URL/POST body, manipular cookies.

**Mitigación**: server-side validation de todos los parámetros, no confiar en valores del cliente.
---
## 10. Envenenamiento de cadena de suministro

**Qué es**: comprometer paquetes/dependencias para infectar aplicaciones que los consumen.

**Tipos**: dependency confusion (typosquatting en npm/PyPI/Gem), malicious packages con malware, CDN compromise.

**Verificación**: revisar si package.json/requirements.txt declaran dependencias que existen en registros públicos pero no en los privados (dependency confusion).

**Mitigación**: escaneo de dependencias (npm audit, Snyk, Socket.dev), lockfiles, verificación de integridad (SRI), mirrors privados, escaneo de malicious packages.

Ref: OWASP Software Supply Chain Security.
---
## 11. Mass assignment

**Qué es**: parámetros adicionales enviados por el atacante que se asignan automáticamente al modelo, modificando propiedades no previstas.

**Verificación**: `POST /api/register {"username":"test","password":"pass","role":"admin","isAdmin":true,"credit":99999}`

**Mitigación**: DTOs explícitos, whitelist de campos permitidos (no usar bind directo del request al modelo), protección del framework (Rails `permit`, Laravel `$fillable`).

Ref: OWASP Mass Assignment Cheat Sheet.
---
## 12. Unrestricted Resource Consumption (API4:2023)

**Qué es**: APIs que no limitan consumo de recursos (número de objetos, tamaño de respuesta, frecuencia de requests).

**Verificación**: paginación ilimitada (`GET /api/users?page=1&limit=100000`), consultas costosas sin límite, objetos anidados sin depth limit.

**Mitigación**: paginación forzada, timeouts, rate limiting, limitar profundidad de objetos, web application firewall.

Ref: OWASP API Security Top 10 - API4:2023.
---
## 13. Denegación de servicio (DoS) como vulnerabilidad a detectar

Enfoque de auditoría propia: detectar la falta de límites. No ejecutar ataques.

**Application-layer DoS (App DoS)**: agota recursos del servidor (CPU, memoria, conexiones BD, almacenamiento), no de red. Superficies a revisar: búsquedas costosas sin límite, query param complexity (JSON anidado), hash collision attacks, upload de archivos enormes, creación masiva de objetos, slow reads/writes. Mitigación: rate limiting, timeouts, límites de tamaño de payload, optimización de queries, CDN/WAF.

**ReDoS (Regular Expression DoS)**: una regex mal construida causa backtracking catastrófico y congela el servidor. Patrón vulnerable: `^(a+)+$` con input `"aaaaaaaaaaaaaaaaaaaaaaaaaaaaa!"`. Detección: auditar regex con grupos anidados y cuantificadores `+`/`*`; probar con strings largos que no matchean pero exigen backtracking exhaustivo. Mitigación: revisar regex, limitar longitud de input, timeouts en regex, evitar grupos anidados con `+`/`*`.

**XML Bomb (Billion Laughs)**: entidades XML anidadas que se expanden exponencialmente (`lol3` ≈ 3GB de texto):

```xml
<?xml version="1.0"?>
<!DOCTYPE lolz [
<!ENTITY lol "lol">
<!ENTITY lol2 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;">
<!ENTITY lol3 "&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;">
]>
<root>&lol3;</root>
```

Detección: parser XML propio que acepta DTDs/external entities. Mitigación: deshabilitar DTDs, limitar expansión de entidades XML.

**Zip Bomb (Decompression Bomb)**: ZIP pequeño que se expande a gigabytes (ej. `42.zip`: 42KB → 4.5PB). Mitigación: limitar tamaño de descompresión, escanear contenido antes de descomprimir, detener descompresión si excede límite, verificar compression ratio.

**Slowloris**: mantiene múltiples conexiones HTTP abiertas enviando headers lentamente (nunca completa la request), agotando el pool de conexiones. Detección: revisar config del servidor — timeouts de cabecera/cuerpo demasiado altos o sin límite de conexiones por IP. Mitigación: timeouts de conexión cortos, límite de conexiones por IP, balanceador de carga, nginx/apache con configuración anti-Slowloris.

**Insufficient Logging and Monitoring**: sin logs/monitoreo no se detectan ataques en curso. Qué loggear: timestamp, IP origen, User-Agent, user ID, acción, recurso, resultado (éxito/fallo), datos de entrada (sin contraseñas). Eventos críticos: logins fallidos, cambios de rol/permiso, acceso a datos sensibles, errores de validación, cambios de configuración, exportaciones masivas. Qué evitar: contraseñas, tokens, tarjetas, datos biométricos. Mitigación: logging estructurado (JSON), SIEM (Splunk, ELK, Datadog), alertas en tiempo real, retención y backup de logs inmutable.
---
## 14. Subdomain takeover

**Qué es**: un registro DNS (CNAME) apunta a un servicio cloud que ya no existe; quien reclama el recurso controla el subdominio.

**Servicios vulnerables**: AWS S3, CloudFront, Azure (varios), GitHub Pages, Heroku, Netlify, Vercel, Shopify, Fastly.

**Detección**: resolver los subdominios propios y verificar si el servicio cloud responde 404/NXDOMAIN para ese recurso — si un subdominio retorna 404 en el servicio cloud → es vulnerable.

**Mitigación**: limpiar registros DNS al eliminar recursos cloud, monitorear CNAMEs huérfanos.
---
## 15. Directory browsing / listing

**Qué es**: el servidor web lista el contenido de un directorio si no hay archivo index.

**Verificación**: `curl https://target.com/uploads/` — si lista archivos → vulnerabilidad.

**Mitigación**: deshabilitar directory listing (Apache: `Options -Indexes`, Nginx: `autoindex off;`).
---
## 16. Server banner grabbing

**Qué es**: exposición de versiones de software en headers de respuesta (`Server: Apache/2.4.49`, `X-Powered-By: Express`).

**Verificación**: `curl -I https://target.com | grep -iE "server|x-powered-by"`

**Mitigación**: ocultar/deshabilitar banners, usar server headers genéricos, deshabilitar `X-Powered-By`.
---
## 17. SSL/TLS débil

**Verificación de la configuración propia** (solo verificadores de configuración TLS, no explotación):

```bash
testssl.sh target.com      # herramienta completa de testing TLS
sslyze --regular target.com
```

Comprobar que rechazan protocolos obsoletos (SSLv2, SSLv3, TLSv1.0, TLSv1.1) y cipher suites débiles (RC4, 3DES, EXPORT, NULL).

**Ataques históricos** (referencia de qué configura mal un servidor): Heartbleed (CVE-2014-0160), POODLE (CVE-2014-3566), ROBOT (CVE-2017-17382), Logjam, FREAK.

**Mitigación**: TLS 1.2+ mínimo, cipher suites fuertes, HSTS, certificados de CA confiable, Let's Encrypt.
