---
name: gilman-correo
description: "Envia correos electronicos desde el servidor Gilman Mail (gilman.pro): transaccionales, marketing, programados, adjuntos y verificacion de estado de entrega. Usar SIEMPRE que el usuario pida enviar un correo/email desde gilman.pro, notificar a alguien por email o comprobar si un correo fue entregado."
---

# gilman-correo — Envío de Correos

Envía correos desde el servidor `gilman.pro` via la API del panel de administracion.

## Cuándo usar

- Enviar correos transaccionales (bienvenida, notificación, alerta)
- Enviar campañas de marketing por email
- Programar envíos futuros
- Verificar estado de correos enviados

## Credenciales

| Campo | Valor |
|-------|-------|
| **URL Base** | `https://admin-correo.gilman.pro` |
| **Usuario** | `admin@gilman.pro` |
| **Contrasena** | Ver en panel o preguntar al usuario |

## Autenticacion

Login por formulario con cookie JWT. Toda peticion requiere la cookie `admin_token`:

```bash
# -k: el panel usa certificado autofirmado; quítalo si tu instalación tiene certificado válido
curl -sk -c cookies.txt -X POST https://admin-correo.gilman.pro/login \
  -d "username=admin@gilman.pro" -d "password=CONTRASENA"
```

## Endpoints

### Enviar correo inmediato
`POST /transactional/send-test`
- `from_email`, `to_email`, `subject`, `body`

```bash
curl -sk -b cookies.txt -X POST https://admin-correo.gilman.pro/transactional/send-test \
  -d "from_email=admin@gilman.pro" -d "to_email=destino@email.com" \
  -d "subject=Asunto" -d "body=<h1>Hola</h1>"
```

### Programar correo futuro
`POST /marketing/schedule`
- `from_email`, `to`, `subject`, `body`, `scheduled_at` (ISO 8601 UTC-5)

```bash
curl -sk -b cookies.txt -X POST https://admin-correo.gilman.pro/marketing/schedule \
  -d "from_email=admin@gilman.pro" -d "to=lista@gilman.pro" \
  -d "subject=Campana" -d "body=<h1>Oferta</h1>" -d "scheduled_at=2026-07-15T10:00"
```

### Ver programados
`GET /marketing` — lista schedules con estado (`pending`, `sent`, `failed`).

### Eliminar programacion
`POST /marketing/schedule/delete` con `schedule_id`.

## Scripts

```bash
# Cliente Python (scripts/send.py) — Forma A: contrasena como segundo argumento
python scripts/send.py ahora <password> <to> <subject> "<body>"
python scripts/send.py programar <password> <to> <subject> "<body>" <YYYY-MM-DDTHH:MM>
python scripts/send.py listar <password>
python scripts/send.py eliminar <password> <schedule_id>

# Forma B (recomendada): contrasena via variable de entorno GILMAN_PASSWORD
# (se omite el argumento password y los demas se desplazan)
export GILMAN_PASSWORD=tu_contrasena    # en cmd.exe: set GILMAN_PASSWORD=tu_contrasena
python scripts/send.py ahora <to> <subject> "<body>"
python scripts/send.py programar <to> <subject> "<body>" <YYYY-MM-DDTHH:MM>
python scripts/send.py listar
python scripts/send.py eliminar <schedule_id>
```

> **Seguridad:** pasar la contrasena como argumento de comando queda registrado en el historial del shell (`~/.bash_history`, historial de cmd/PowerShell) y puede verse en la lista de procesos. Prefiere `GILMAN_PASSWORD`.

## SMTP para Apps externas

| Campo | Valor |
|-------|-------|
| SMTP Host | `correo.gilman.pro` |
| Puerto | `465` (SSL) o `587` (STARTTLS) |
| Auth | Usuario + contrasena de la cuenta |

## Buenas practicas

1. SPF + DKIM + DMARC en DNS. Verifica en `https://admin-correo.gilman.pro/dns`
2. Limite: ~100 destinatarios por envio. Usa multiples envios para listas grandes
3. Calentamiento de IP: empieza con 50-100 correos/dia si la IP es nueva
4. Incluye siempre enlace de unsubscribe en campanas marketing
5. Prueba spam score en https://www.mail-tester.com
6. Horario: UTC-5 (America/Panama)
7. Crea cuentas dedicadas para apps en `https://admin-correo.gilman.pro/accounts`

> **Cliente Python** en `scripts/send.py`. Para HTML, construye el cuerpo con tablas y estilos inline.