---
name: ciberseguridad
description: "Auditoria de seguridad y hardening para proyectos software PROPIOS (web, API, cloud, IA/LLM): busqueda de vulnerabilidades con curl/navegador, OWASP Top 10 y OWASP LLM Top 10, catalogo de verificacion y mitigacion (CSRF, XSS, SSRF, inyecciones, clickjacking, prototype pollution, request smuggling, cache poisoning), autenticacion y sesiones (timing attacks, OTP/2FA, OAuth/OIDC, JWT, cookies), validacion de endpoints, rate limiting, honeypots, headers de seguridad, secretos en git, SAST/SCA, checklists por tipo de proyecto y CVSS. Genera informes con severidad, evidencia y recomendaciones. Usar SIEMPRE que el usuario pida proteger, asegurar, auditar o testear la seguridad de su propio codigo, servidor o app, o mencione vulnerabilidades, ataques, OWASP, hardening, rate limiting o endpoints inseguros, aunque no diga seguridad explicitamente. NO usar para campanas de pentesting ofensivo con herramientas de Kali contra objetivos de terceros (la skill kali-linux fue archivada el 2026-10-13: sin sucesora activa)."
---

# Ciberseguridad

Auditorías de seguridad ofensiva y defensiva con impacto real y generación de informes.

## Cuándo usar

- Pentesting web/API con curl o navegador
- Auditoría de versiones, CVEs, rutas sensibles, credenciales
- Hardening de Linux, headers de seguridad, IDS
- Code security review y análisis de dependencias
- Informes de seguridad con mapeo OWASP/MITRE/CWE

## Alcance
- Petición específica → ejecuta solo lo pedido. Genérica → checklist del modo relevante. Informativa → responde sin ejecutar.
- Solo targets con autorización por escrito; nunca expongas secretos.
- Esta skill audita/protege proyectos propios con curl, navegador y scripts incluidos. Campañas ofensivas completas con toolchain de Kali (nmap/sqlmap/metasploit/hashcat, AD, C2) → la antigua skill `kali-linux`, ARCHIVADA el 2026-10-13 en `~/.agents/skills-archive/kali-linux` (sin sucesora activa en el roster de skills).

## Estándar de rigor (obligatorio en cada auditoría)
1. **Contexto y autorización:** analiza target, alcance y permisos antes del primer comando; qué se podría romper al probar.
2. **Hipótesis:** formula hipótesis explícitas por hallazgo; traza el flujo input → procesamiento → salida (lenguaje/framework/query/templating). Prueba la hipótesis, no payloads sueltos.
3. **Baseline primero:** mide el comportamiento normal (código, tamaño, timing) antes de inyectar; las diferencias solo son señal si superan claramente ese baseline.
4. **Doble evidencia:** todo hallazgo = comando exacto + respuesta cruda + al menos 2 técnicas de confirmación cruzada (booleana + time-based; curl + navegador).
5. **Contra falsos positivos:** repite cada prueba 3×; si es errática o inexplicable, marca "no confirmado". Separa hallazgo teórico (versión vulnerable) de confirmado (explotable) al asignar severidad.
6. **Iteración:** probar → analizar → validar → documentar; re-test tras cada remediación; revisión final del reporte.
7. **Tema sensible:** payloads no destructivos (RCE solo lectura o canary OOB), sin DoS, respeta rate limits; detente y pregunta ante algo irreversible. Documenta cada paso para que un tercero lo reproduzca.
8. **Evidencia segura:** guarda respuestas en `security/evidence/` y redacta secretos/datos personales antes de pegarlos en el reporte.

## Modos de operación

