@echo off
REM ============================================
REM endpoint-authz-check.bat - Verifica que endpoints
REM protegidos rechacen peticiones sin autenticacion
REM Uso: endpoint-authz-check.bat <base_url> [token] [endpoints.txt]
REM   endpoints.txt formato: METODO /ruta  (una por linea, # = comentario)
REM   Ej:  endpoint-authz-check.bat https://target.com mytoken endpoints.txt
REM Salida: security\evidence\endpoint-authz.csv
REM ============================================
setlocal enabledelayedexpansion

set BASE=%1
set TOKEN=%2
set FILE=%3
if "%FILE%"=="" set FILE=endpoints.txt
set OUT=security\evidence\endpoint-authz.csv

if "%BASE%"=="" (
    echo Uso: endpoint-authz-check.bat ^<base_url^> [token] [endpoints.txt]
    exit /b 1
)
if not exist "%FILE%" (
    echo ERROR: archivo %FILE% no encontrado
    exit /b 1
)
if not exist "security\evidence" mkdir "security\evidence"

echo METODO,RUTA,CODIGO_SIN_AUTH,REDIREC,RESULTADO,CODIGO_CON_TOKEN > "%OUT%"

for /f "eol=# tokens=1,2" %%a in (%FILE%) do (
    if not "%%b"=="" (
        set "URL=!BASE!%%b"
        set CODE=
        set REDIR=
        for /f %%c in ('curl -s -o nul -w "%%{http_code}" -X %%a "!URL!"') do set CODE=%%c
        for /f %%d in ('curl -s -o nul -w "%%{redirect_url}" -X %%a "!URL!"') do set REDIR=%%d
        if "!CODE!"=="401" (set RES=OK) else if "!CODE!"=="403" (set RES=OK) else (set RES=FALLO)
        set CT=
        if not "!TOKEN!"=="" (
            for /f %%e in ('curl -s -o nul -w "%%{http_code}" -X %%a -H "Authorization: Bearer !TOKEN!" "!URL!"') do set CT=%%e
        )
        echo %%a,%%b,!CODE!,!REDIR!,!RES!,!CT! >> "%OUT%"
        echo %%a %%b  sin-auth: !CODE! (!RES!)  con-token: !CT!
    )
)

echo.
echo Resultados: %OUT%  (FALLO = accesible sin auth - investigar)
endlocal
