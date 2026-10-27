---
name: playwright-cli
description: "Automatizar navegadores con Playwright CLI: navegar, interactuar con elementos, snapshots de accesibilidad, screenshots, testing E2E, manejo de sesiones/auth, trazado de red y grabacion de video. Usar SIEMPRE que el usuario pida automatizar un navegador, scrapear una pagina dinamica, probar una web o debuggear flujos de usuario con Playwright."
---

# playwright-cli

Automatiza navegadores con `playwright-cli` mediante comandos de terminal.

## Cuándo usar

- Automatizar flujos de usuario en navegadores
- Tomar snapshots y screenshots de páginas
- Depurar aplicaciones web interactivamente
- Grabar sesiones de navegación
- Probar formularios y autenticación

## Instalación

```bash
npm install -g @playwright/cli@latest
# O local: npx playwright cli <comando>
```

## Flujo básico

```bash
playwright-cli open https://example.com
playwright-cli snapshot
playwright-cli fill e1 "user@example.com"
playwright-cli fill e2 "password123"
playwright-cli click e3
playwright-cli snapshot
playwright-cli close
```

## Comandos esenciales

| Categoría | Comandos |
|---|---|
| Navegación | `open`, `goto`, `go-back`, `go-forward`, `reload` |
| Interacción | `click <ref>`, `type <text>`, `fill <ref> <text>`, `press <key>` |
| Snapshot | `snapshot`, `snapshot --filename=after.yaml` |
| Tabs | `tab-list`, `tab-new [url]`, `tab-close [id]` |
| Storage | `state-save/load`, `cookie-list/get/set`, `localstorage-list/get/set` |
| Network | `requests`, `route <pattern> --status=<code>` |
| DevTools | `console [level]`, `tracing-start/stop`, `video-start/stop` |
| Sesiones | `-s=<name> --persistent`, `list`, `close-all`, `kill-all` |

## Targeting

Usa refs del snapshot (`e15`), selectores CSS o locators:

```bash
playwright-cli click "#main > button.submit"
playwright-cli click "getByRole('button', { name: 'Submit' })"
playwright-cli click "getByTestId('submit-button')"
```

## Opciones de open

```bash
playwright-cli open --browser=chrome|firefox|webkit|msedge
playwright-cli open --persistent
playwright-cli attach --cdp=chrome
# Emulación móvil: vía contextOptions (viewport/isMobile/touch) en .playwright/cli.config.json
```

## Desinstalación

```bash
playwright-cli kill-all && playwright-cli delete-data
npm uninstall -g @playwright/cli
# Playwright no tiene comando 'uninstall': borra la caché de navegadores a mano
# Windows: rmdir /s /q "%LOCALAPPDATA%\ms-playwright"   Unix: rm -rf ~/.cache/ms-playwright
npm cache clean --force
```

## Referencias

- `references/playwright-tests.md` — ejecutar y debuggear tests.
- `references/request-mocking.md` — mocking de requests.
- `references/running-code.md` — ejecutar código en el browser.
- `references/session-management.md` — gestión de sesiones.
- `references/storage-state.md` — cookies, localStorage y state.
- `references/test-generation.md` — generación de tests.
- `references/tracing.md` — tracing.
- `references/video-recording.md` — grabación de video.
- `references/element-attributes.md` — inspección de atributos.