| Modo | Reference |
|---|---|
| Auditoría web activa con curl (playbook + 4 scripts) | `references/web-audit-curl.md` |
| Catálogo de opciones de curl para pentesting (autocontenido) | `references/curl-pentest.md` |
| Pentesting de frontend con navegador (autocontenido, playwright-cli) | `references/playwright-pentest.md` |
| Auditoría y hardening de Linux (audit + IDS + triaje) | `references/linux-audit-ids.md` |
| Endpoints/AuthZ | `references/endpoint-authz.md` |
| Git y secretos | `references/git-secrets-audit.md` |
| Cloud (AWS/Azure/GCP/K8s) | `references/cloud-security.md` |
| Catálogo de vulnerabilidades web: verificación y mitigación (CSRF, XSS, SSRF, inyecciones, ataques de cliente) | `references/vuln-web-catalog.md` |
| Autenticación y sesiones (timing attacks, OTP/2FA, OAuth/OIDC, JWT, cookies, almacenamiento de tokens) | `references/auth-sessions.md` |
| Hardening en profundidad (headers, CORS, rate limiting, honeypots, uploads, DoS, subdomain takeover) | `references/hardening-defense.md` |
| Checklists por tipo de proyecto + CVSS v3.1 + SAST/SCA/IaC | `references/checklists-proyecto.md` |
| Malware / Forense / SaaS / IA-LLM / Context7 | `references/malware-analysis.md`, `references/forensics-ir.md`, `references/saas-security.md`, `references/ai-security.md`, `references/context7.md` |
| Red, AD, móvil, wireless, IoT/OT, red teaming, OSINT | `references/pentesting-modes.md` |

## OWASP Top 10 rápido
A01 Control de acceso · A02 Criptografía · A03 Inyección · A04 Diseño · A05 Configuración · A06 Componentes · A07 Autenticación · A08 Integridad · A09 Registro/Monitoreo · A10 SSRF → detalle en `references/owasp-top10.md`.

Tests rápidos: sin token en endpoints (A01) · `' OR '1'='1` (A03) · headers faltantes / `.env` (A05) · `npm audit`/`trivy` (A06) · JWT alg:none (A07) · `169.254.169.254` (A10).

## Auditoría web con curl
```bash
./scripts/fingerprint-scan.sh <url>              # versiones (o .bat en Windows)
./scripts/cve-lookup.sh "<producto>" <version>   # CVEs vía NVD
./scripts/route-scan.sh <url>                    # rutas sensibles (lista en scripts/paths/)
./scripts/rate-limit-test.sh <url> [n]            # rate limit
```
Cobertura del playbook: versiones §1 · CVEs §2 · explotación §3 · rutas §4 · claves §5 · rate-limit §6 · credenciales §7 · bypass §8 · inyecciones §9 · reporte §10.

## Hardening y defensa
Headers de seguridad (CSP/HSTS/X-Frame-Options…), CORS, rate limiting (algoritmos + token bucket), honeypots, file upload seguro, deserialización, DoS (ReDoS/XML/zip bomb/Slowloris), subdomain takeover y SSL/TLS: valores y código completos en `references/hardening-defense.md` (script `scripts/cors-test.sh`). Gestión de secretos en `references/git-secrets-audit.md`. Mínimo privilegio, MFA, parches/SBOM. Hosts Linux: SSH/firewall/PAM, IDS (Snort/OSSEC/Wazuh/AIDE), triaje con `scripts/linux-audit.sh` y `scripts/linux-intrusion-triage.sh` (requieren Linux + sudo).

## Code security review
Traza flujos de datos (input → procesamiento → salida). SAST por lenguaje (`bandit`, `gosec`, `eslint-plugin-security`, `semgrep`). Valida input validation, authZ en cada handler, secretos, dependencias y sanitización.

## Context7
Antes de recomendar hardening o payloads, verifica configs seguras con la CLI `ctx7` (ver `references/context7.md`).

## Salida
1. Hallazgos con severidad (Critical/High/Medium/Low/Info) y evidencia reproducible. Rangos CVSS v3.1 y checklists por tipo de proyecto (Frontend/API/BD/DevOps) en `references/checklists-proyecto.md`.
2. `security/report.md` con reproducción, recomendación y mapeo OWASP/MITRE/CWE.
3. Secretos redactados (`sk_live_••••abcd`); respuestas crudas en `security/evidence/`.