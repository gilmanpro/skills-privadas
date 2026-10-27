# skills-privadas

Coleccion **privada** de 14 skills de OpenCode (estandar [Agent Skills](https://agentskills.io)) que no tienen repositorio propio. Espejo de las carpetas de `~/.agents/skills/`; cada carpeta es una skill autocontenida (`SKILL.md` + `references/` + `scripts/` cuando aplica).

## Skills incluidas

| Skill | Que hace |
|---|---|
| `agent-browser` | Guia en espanol de la CLI `agent-browser` de Vercel (automatizacion de navegador por CDP) |
| `ciberseguridad` | Auditoria de seguridad y hardening de proyectos software propios (web, API, red) |
| `cloudpanel-cli` | CLI de CloudPanel (`clpctl`): IPs de Cloudflare, backups, dominios, SSL |
| `computer-use-orca` | Inspeccion y entrada de escritorio en ventanas visibles via `orca` |
| `context7` | Skill oficial de Context7 (docs y APIs actualizadas; contenido upstream en ingles) |
| `curl-expert` | Experto en curl: peticiones HTTP/HTTPS desde terminal y depuracion |
| `dev-stack` | Stack unificado de desarrollo: UI web, Go, compilacion, despliegue y decompilacion PyInstaller |
| `diseno-marcas` | Identidad visual de MiBus, ITSE, gilman.pro y Electrocontrol |
| `gilman-correo` | Envio de correos electronicos desde el servidor Gilman Mail (gilman.pro) |
| `orca-cli` | Operar worktrees, contextos de carpeta, terminales, repos y automatizaciones de Orca |
| `orchestration` | Orquestar workers de Orca coordinados (mensajes, ask/reply, tareas) |
| `playwright-cli` | Automatizacion de navegador con Playwright CLI |
| `validacion-con-commandcode` | Delegar la validacion de entregables a Command Code (`cmdc`) en modo headless |
| `wsl-raspberry-ssh` | Crear una distro WSL del SO elegido y conectar por SSH a una Raspberry Pi |

## Instalacion

Copia la carpeta de la skill que necesites a:

- `~/.agents/skills/<nombre>/` (global, compatibilidad herencia)
- `<proyecto>/.opencode/skills/<nombre>/` (proyecto)

## Notas de publicacion

- Contenido sanitizado: sin rutas personales (placeholders `C:\Users\...` / `C:\Users\yo` son ejemplos), sin secretos (solo referencias `${env:VAR}` / `{file:...}`) y sin IPs reales (CIDRs `192.168.x.x` etc. son ejemplos de documentacion).
- Excluido de este espejo el estado generado: `.tmp/`, `.cache/`, `__pycache__/`, `.env`, `.uso_diario.json`, `node_modules/` y los junctions del vendor UI/UX de `dev-stack` (su contenido real vive en `dev-stack/ui-ux-pro-max/repo/`).

## Verificacion

```bash
python skill-creator/scripts/quick_validate.py <nombre>
python skill-creator/scripts/auditar_seguridad.py <nombre>
```
