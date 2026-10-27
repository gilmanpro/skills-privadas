# Auditoría de Git y Secretos Hardcodeados

Objetivo: detectar secretos (API keys, tokens, contraseñas, certificados, URLs con credenciales) en el **código actual** y en el **historial de commits**. Regla fundamental: **borrar un archivo no borra el secreto de git** — todo lo que se haya commiteado una vez queda en el historial (y en clones, forks y backups).

Alcance: backend, frontend (bundles, config) y metadatos (remotes, authors, tags, CI).

## Fase 0 — Preparación

- Auditar el repo correcto: si es un clon, verificar que tiene historial completo (`git log --all | wc -l` vs. repo remoto).
- Herramientas: `gitleaks` (preferida), `trufflehog`, `detect-secrets`, `git-secrets`, y para remediación `git-filter-repo` o BFG.
- Instalación rápida: `choco install gitleaks` (Windows), `brew install gitleaks` (macOS), `go install github.com/gitleaks/gitleaks/v8@latest`.

## Fase 1 — Estado actual (working tree + index)

```bash
# Escaneo automatizado (gitleaks)
npx gitleaks detect --source . --report-path security/evidence/gitleaks.json --report-format json

# Escaneo del estado actual (detect-secrets; emite baseline JSON al stdout)
detect-secrets scan

# Archivos sensibles bajo control de versiones (¡incluso si ahora están en .gitignore!)
git ls-files | grep -iE "\.env|secret|credential|\.pem|\.p12|\.pfx|\.key$"

# ¿.gitignore cubre los archivos de entorno?
grep -nE "\.env|secret|\.key" .gitignore

# Búsqueda directa en el código (rápida, muchos falsos positivos → triar)
grep -rInE "api[_ -]?key|secret|password|passwd|BEGIN (RSA|EC|OPENSSH|PGP) PRIVATE" \
  --include="*.py" --include="*.js" --include="*.ts" --include="*.java" --include="*.go" \
  --include="*.rb" --include="*.php" --include="*.cs" --include="*.yaml" --include="*.yml" \
  --include="*.json" --include="*.toml" . | grep -viE "test|example|mock|sample|node_modules"
```

## Fase 2 — Historial de commits (todas las ramas)

```bash
# Visión general
git log --all --oneline --decorate
git branch -a && git tag

# Diffs de todo el historial filtrando por patrones de secretos (lento en repos grandes)
git log --all -p -G "api[_ -]?key|secret|password|token|BEGIN (RSA|EC|OPENSSH|PGP) PRIVATE" \
  | grep -iE "^commit |^    |api[_ -]?key|secret|password|token|BEGIN" | head -100

# Archivos sensibles BORRADOS del historial (siguen recuperables)
git log --all --diff-filter=D --name-only --pretty=format:"%h %s" -- "*.env*" "*secret*" "*credential*"

# Blobs huérfanos (commits reescritos/borrados que quedaron sin referencia)
git rev-list --objects --all | grep -iE "\.env|secret|\.key$"
git fsck --lost-found 2>/dev/null | grep commit   # commits sin referencia

# gitleaks sobre TODO el historial
npx gitleaks detect --source . --log-opts="--all" --report-path security/evidence/gitleaks-history.json

# git-secrets sobre TODO el historial (patrones genericos + AWS)
git secrets --scan-history

# Metadatos: remotes, autores, CI
git remote -v                                    # ¿apunta a un repo público equivocado?
git log --all --format="%an <%ae>" | sort | uniq -c | sort -rn   # emails sospechosos
git log --all -i --grep="password|token|secret|key" --oneline    # mensajes de commit reveladores
```

## Fase 3 — Frontend

```bash
# Keys embebidas en bundles de producción
grep -rInE "AIza[0-9A-Za-z_-]{35}|sk_live_[0-9a-zA-Z]{24}|sk_test_[0-9a-zA-Z]{24}|AKIA[0-9A-Z]{16}|ghp_[0-9A-Za-z]{36}|xox[baprs]-" \
  --include="*.js" dist/ build/ 2>/dev/null

# Source maps: exponen el código fuente original (buscar también keys dentro)
git ls-files | grep -E "\.js\.map$"

# .env del frontend commiteado (las keys "públicas" de Firebase/Stripe son públicas por diseño,
# pero su mal uso SÍ es hallazgo: reglas Firestore abiertas, webhooks sin verificación de firma)
git ls-files | grep -E "\.env"
```

