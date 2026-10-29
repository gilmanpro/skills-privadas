# skills-privadas

Indice **privado** de referencia de la coleccion de skills de OpenCode de [gilmanpro](https://github.com/gilmanpro) sin visibilidad publica. Cada skill vive en su **propio repositorio privado** (espejo de `~/.agents/skills/<nombre>/`); este repo ya no guarda contenido: solo la ficha y el enlace.

| Skill | Que hace | Repo |
|---|---|---|
| agent-browser | Guia en espanol de la CLI `agent-browser` de Vercel (automatizacion de navegador por CDP) | [gilmanpro/agent-browser](https://github.com/gilmanpro/agent-browser) |
| ciberseguridad | Auditoria de seguridad y hardening de proyectos software propios (web, API, red) | [gilmanpro/ciberseguridad](https://github.com/gilmanpro/ciberseguridad) |
| cloudpanel-cli | CLI de CloudPanel (`clpctl`): IPs de Cloudflare, backups, dominios, SSL | [gilmanpro/cloudpanel-cli](https://github.com/gilmanpro/cloudpanel-cli) |
| computer-use-orca | Inspeccion y entrada de escritorio en ventanas visibles via `orca` | [gilmanpro/computer-use-orca](https://github.com/gilmanpro/computer-use-orca) |
| context7 | Skill oficial de Context7 (docs y APIs actualizadas; contenido upstream en ingles) | [gilmanpro/context7](https://github.com/gilmanpro/context7) |
| curl-expert | Experto en curl: peticiones HTTP/HTTPS desde terminal y depuracion | [gilmanpro/curl-expert](https://github.com/gilmanpro/curl-expert) |
| dev-stack | Stack unificado de desarrollo: UI web, Go, compilacion, despliegue y decompilacion PyInstaller | [gilmanpro/dev-stack](https://github.com/gilmanpro/dev-stack) |
| diseno-marcas | Identidad visual de MiBus, ITSE, gilman.pro y Electrocontrol | [gilmanpro/diseno-marcas](https://github.com/gilmanpro/diseno-marcas) |
| gilman-correo | Envio de correos electronicos desde el servidor Gilman Mail (gilman.pro) | [gilmanpro/gilman-correo](https://github.com/gilmanpro/gilman-correo) |
| orca-cli | Operar worktrees, contextos de carpeta, terminales, repos y automatizaciones de Orca | [gilmanpro/orca-cli](https://github.com/gilmanpro/orca-cli) |
| orchestration | Orquestar workers de Orca coordinados (mensajes, ask/reply, tareas) | [gilmanpro/orchestration](https://github.com/gilmanpro/orchestration) |
| playwright-cli | Automatizacion de navegador con Playwright CLI | [gilmanpro/playwright-cli](https://github.com/gilmanpro/playwright-cli) |
| skills-archivadas | Respaldo historico del arbol `archivadas/`: 26 skills archivadas (absorbidas por las super skills consolidadas o retiradas), contenido sanitizado; no es una skill individual sino el espejo del grupo | [gilmanpro/skills-archivadas](https://github.com/gilmanpro/skills-archivadas) |
| validacion-con-commandcode | Delegar la validacion de entregables a Command Code (`cmdc`) en modo headless | [gilmanpro/validacion-con-commandcode](https://github.com/gilmanpro/validacion-con-commandcode) |
| wsl-raspberry-ssh | Crear una distro WSL del SO elegido y conectar por SSH a una Raspberry Pi | [gilmanpro/wsl-raspberry-ssh](https://github.com/gilmanpro/wsl-raspberry-ssh) |

No incluida: `go-worker-pool` (carpeta sin `SKILL.md`, no es una skill registrada).

**Indice de las skills con repo publico**: [skills-publicas](https://github.com/gilmanpro/skills-publicas).

## Instalacion

Copia la carpeta de la skill desde su repo a `~/.agents/skills/<nombre>/` (global) o `<proyecto>/.opencode/skills/<nombre>/`, o usa `cmdc skills add gilmanpro/<nombre> -g` (los repos privados requieren `gh auth login`).

## Notas

- Cada repo por skill excluyo el estado generado (`.tmp/`, `.cache/`, `__pycache__/`, `.env`) y los junctions del vendor UI/UX de `dev-stack` (su contenido real vive en `dev-stack/ui-ux-pro-max/repo/`).
- Verificacion de cada skill: `python skill-creator/scripts/quick_validate.py <nombre>` y `python skill-creator/scripts/auditar_seguridad.py <nombre>`.
