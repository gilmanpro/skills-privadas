# Checklists por tipo de proyecto y severidad

> Alcance: auditoría/defensa de proyectos PROPIOS. Checklists de verificación interna y catálogo de escáneres estáticos (SAST/SCA/IaC). Sin herramientas ofensivas de Kali.

## Índice

1. [Severidad (CVSS v3.1)](#1-severidad-cvss-v31)
2. [Checklist rápido por tipo de proyecto](#2-checklist-rápido-por-tipo-de-proyecto)
3. [Tipos de input a probar en endpoints](#3-tipos-de-input-a-probar-en-endpoints)
4. [Catálogo SAST / SCA / IaC](#4-catálogo-sast--sca--iac)

---

## 1. Severidad (CVSS v3.1)

| Nivel | Rango CVSS | Descripcion | Ejemplos |
|-------|-----------|------------|----------|
| Critical | 9.0-10.0 | Acceso total al sistema, RCE, data breach masivo | SQLi con dump de DB, RCE sin auth |
| High | 7.0-8.9 | Acceso a datos sensibles, bypass de auth | IDOR en datos de usuarios, JWT sin firma |
| Medium | 4.0-6.9 | Informacion sensible expuesta, DoS local | Informacion en headers, rate limit ausente |
| Low | 0.1-3.9 | Mejores practicas, hardening | Missing security headers, verbose errors |
| Info | N/A | Observaciones, recomendaciones | Tecnologia obsoleta, cookies sin SameSite |

---

## 2. Checklist rápido por tipo de proyecto

### Frontend / SPA

```
[ ] No hay tokens en localStorage (usar httpOnly cookies)
[ ] CSP configurado correctamente
[ ] No hay datos sensibles en console.log
[ ] No hay secretos hardcodeados en JS
[ ] SRI en CDN externos
[ ] innerHTML no se usa con datos no confiables
[ ] eval() no se usa (o esta justificado)
[ ] CORS validado
[ ] Cookies con Secure + HttpOnly + SameSite
```

### API Backend

```
[ ] Rate limiting en todos los endpoints
[ ] Autenticacion en todos los endpoints (excepto login/register)
[ ] Input validation (server-side, nunca confiar en client-side)
[ ] Parameterized queries (nunca concatenar SQL)
[ ] Output encoding (para prevenir XSS en respuestas HTML)
[ ] CORS configurado con origenes especificos
[ ] Headers de seguridad en todas las respuestas
[ ] File upload con validacion estricta
[ ] Errores sin informacion sensible
[ ] Logs sin datos sensibles
[ ] HTTPS obligatorio (redirigir HTTP → HTTPS)
```

### Base de Datos

```
[ ] Principio de minimo privilegio (app user no es admin)
[ ] Conexiones encriptadas (TLS)
[ ] Backups encriptados
[ ] No exponer puerto de BD a internet
[ ] Prepared statements / parameterized queries
[ ] Datos sensibles encriptados en reposo (PII, passwords, tokens)
```

### DevOps / Infraestructura

```
[ ] Secretos en vault/secrets manager, NO en codigo/env
[ ] Imagenes Docker escaneadas (trivy, snyk)
[ ] IaC escaneado (tfsec, checkov)
[ ] CI/CD pipelines con security scans
[ ] Principio de minimo privilegio en IAM roles
[ ] Network policies / security groups restrictivos
[ ] Logs centralizados con alertas
[ ] Dependencias actualizadas regularmente
```

---

## 3. Tipos de input a probar en endpoints

Al validar la entrada de cada endpoint propio, cubrir:

- Tipos incorrectos (string en vez de number)
- Valores extremos (numeros grandes, negativos, cero)
- Caracteres especiales, Unicode, emojis
- Null, undefined, campos faltantes
- Arrays donde se espera string
- SQLi, XSS, NoSQLi payloads en cada campo
- Mass assignment: enviar campos extra como `role: "admin"`, `isAdmin: true`

---

## 4. Catálogo SAST / SCA / IaC

### SAST (Static Analysis)

```bash
# JavaScript/TypeScript
eslint-plugin-security
npm audit

# Multi-lenguaje (reglas propias y comunitarias)
semgrep --config auto .

# Python
bandit -r .
safety check

# Go
gosec ./...

# Java
spotbugs
findsecbugs

# Terraform/Infrastructure as Code
tfsec .
checkov -d .
terrascan scan

# Docker
trivy image <image>
dockle <image>
hadolint Dockerfile
```

### SCA (Dependency Scanning)

```bash
npm audit --json
pip-audit
bundle audit
cargo audit
trivy fs --scanners vuln .
snyk test
osv-scanner .
retire.js    # JS library scanner
```

Notas de uso en CI: `trivy fs --severity HIGH,CRITICAL .` para filtrar hallazgos relevantes, y `pip-audit --format json` / `snyk test --json` para consumo por scripts.

---

## 5. Referencias cruzadas

- Verificacion de headers y CORS: [hardening-defense.md](hardening-defense.md)
- Secretos en repositorios: [git-secrets-audit.md](git-secrets-audit.md)
- Scripts listos en `scripts/`: `security-scan.bat` (headers, metodos HTTP, CORS, archivos sensibles, timing), `timing-attack.bat` (user enum, OTP digit, password char), `cors-test.sh` (7 origenes).
