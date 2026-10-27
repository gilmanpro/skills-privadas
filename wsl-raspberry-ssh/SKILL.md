---
name: wsl-raspberry-ssh
description: "Crear una distro WSL del SO que elija el usuario (preguntar SIEMPRE el SO, con Debian por defecto si no indica otro), configurar usuario/contrasena, exponer su SSH en un puerto libre de Windows y publicarlo por tunel a un puerto publico del VPS, usando las tools MCP del servidor wsl-port. Usar SIEMPRE que el usuario pida: crear distro wsl con ssh, crear distro raspberry en wsl, distro debian/ubuntu/kali/raspberry en wsl con tunel, publicar ssh de wsl al vps, raspberry pi os wsl con tunel, exponer ssh wsl-port, o cualquier flujo importar distro + forward Windows-WSL + tunel VPS. Aunque no nombre wsl-port ni el SO explicitamente."
---

# wsl-raspberry-ssh: distro WSL (SO a elegir, Debian por defecto) con SSH publicado al VPS

Flujo end-to-end: crear/traer una distro WSL del SO elegido por el usuario (Paso 0; Debian por defecto) → usuario con sudo → sshd → forward Windows→WSL en puerto libre → tunel al VPS en puerto publico libre → prueba `ssh`. Todo con las tools MCP del servidor `wsl-port` (via `execute`/code mode).

## Paso 0 — PREGUNTAR ANTES de ejecutar (obligatorio)

Al activarse la skill, NO ejecutar nada todavia. Usar la tool `question` (o preguntas numeradas) para recoger estos 3 parametros en la MISMA ronda de preguntas:

1. **SO/distro a crear** — OBLIGATORIO PREGUNTARLO SIEMPRE con la tool `question`, junto con usuario y contrasena. NUNCA asumirlo implicitamente ni dar por hecho Raspberry Pi OS u otro SO. OPCION POR DEFECTO: **Debian** (ultima version estable), marcada como tal en la pregunta (p. ej. "1. Debian (por defecto)"): si el usuario no elige otro SO, se usa Debian. Alternativas: Raspberry Pi OS, Ubuntu, Kali y cualquier perfil que devuelva `profile_list` del MCP `wsl-port` (ver Paso 1a); si la lista no carga, ofrecer Debian (por defecto), Raspberry Pi OS, Ubuntu y Kali.
2. **Nombre de usuario** de la distro — SIN default, obligatorio.
3. **Contrasena** del usuario — SIN default, obligatorio. Regla: NO repetir la contrasena en claro en el reporte final ni en logs; usar placeholder `<CONTRASENA>`.

Si el usuario ya dio alguno de estos datos en su mensaje, no volver a preguntarlo: confirmar y continuar con los que falten.

## Paso 1 — Descubrir las tools MCP (no adivinar nombres)

Las tools se acceden en code mode via `tools["wsl-port"]*`. Antes de la primera llamada:

```js
// dentro de execute
const t = search({ namespace: "wsl-port" }); // lista EXACTA de tools y firmas
```

Nunca inventar nombres de tool: usar solo los `path` que devuelve `search`. Nombres citados abajo (`profile_list`, `vps_list`, `tunnel_list`, etc.) son los verificados por esta skill; si `search` muestra otra grafia, primar la de `search`.

### 1a. Perfiles y creacion de la distro (flujo a)

1. `profile_list` → obtener perfiles disponibles (distro, usuario, recursos) y las opciones para la pregunta del Paso 0.
2. Elegir un nombre de distro unico (p. ej. `debian-ssh-1`; `wsl -l` / listado de distros para no chocar).
3. Crear/importar la distro elegida: usar la tool MCP de crear/importar correspondiente (perfil o `wsl --import` si no hay perfil). WSL exige **carpeta propia por distro**; si el destino ya tiene una (`base.tar`/`ext4.vhdx`), la CLI/MCP registra en `<dir>/<nombre>` para evitar `Wsl/Service/RegisterDistro/ERROR_FILE_EXISTS`.

### 1b. Usuario con sudo y default-user (flujo b)

Dentro de la distro (via la tool MCP de exec/comandos en distro, o `wsl -d <distro> -u root -- <cmd>`):

```bash
useradd -m -s /bin/bash <usuario>
echo '<usuario>:<CONTRASENA>' | chpasswd
usermod -aG sudo <usuario>        # en Debian/Raspbian/Ubuntu; en Kali: usermod -aG sudo
# default-user de la distro:
#   option --user <usuario> default  (WSL >= 0.64), o en /etc/wsl.conf:
#   [user]\ndefault=<usuario>
```

Despues de tocar `/etc/wsl.conf`: `wsl --terminate <distro>` y arrancar de nuevo para aplicar.

### 1c. openssh-server + sshd (flujo c)

