# Flujo Interactivo — Preguntas al Usuario

## Por qué es crítico preguntar al usuario

El bytecode te dice **qué** hace el código, pero no siempre **por qué** o **con qué contexto**. El usuario:

- Sabe qué **comportamiento observa** cuando ejecuta el .exe
- Conoce el **sistema destino** (GoalReport, formulario web, app de escritorio)
- Puede identificar **patrones** que el bytecode no revela
- Sabe si el .exe **funciona correctamente** o tiene bugs

**Caso real documentado:** En la conversación de referencia, el bytecode mostraba:
- `INT: 10` en constantes
- `STR: '\t'` y `STR: 'backspace'` 

La interpretación inicial fue `typewrite → press([tab,down,space]) → press(backspace)`.
Pero el usuario corrigió: el `10` era `presses=10`, haciendo `press('\t', presses=10)` — **10 TABs para navegar hacia arriba**, y luego `backspace` para borrar todo.

**Sin preguntar, la reconstrucción habría sido incorrecta.**

---

## Cuándo preguntar

### 1. CONSTANTES AMBIGUAS

Cuando encuentres números o strings cuyo propósito no sea 100% obvio:

```
🔍 Encontré estas constantes que no tengo del todo claras:

  [N] INT: 10 → ¿Podría ser la cantidad de repeticiones de una tecla? 
                 ¿O un timeout? ¿O un límite de iteraciones?

  [N] STR: '\t' → Esta tecla TAB, ¿se presiona 1 vez o múltiples?
```

### 2. COMPORTAMIENTO OBSERVADO

```
❓ Cuando ejecutas el .exe, ¿qué ves exactamente?

  1. ¿Aparece una ventana? ¿Cuál?
  2. ¿Escribe números en algún campo específico?
  3. ¿Ves que el cursor se mueve entre campos con TAB?
  4. ¿Hay alguna cuenta regresiva antes de empezar?
  5. ¿Cuánto tiempo tarda entre número y número?
  6. ¿Alguna vez borra lo que escribió?
```

### 3. SISTEMA DESTINO

```
❓ ¿En qué sistema se tipean los números?

  - ¿Es GoalReport (sistema de gestión)?
  - ¿Un formulario web? ¿Cuál?
  - ¿Una aplicación de escritorio?
  - ¿Una terminal / consola?

  Esto ayuda a entender la secuencia de teclas:
  TAB + DOWN + SPACE ≠ TAB + DOWN + SPACE en todos los sistemas
```

### 4. ARCHIVO DE ENTRADA

```
❓ Sobre el archivo Excel de entrada:

  - ¿Los números están en la columna A?
  - ¿Hay encabezados? (fila 1)
  - ¿Son solo números enteros, o también decimales?
  - ¿El .exe recibe la ruta del Excel como argumento?
```

### 5. SECUENCIA DE TECLADO DETALLADA

Esta es LA pregunta más importante. Después de mostrarle tu análisis:

```
❓ Según el bytecode, la secuencia para cada número sería:

  1. Escribir el número dígito a dígito
  2. Presionar TAB + DOWN + SPACE
  3. Presionar BACKSPACE

  ¿Esto coincide con lo que observas? ¿O falta algún paso?
  ¿Ves que después de escribir, el cursor hace varios TABs?
  ¿Cuántas veces ves que se mueve hacia arriba/abajo?
```

### 6. VALORES QUE PODRÍAN SER REPETICIONES

```
❓ Encontré este número que no sé cómo interpretar:

  INT: 10 aparece como constante suelta.
  
  ¿Podría ser presses=10 (10 repeticiones de una tecla)?
  ¿El cursor retrocede exactamente 10 posiciones?
```

---

## Plantilla de mensaje para el usuario

Después del análisis inicial del bytecode, presenta esto al usuario:

```markdown
## 🔍 Análisis del ejecutable

### 📊 Lo que encontré en el bytecode

**Módulos detectados:**
- `pyautogui` → control de teclado/ratón
- `openpyxl` → lectura de Excel
- `time` → pausas y temporización
- `sys` → argumentos de línea de comandos

**Estructura del programa:**
1. Lee un Excel (columna A, solo valores numéricos)
2. Cuenta regresiva 9→0 con sleep(1)
3. Pausa de 3 segundos
4. Por cada número: secuencia de teclado
5. Muestra tiempo total al final

### 🤔 Zonas de ambigüedad (necesito tu ayuda)

| Constante | Mi interpretación | Lo que podría ser |
|---|---|---|
| INT: 10 | sleep(10) | **O** presses=10 (repeticiones) |
| TUPLE: ('\\t', 'down', 'space') | Presionar TAB, DOWN, SPACE | — (esto está claro) |
| STR: '\\t' sola | Otra tecla TAB | **O** parte de press con repeticiones |

### ❓ Preguntas:

1. Cuando ejecutas el .exe, ¿cuánto tiempo pasa entre que termina la cuenta regresiva y empieza a tipear?
2. ¿Ves que después de escribir un número, el cursor se mueve varias veces con TAB antes de borrar?
3. ¿Los números se escriben de corrido o con pausa entre dígitos?
4. ¿El Excel tiene solo una columna de números? ¿Hay encabezado?

### 📝 Mi reconstrucción tentativa (sujeta a tus respuestas):

```python
for x in contenido:
    pyautogui.typewrite(x, interval=0.1)
    pyautogui.press(['\\t', 'down', 'space'])
    pyautogui.press('backspace')
```

¿Se ve correcto? ¿Falta algo?
```

---

## Proceso iterativo de refinamiento

```
1. ANÁLISIS INICIAL
   ↓
2. PRESENTAR al usuario + PREGUNTAR
   ↓
3. USUARIO RESPONDE (corrige, añade contexto)
   ↓
4. REFINAR interpretación
   ↓
5. RE-CONSTRUIR código corregido
   ↓
6. ¿Hay más dudas? ──SÍ──→ volver a 2
   ↓ NO
7. VERIFICAR sintaxis
   ↓
8. ENTREGAR código final
```

### Ejemplo de múltiples iteraciones (de la conversación real):

**Iteración 1 — Análisis inicial:**
```
typewrite(x, interval=0.1)
press(['\t', 'down', 'space'])
press('backspace')
```

**Iteración 2 — Usuario corrige:**
> "el 10 significa que ejecuta 10 veces tap de arriba, y cuando borra elimina todo"

**Código corregido:**
```
typewrite(x, interval=0.1)
press(['\t', 'down', 'space'])
press('\t', presses=10)      ← 10 TABs hacia arriba
press('backspace')           ← borra todo lo tipeado
```

---

## Preguntas de verificación final

Cuando el código ya está reconstruido:

```
✅ Código reconstruido con ~98% de fidelidad.

¿Quieres que:
  a) Lo guarde como script Python listo para probar
  b) Genere también un .exe con PyInstaller para reemplazar el original
  c) Pruebe la sintaxis y verifique que no tenga errores
  d) Haga algún ajuste adicional
```

## Checklist de confirmación antes de entregar

- [ ] ¿Se preguntó al usuario sobre constantes ambiguas?
- [ ] ¿Se confirmó la secuencia de teclado exacta?
- [ ] ¿Se verificó el sistema destino?
- [ ] ¿Se corrigió el código basado en feedback?
- [ ] ¿Se verificó la sintaxis con `ast.parse()`?
- [ ] ¿Se documentó el % de certeza?
- [ ] ¿Se preguntó si quiere probar el código?
