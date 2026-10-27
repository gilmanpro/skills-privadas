---
name: validacion-con-commandcode
description: "Delega la validacion de entregables a Command Code (cmdc) en modo headless, en el mismo workspace y bloqueando hasta recibir el resultado: inventario, criterios, pruebas, residuos y secretos con veredicto PASS/FAIL. Cadena de modelos: deepseek/deepseek-v4-flash con --effort off (primero), qwen/qwen3.7-flash (segundo), modelo gratuito poolside/laguna-s-2.1-free (tercero). Usar cuando el ORQUESTADOR (fase 5, validacion final) necesite evidencia o segunda opinion de un entregable aunque no se pida la skill explicitamente; keywords: cmdc, command code, validacion externa, arnes externo, headless."
---

# Validacion con Command Code (harness externo)

## Que resuelve

Doble ciego barato: validas UN entregable con un modelo economico en su PROPIO contexto (ventana limpia, sin el sesgo de quien hizo el trabajo), con el MISMO workspace (mismo cwd: cmdc hereda tu directorio de trabajo actual) y de forma SINCRONA: la llamada shell bloquea hasta que cmdc termina y su stdout es la respuesta.

## Arbol de decision

1. **Necesitas pruebas/lint (Pasada 2 completa)** → comando BASE con `--yolo` (los tests son shell mutante; sin el flag, cmdc los bloquea):

```
type .tmp\validacion_cmdc.txt | cmdc -p -m deepseek/deepseek-v4-flash --effort off --yolo -t --skip-onboarding
```

2. **Solo inventario/criterios (Pasada 1, lectura)** → MISMO comando SIN `--yolo` (headless por defecto deniega edits/shell; lecturas corren gratis).

3. **`cmdc` no existe o devuelve error persistente** → validacion local con tus propios read/bash (fallback final); consta "validacion externa no disponible".

## Preparar el prompt (obligatorio en Windows)

El prompt de validacion va SIEMPRE en un archivo y entra por stdin — multi-linea entre comillas en cmd.exe se rompe (comillas/acentos comidos): escribe primero el archivo con tu tool de edicion (ej. `.tmp\validacion_cmdc.txt`) y despues abre el pipe `type ... | cmdc -p ...`.

Contenido autocontenido del prompt: entregables con rutas EXACTAS; criterios de termino; comandos de prueba esperados; y las restricciones duras — SOLO valida, NO edite, NO commitee, NO escriba fuera de `.tmp/`, veredicto PASS/PASS_PARCIAL/FAIL con evidencia `archivo:linea` y una linea por prueba.

## Modelos — cadena de 3 opciones (en este orden)

| # | Modelo | Costo (in/out por 1M) | Cuando baja la cadena |
|---|---|---|---|
| 1 | `deepseek/deepseek-v4-flash` | $0.15/$0.6 · cache $0.003 | Default de toda validacion |
| 2 | `qwen/qwen3.7-flash` | $0.03/$0.13 · cache $0.006 | Tras 1 fallo claro de la opcion 1 (exit 5 rate limit, exit 7 error servidor, o informe vacio/inutil) |
| 3 | `poolside/laguna-s-2.1-free` | $0/$0 | Ultimo recurso: exit 10 (creditos insuficientes) en las opciones de pago, o peticion explicita de costo cero |

- Baja a la siguiente opcion solo tras 1 fallo claro; no alternes entre modelos en cada corrida (cachos de contexto perdidos).
- Sube de nuevo a la opcion 1 en la siguiente tarea valida: la cadena es un fallback, no un estado.

## Razonamiento (thinking) — siempre OFF o el minimo

Los modelos de la validacion corren SIN thinking o en su nivel mas bajo — validar es seguir un checklist, no razonar hondo:

| Modelo | Flag | Nota |
|---|---|---|
| `deepseek/deepseek-v4-flash` | `--effort off` (SIN thinking; niveles: off/high/max) | Unico con apagon real de la cadena — va SIEMPRE en el comando |
| `qwen/qwen3.7-flash` | ninguno | No expone niveles de esfuerzo; corre al default del modelo (sin control disponible) |
| `poolside/laguna-s-2.1-free` | ninguno | Idem: sin niveles expuestos |

- Si en el futuro un modelo de la cadena expusiera `low` como nivel minimo (en vez de `off`), usa `--effort low`.
- No pases un nivel que el modelo no acepta: se degrada silenciosamente al default — no protege nada y ensucia el comando.

## Interpretar el resultado

| Exit | Significado | Accion |
|---|---|---|
| 0 | OK — stdout = informe con veredicto externo | Coteja contra tu evidencia local; es APOYO, no veredicto final |
| 8 | max-turns, respuesta parcial | Acota el prompt (menos entregables) o anade `--max-turns 60` |
| 5 / 7 | rate limit / error servidor | Reintenta UNA vez con el MISMO modelo; si falla, baja la cadena |
| 10 / 3 | creditos insuficientes / no autenticado | Baja la cadena (opcion 2 → 3) o validacion local; NO reintentes en loop |

El informe externo entra como evidencia de apoyo en la fase 5; el veredicto UNICO lo emite el orquestador combinando su Pasada 1 local con este informe. Si el veredicto externo y el local discrepan → manda el local y documenta la discrepancia. Tras PASS, el cierre git/AGENTS.md se delega en `@2-ejecutor`.

## Anti-patrones

- **Usar `cmd` en Windows**: choca con cmd.exe de Microsoft y ejecuta otra cosa. El binario es `cmdc` (alias `command-code`).
- **Prompt multi-linea entre comillas en cmd.exe**: se trunca o corrompe → siempre archivo + pipe.
- **Confiar el commit a la sesion externa**: la restriccion "no commitees" vive en el prompt, pero no la asumas como garantia; el commit lo hace `@2-ejecutor` local tras el PASS del orquestador.
- **`--yolo` fuera de un workspace de confianza**: habilita ediciones y shell sin preguntar; solo se justifica para correr pruebas en el proyecto en curso.
- **Asumir que exit 0 = PASS**: exit 0 solo dice que el run termino; lee el veredicto del stdout.
- **Reintentar en loop ante exit 3/10**: es senal de plan/credenciales, no de fallo transitorio — baja la cadena.

## Problemas comunes

- `cmdc no se reconoce` → el npm global bin no esta en PATH; prueba la ruta completa `%APPDATA%\npm\cmdc.cmd`.
- `el proceso se corta por timeout` → usa `--max-turns 30` y divide el lote de entregables en dos corridas.
- `stdin timeout (30 s)` → el pipe no llego datos; verifica que el archivo `.tmp\validacion_cmdc.txt` exista ANTES de la barra vertical.
- `salida vacia con exit 0` → trata como fallo de validacion; re-corre una vez sin `--yolo` y, si persiste, baja la cadena.