```bash
apt-get update && apt-get install -y openssh-server
ssh-keygen -A 2>/dev/null || true
mkdir -p /run/sshd
/usr/sbin/sshd            # arrancar sin systemd; verificar con: pgrep -a sshd
# opcional persistente: systemctl enable ssh && systemctl start ssh (si systemd activo)
```

Puerto interno sugerido para la distro: **22** (o el que indique el perfil). Anotar el puerto WSL para el forward.

### 1d. Forward Windows→WSL en puerto libre (flujo d)

1. Obtener puertos Windows LIBRES:
   - API de expuestos (ocupados por otras distros): `GET https://wsl-port.gilman.pro/api/v1/ports/exposed` → JSON `{ok, ports:[{listen_port, wsl_distro, service, state, ...}]}`. Historico de ocupados: **2222, 2223, 2224** (sshd de kali/alantede-2/abel-1-debian) y **9119** (hermes). NO reutilizar ninguno que aparezca aqui.
   - Validar ademas en local: `netstat -ano | findstr :<puerto>` (debe salir vacio).
2. Elegir el primer puerto libre del rango de SSH (p. ej. 2225 en adelante) y crear el forward con la tool MCP de forwards (equivale a `wsl-port forwards add --id <distro>-ssh --listen-port <pW> --distro <distro> --wsl-port <pWSL>`).

### 1e. Puerto publico libre del VPS (flujo f)

- Panel: `https://puertos-disponibles.gilman.pro/` — muestra puertos TCP LISTEN disponibles en el rango **10001-65535**.
- Es un panel JS: para consultarlo en automate, descubrir su API inspeccionando el JS de la pagina (ver requests XHR/fetch en el HTML/JS) y llamar esa endpoint con `fetch` en code mode.
- Alternativa MCP mas simple: `vps_list` (unico VPS configurado) + `tunnel_list` (tuneles activos) para deducir puertos remotos ocupados, y cruzar con el panel.
- Elegir un puerto publico NO ocupado y recordarlo.

### 1f. Tunel al VPS y verificacion (flujo g)

1. `vps_list` → confirmar el UNICO VPS disponible y su id/host.
2. Crear el tunel con la tool MCP de tunnels: local = `<puertoWindows>` del forward, remoto = `<puertoPublico>` del VPS, tipo ssh. (Equivale a `wsl-port tunnels add --id <distro>-pub --vps <vps> --local-port <pW> --remote-port <pPub> --type ssh` y `tunnels start`.)
3. Verificar con `tunnel_list`: estado activo/ok del tunel nuevo.

### 1g. Prueba de conexion (flujo h)

```powershell
ssh <usuario>@127.0.0.1 -p <puertoWindows>    # pide la contrasena del Paso 0
```

Si responde, el flujo esta completo. Reportar: distro, usuario, puerto Windows, puerto publico VPS, ids de forward/tunel. **Nunca** reportar la contrasena en claro.

## Restricciones y anti-patrones

- **No tocar tuneles/forwards de otras distros existentes**: solo crear/modify los items cuyo `--id`/nombre pertenezca a la distro de esta ejecucion. Motivo: romper el SSH publicado de kali, alantede-2, abel-1-debian, etc.
- No adivinar nombres de tools MCP sin pasar por `search({namespace:"wsl-port"})`: una firma mal elegida falla o ejecuta la accion equivocada.
- No hardcodear puertos ocupados: validar SIEMPRE contra la API `/api/v1/ports/exposed` + `netstat` en el momento de ejecutar (el historico 2222-2224/9119 es solo referencia).
- No elegir puerto publico sin consultar el panel de puertos disponibles o `tunnel_list`: colision de LISTEN en el VPS deja el tunel en fallo.
- No ejecutar el flujo sin los 3 parametros del Paso 0 (SO, usuario, contrasena), ni inventar usuario/contrasena/SO distintos de los indicados. El default de distro es Debian SOLO si el usuario no eligio otra; nunca asumir un SO distinto por defecto.
- No dejar la contrasena en el reporte, en el titulo de la sesion ni en archivos.

## Errores comunes

| Error | Causa / arreglo |
|---|---|
| `RegisterDistro/ERROR_FILE_EXISTS` | Carpeta de import ocupada: crear la distro en `<dir>/<nombre>` propio |
| `ssh: connect ... refused` en 127.0.0.1 | sshd no arranco dentro de WSL (`pgrep sshd`) o el forward apunta otro puerto: revisar 1c y 1d |
| Forward en estado `missing` | Distro apagada o IP WSL cambiada: arrancar la distro y `forwards apply` (tool MCP de apply) |
| Tunel `FAILED` al arrancar | Puerto publico ya en LISTEN en el VPS: elegir otro con el panel y recrear el tunel |
| `wsl` no responde | Servicio WSL caido: `wsl --shutdown` y reintentar |
| Cambio de default-user no aplica | Falta `wsl --terminate <distro>` tras editar `/etc/wsl.conf` |
