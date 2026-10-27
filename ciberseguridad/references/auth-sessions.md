# Autenticación, sesiones y control de acceso: testing y hardening

> IDOR / BOLA / BOPLA y escalada de privilegios NO se duplican aquí: ver `references/endpoint-authz.md`.

## Índice

1. [Timing Attack (character-by-character)](#1-timing-attack--bypass-por-tiempo-de-respuesta-character-by-character-enumeration)
2. [Script timing-attack.bat](#2-script-scripts-timing-attackbat)
3. [OTP / 2FA](#3-otp--2fa-brute-force-y-logical-bypass)
4. [Sesiones](#4-sesiones)
5. [JWT](#5-jwt-insecure-validation)
6. [OAuth 2.0 / OpenID Connect](#6-oauth-20--openid-connect)
7. [Cookies de sesión](#7-cookies-de-sesión)
8. [Almacenamiento de tokens](#8-almacenamiento-de-tokens)
9. [Password policy](#9-password-policy)

---

## 1. Timing Attack — Bypass por Tiempo de Respuesta (Character-by-Character Enumeration)

**Qué es**: El atacante mide tiempos de respuesta para deducir caracteres válidos uno por uno. Ocurre cuando la validación usa comparación por caracter (`strcmp`, `===` por posición) en vez de comparación en tiempo constante. Funciona contra passwords de strings cortas, OTP numéricos, PINs y tokens de recuperación.

**Cómo funciona**: un string comparado caracter por caracter retorna *inmediatamente* al encontrar una diferencia. Si `password[0]` coincide con `input[0]`, el sistema compara `password[1]` antes de fallar. Ese microsegundo extra es medible.

**Verificación — Password (Python)**:
```python
import requests, time, string

target = "https://target.com/api/login"
base_time = float('inf')
password = ""
charset = string.ascii_lowercase + string.digits

for pos in range(8):  # asumiendo 8 chars
    for c in charset:
        payload = {"username": "admin", "password": password + c + "x" * (7 - pos)}
        start = time.time()
        r = requests.post(target, json=payload)
        elapsed = time.time() - start

        if elapsed > base_time + 0.01:  # threshold de timing
            password += c
            base_time = elapsed
            break
```

**Verificación — OTP (Python)**:
```python
# OTP de 6 dígitos — probar posición por posición
# Si posición 0 correcta tarda 1ms más, la detectamos
otp = ""
for pos in range(6):
    for digit in range(10):
        payload = {"code": otp + str(digit) + "0" * (5 - pos)}
        # medir tiempo de respuesta
        # si el tiempo es mayor que baseline → dígito correcto
```

**Verificación manual con curl**:
```bash
# Medir timing exacto de cada intento
curl -w "Connect: %{time_connect}s, TTFB: %{time_starttransfer}s, Total: %{time_total}s\n" \
  -d "username=admin&password=A" -s -o nul https://target.com/login
curl -w "Connect: %{time_connect}s, TTFB: %{time_starttransfer}s, Total: %{time_total}s\n" \
  -d "username=admin&password=B" -s -o nul https://target.com/login
# Comparar tiempos totales — el carácter correcto será ligeramente más lento
```

**Variantes de Timing Attack**:
- **OTP numérico**: probar dígito por dígito en códigos de 2FA. Si la posición 0 es correcta → respuesta ~1-3ms más lenta.
- **Password reset token**: tokens UUID/secuenciales en URLs de recuperación; probar caracter por caracter.
- **Login username enumeration**: el tiempo varía si el usuario existe vs no (el sistema hashea password solo si el user existe).
- **API key validation**: validación carácter por carácter expuesta en endpoints de API.
- **Session ID / CSRF token**: si el token se compara carácter a carácter.

**Mitigación**:
- **Comparación en tiempo constante**: `hash_equals()` (PHP), `compare_digest()` (Python hmac), `crypto.timingSafeEqual()` (Node.js), `MessageDigest.isEqual()` (Java).
- Para OTP: `hash_equals(hmac(otp_attempt), hmac(stored_otp))`.
- **Jitter/retardo aleatorio**: ~10-50ms de ruido aleatorio en todas las respuestas de autenticación.
- **Respuesta genérica siempre**: mismo tiempo de respuesta sin importar si el user existe o la pass es correcta.
- **Rate limiting agresivo**: máximo 3-5 intentos por segundo por IP.
- **OTP con rate limiting**: máximo 3 intentos de OTP erróneos antes de bloquear 30s.
- **bcrypt/argon2**: el hash es intencionalmente lento (~100-250ms), lo que reduce la ventana de timing.

Refs: OWASP Timing Attacks, PortSwigger Authentication, CWE-208.

---

## 2. Script `scripts/timing-attack.bat`

Detecta timing attacks en login/OTP usando `curl -w "%{time_total}"`. Uso:

```bat
timing-attack.bat <url> [userenum|otp|password]
:: Ej: timing-attack.bat https://target.com/login userenum
```

| Modo | Qué envía | Interpretación |
|------|-----------|----------------|
| `userenum` | `username=` admin, root, test, user, nonexistent (con `password=test`) | Diferencias >50ms entre usuarios existentes y no existentes → user enumeration posible |
| `otp` | `code=X00000` para X en 0-9 | Un dígito consistentemente más lento (~1-5ms) → dígito inicial correcto; repetir 3 veces para confirmar |
| `password` | `password=a,aa,aaa...` (longitudes 1-12, username=admin) | El tiempo aumenta con la longitud → comparación char-by-char, enumeración viable |

Notas:
- Crea la carpeta `security\evidence` si no existe; los tiempos se muestran por consola (redirigir a `security\evidence\timing-results.txt` para guardarlos).
- Verificación defensiva en proyecto propio: si el script muestra diferenciación, aplicar las mitigaciones de la sección 1.

---

## 3. OTP / 2FA: Brute Force y Logical Bypass

**Qué es**: El código OTP de 6 dígitos (10^6 = 1,000,000 combinaciones) es vulnerable a fuerza bruta sin rate limiting. La validación secuencial posición-por-posición permite reducir el espacio de 1,000,000 a solo 6×10 = 60 intentos mediante timing attack.

**Verificación**:
```python
# Brute force directo (sin timing) — solo si no hay rate limiting
for code in range(1000000):
    r = requests.post(url, json={"code": f"{code:06d}"})
    if r.status_code == 200: break

# Timing attack OTP (reducido a 60 intentos)
otp = ""
for pos in range(6):
    for d in range(10):
        # enviar OTP parcial + dígito de prueba
        test = otp + str(d) + "".zfill(5 - pos)
        start = time.time()
        r = requests.post(url, json={"code": test})
        elapsed = time.time() - start
        if elapsed > threshold:  # dígito correcto detectado por timing
            otp += str(d)
            break
```

**Bypass de 2FA comunes (checklist de testing)**:
- Rate limiting ausente: probar los 1,000,000 códigos en paralelo.
- OTP reutilizable: el código no se invalida tras usarse o expirar.
- OTP estático por sesión: el mismo código es válido para toda la sesión.
- Validación server-side débil: solo valida longitud (6 dígitos) pero acepta requests sin OTP.
- Enumeración de OTP: generado con timestamp o seed predecible.
- Forced browsing después del login (pasar directo a `/dashboard` saltando el paso 2FA).
- Reutilización de código TOTP; sesión no invalidada tras 2FA fallido.
- Backup codes no protegidos; "Remember this device" sin seguridad.

**Mitigación**:
- Rate limiting estricto (máx 3-5 intentos de OTP, luego bloqueo de 30-60s).
- Invalidar OTP tras primer uso o tras 60s.
- Comparación en tiempo constante (`hash_equals`).
- TOTP (Time-based OTP) con ventana de ±1 step.
- Bloqueo de cuenta tras 10 OTP fallidos.
- Logging y alerta de actividad sospechosa.
- Verificar 2FA en cada request sensible; no permitir forced browsing.

---

## 4. Sesiones

**Session Fixation**
- Qué es: el atacante fuerza a la víctima a usar un ID de sesión conocido y el ID no se regenera tras el login.
- Verificación: comprobar si el session ID cambia después del login.
- Mitigación: regenerar session ID al hacer login (`session_regenerate_id` en PHP o equivalente del framework).

**Session Hijacking**
- Qué es: robo del token de sesión para impersonar al usuario.
- Vectores: XSS (robo de cookies), sniffing de red (HTTP sin HTTPS), malware, phishing.
- Mitigación: cookies HttpOnly + Secure + SameSite, HTTPS obligatorio, regenerar sesión al login, timeout de sesión.

**Invalidación de Sesión Deficiente**
- Qué es: el logout no invalida realmente la sesión; el token sigue siendo válido.
- Verificación: hacer logout y reusar el mismo token/cookie → si funciona, la sesión no fue invalidada.
- Mitigación: invalidar la sesión en servidor al logout (no solo borrar la cookie del cliente).

**Predicibilidad de IDs de Sesión**
- Qué es: session IDs con baja entropía (timestamp, secuenciales, hash débil).
- Verificación: capturar múltiples session IDs y analizar patrones.
- Mitigación: generadores criptográficamente seguros (CSPRNG), longitud ≥ 128 bits.

**Enumeración de Usuarios**
- Qué es: determinar si un email/username existe en el sistema.
- Indicadores: mensajes de error distintos ("Usuario no encontrado" vs "Contraseña incorrecta"), tiempos de respuesta diferentes, códigos HTTP diferentes.
- Verificación: probar login y "forgot password" con emails existentes vs no existentes.
- Mitigación: mensajes de error genéricos idénticos ("Credenciales inválidas"), tiempos de respuesta constantes.

---

## 5. JWT Insecure Validation

**Qué es**: Vulnerabilidades en la validación de JSON Web Tokens (verificación conceptual, sin herramientas de crackeo).

**Puntos a verificar**:
- Claims ausentes: `exp` (sin expiración), `aud` (audiencia), `iss` (issuer) → token demasiado permisible.
- Secreto débil: confirmar que la clave HMAC no es una palabra obvia (`secret`, `password`, `changeme`).
- `alg: none`: cambiar el algoritmo a "none" → el token queda sin firma.
- Confusión `HS256` vs `RS256`: usar la clave pública como secreto HMAC cuando el servidor espera RS256.

```python
# Prueba conceptual alg:none
header = {"alg":"none","typ":"JWT"}
payload = {"sub":"1","admin":true}
token = base64url(header) + "." + base64url(payload) + "."
```

**Mitigación**: Forzar algoritmo RS256/ES256, validar `exp`, `aud`, `iss`, usar secretos fuertes, no confiar en el `alg` del header.

---

## 6. OAuth 2.0 / OpenID Connect

**Ataques comunes**:
- **CSRF en OAuth**: parámetro `state` ausente o débil.
- **Redirect URI manipulation**: redirect URI abierto permite robo del code.
- **Code injection**: robo de authorization code.
- **Token leakage**: token en referer header, logs o URL fragment.
- **Scope abuse**: la aplicación solicita más permisos de los necesarios.

**Verificación**: manipular `redirect_uri`, probar CSRF en el flujo OAuth, verificar scopes solicitados.

**Mitigación**: `state` parameter anti-CSRF, validar `redirect_uri` contra whitelist, PKCE obligatorio, scopes mínimos.

---

## 7. Cookies de Sesión

**Flags requeridas**:
```
Set-Cookie: session=abc123; Secure; HttpOnly; SameSite=Strict; Path=/; Max-Age=3600; Domain=example.com
```

| Flag / atributo | Función |
|-----------------|---------|
| `Secure` | Solo se envía por HTTPS |
| `HttpOnly` | No accesible vía `document.cookie` (evita robo por XSS) |
| `SameSite` | `Strict` (mejor) o `Lax` (balance) — evita CSRF |
| `Path` | Limita la cookie a una ruta específica |
| `Domain` | Si no se especifica, solo el origen exacto |
| `Max-Age` / `Expires` | Tiempo de vida limitado |
| Prefijo `__Host-` | Requiere Secure + Path=/ + sin Domain |
| Prefijo `__Secure-` | Requiere Secure |

**Verificación en navegador** (DevTools — cookies visibles desde JS = sin HttpOnly):
```js
() => {
  const cookies = document.cookie.split(';').map(c => c.trim().split('='));
  const problems = [];
  cookies.forEach(([name, value]) => {
    problems.push({ cookie: name, accessibleViaJS: true, concern: 'Not HttpOnly — vulnerable to XSS' });
  });
  return {
    accessibleCookies: cookies.map(c => c[0]),
    concerns: problems.length > 0 ? problems : 'No cookies accessible via JS (HttpOnly is set)'
  };
}
```

---

## 8. Almacenamiento de Tokens

| Lugar | Seguridad | Nota |
|-------|-----------|------|
| `localStorage` | Baja | Vulnerable a XSS |
| `sessionStorage` | Baja | Vulnerable a XSS, se limpia al cerrar tab |
| Cookie HttpOnly + Secure + SameSite | Alta | Recomendado |
| `httpOnly` cookie + CSRF token | Alta | Mejor práctica |
| In-memory (variable JS) | Media | Se pierde al refrescar |

**Verificación en navegador** (auditar tokens en storage):
```js
() => {
  const storage = {};
  for (let i = 0; i < localStorage.length; i++) {
    const key = localStorage.key(i);
    storage.localStorage = storage.localStorage || {};
    storage.localStorage[key] = localStorage.getItem(key).substring(0, 50) + '...';
  }
  for (let i = 0; i < sessionStorage.length; i++) {
    const key = sessionStorage.key(i);
    storage.sessionStorage = storage.sessionStorage || {};
    storage.sessionStorage[key] = sessionStorage.getItem(key).substring(0, 50) + '...';
  }
  return { ...storage, warning: 'Tokens in localStorage/sessionStorage are vulnerable to XSS' };
}
```

---

## 9. Password Policy

- Mínimo 8-12 caracteres (NIST recomienda 8, sin máximo artificial).
- No forzar cambios periódicos (NIST ya no lo recomienda).
- Verificar contra listas de passwords comunes (HaveIBeenPwned API).
- bcrypt/argon2 para hashing (NO SHA, NO MD5).
- Salt único por password (bcrypt lo incluye automáticamente).