Claves típicas de frontend y su riesgo real:

| Key | Ejemplo de patrón | Riesgo real |
|-----|-------------------|-------------|
| Firebase API key | `AIza...` | Pública por diseño → riesgo si las reglas de Firestore/Storage están abiertas |
| Stripe publishable | `pk_live_...` | Pública por diseño → riesgo en webhooks sin `Stripe-Signature` verificada |
| Stripe secret | `sk_live_...` | **CRITICAL** — nunca debe estar en frontend |
| Google Maps | `AIza...` | Abuso de cuota, costes |
| AWS Cognito | UserPoolId/ClientId | Público por diseño → riesgo por reglas/roles mal configurados |
| GitHub PAT | `ghp_...` | **CRITICAL** |
| Slack webhook | `https://hooks.slack.com/services/...` | **High** — envío de mensajes como el bot |
| Sentry DSN | `https://...@o...ingest.sentry.io/...` | Low/Medium — fuga de eventos a terceros |

## Fase 4 — Patrones de búsqueda (regex)

| Tipo | Patrón |
|------|--------|
| AWS Access Key ID | `AKIA[0-9A-Z]{16}` |
| AWS Secret Access Key | `(?i)aws(.{0,20})?(secret|access).{0,20}['"][0-9a-zA-Z/+]{40}['"]` |
| Google API key | `AIza[0-9A-Za-z\-_]{35}` |
| Stripe live secret | `sk_live_[0-9a-zA-Z]{24}` |
| Stripe publishable | `pk_(live|test)_[0-9a-zA-Z]{24}` |
| GitHub PAT | `ghp_[0-9A-Za-z]{36}` |
| Slack token | `xox[baprs]-[0-9A-Za-z-]{10,}` |
| JWT | `eyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}` |
| Clave privada | `-----BEGIN (RSA|EC|OPENSSH|PGP|ENCRYPTED) PRIVATE KEY-----` |
| URL con credenciales | `https?://[^:/\s]+:[^@/\s]+@[^/\s]+` |
| Connection string | `(mysql|postgres|mongodb)(\+srv)?://[^:/\s]+:[^@/\s]+@` |
| Slack webhook | `https://hooks\.slack\.com/services/T[0-9A-Z]+/B[0-9A-Z]+/[0-9A-Za-z]+` |
| Azure Storage | `AccountKey=[A-Za-z0-9+/=]{40,}` |
| Heroku API key | `heroku[a-z0-9_-]{20,}` |

## Fase 5 — Remediación

**Orden correcto (crítico):**
1. **ROTAR las credenciales expuestas primero** — asumir que están comprometidas (pueden estar en logs de CI, forks, backups, scraping de GitHub).
2. Limpiar el historial:
   ```bash
   # Preferido (rápido, elimina blobs huérfanos)
   git filter-repo --invert-paths --path .env --path path/to/secret.py
   # Alternativa clásica
   git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch .env' --prune-empty --tag-name-filter cat -- --all
   # O BFG:  bfg --delete-files .env
   git gc --prune=now --aggressive
   ```
3. Force push de **todas** las ramas y tags: `git push --force --all && git push --force --tags` (coordinado con el equipo: invalida clonaciones).
4. Si el repo es público: asumir comprometido, revisar `gh secret list`, GitHub secret scanning, y considerar la reescritura del historial no es suficiente → rotar y evaluar privacidad.
5. Prevención para el futuro:
   - Pre-commit hook con gitleaks: `npx gitleaks protect --staged`
   - Secret scanning en CI (GitHub Actions: `zricethezav/gitleaks-action` o trufflehog)
   - `.gitignore` con `.env*`, `*.pem`, `*.p12`, `*.pfx`
   - `.env.example` documentando variables sin valores

## Reporte (`security/report.md`)

Por cada secreto encontrado: archivo + commit (hash corto) + rama + tipo de secreto + estado (activo/rotado) + severidad:

| Situación | Severidad |
|-----------|-----------|
| Secreto activo en historial de repo público | Critical |
| Secreto activo en historial de repo privado | High |
| Secreto rotado pero aún en historial | Medium |
| Key pública frontend (pk_, AIza) bien usada | Info (documentar el riesgo de diseño) |
| .env correctamente ignorado y sin historial | Info |
| Source maps en producción | Medium |

**Regla de redacción:** en el informe, el secreto se muestra truncado (`sk_live_••••abcd`), nunca el valor completo.
