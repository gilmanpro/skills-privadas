# Evals de agent-browser

Set de evaluaciones creado segun el ciclo de creacion de `skill-creator`
(eval antes/despues del contenido, activacion + rendimiento).

## Ficheros

- `trigger.json` — 10 queries de activacion (5 deben disparar, 5 no; los
  negativos son casi-acierto: comparten keywords de navegador/web pero piden
  otra cosa). Formato: `[{"query": "...", "should_trigger": true|false}]`.
- `evals.json` — 3 escenarios de rendimiento con `expected_output`
  verificable (sesion propia + flujo open/snapshot/click; extraccion JSON
  sin HTML crudo; espera condicional + captura con `--if-changed` + close).

## Como ejecutarlos

```bash
# Desde skill-creator/
python -m scripts.run_eval --eval-set ..\agent-browser\evals\trigger.json --skill-path ..\agent-browser --verbose

# Optimizacion de description (train/test 60/40, 3 corridas por query):
python -m scripts.run_loop --eval-set ..\agent-browser\evals\trigger.json --skill-path ..\agent-browser --model <provider/model> --max-iterations 5 --verbose
```

## Regla critica: sacar la skill del arbol mientras se mide

`run_eval` instala una copia desechable con nombre unico
(`agent-browser-skl-<hex>`) en `.opencode/skills/` y solo cuenta trigger si
la PRIMERA llamada a la herramienta `skill` menciona ese nombre unico. Este
repo **es** `~/.agents/skills`, asi que la skill real `agent-browser` esta
globalmente visible: el agente la carga a ella (nombre de dominio) y toda
query positiva contaria como falso negativo. Antes de medir, moverla fuera:

```bat
move %USERPROFILE%\.agents\skills\agent-browser %TEMP%\agent-browser-hold
python -m scripts.run_eval --eval-set %TEMP%\agent-browser-hold\evals\trigger.json --skill-path %TEMP%\agent-browser-hold --runs-per-query 1 --verbose
move %TEMP%\agent-browser-hold %USERPROFILE%\.agents\skills\agent-browser
```

(El `finally` de `run_eval` limpia la copia desechable; si se mata la
corrida, revisar `.opencode/skills/` por restos `*-skl-*`.)

## Estado

- 2026-10-27: ejecucion BLOQUEADA — el proveedor configurado en opencode
  (`1-orquestador` → `mimo-v2.6-pro`) devuelve `429 quota exhausted`; con la
  API caida el eval mide 0 en todo (los negativos "pasan" por el error, no
  por la description). Reejecutar cuando la cuota vuelva; los resultados de
  esa corrida no son validos.
