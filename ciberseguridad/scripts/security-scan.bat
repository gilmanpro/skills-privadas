@echo off
REM ============================================
REM security-scan.bat — Escaneo rapido de seguridad
REM Uso: security-scan.bat <url> [puerto]
REM Ej:  security-scan.bat https://target.com 443
REM ============================================
setlocal enabledelayedexpansion

set URL=%1
set PORT=%2
if "%PORT%"=="" set PORT=443
set OUTDIR=security

if "%URL%"=="" (
    echo Uso: security-scan.bat ^<url^> [puerto]
    echo Ej:  security-scan.bat https://target.com 443
    exit /b 1
)

if not exist "%OUTDIR%" mkdir "%OUTDIR%"
if not exist "%OUTDIR%\evidence" mkdir "%OUTDIR%\evidence"
if not exist "%OUTDIR%\scans" mkdir "%OUTDIR%\scans"

echo ========================================
echo  SECURITY SCAN — %URL%
echo  Started: %DATE% %TIME%
echo ========================================

REM === 1. RECON: HEADERS DE SEGURIDAD ===
echo [1/6] Analizando headers de seguridad...
curl -sI -L "%URL%" > "%OUTDIR%\evidence\headers.txt"
findstr /i "strict-transport-security content-security-policy x-frame-options x-content-type-options referrer-policy permissions-policy" "%OUTDIR%\evidence\headers.txt" > "%OUTDIR%\scans\security-headers.txt"
if %errorlevel% equ 0 (
    echo   Algunos headers encontrados. Revisar: %OUTDIR%\scans\security-headers.txt
) else (
    echo   ⚠ NO se encontraron security headers
)

REM === 2. RECON: METODOS HTTP ===
echo [2/6] Probando metodos HTTP peligrosos...
curl -s -o nul -w "  OPTIONS: %%{http_code}\n" -X OPTIONS "%URL%"
curl -s -o nul -w "  PUT:     %%{http_code}\n" -X PUT "%URL%/test"
curl -s -o nul -w "  DELETE:  %%{http_code}\n" -X DELETE "%URL%/test"
curl -s -o nul -w "  TRACE:   %%{http_code}\n" -X TRACE "%URL%"

REM === 3. RECON: TIMING BASELINE ===
echo [3/6] Midiendo tiempos de respuesta baseline...
set total=0
for /l %%i in (1,1,5) do (
    for /f %%t in ('curl -s -o nul -w "%%{time_total}" "%URL%"') do set t=%%t
    echo   Request %%i: !t!s
)

REM === 4. VULN: PATH TRAVERSAL y ARCHIVOS SENSIBLES ===
echo [4/6] Probando archivos sensibles comunes...
for %%f in (.env .git/config backup.zip admin wp-admin phpinfo.php composer.json package.json) do (
    curl -s -o nul -w "  /%%f: %%{http_code}\n" "%URL%/%%f"
)

REM === 5. VULN: CORS ===
echo [5/6] Probando configuracion CORS...
curl -s -I -H "Origin: https://evil.com" "%URL%" | findstr /i "access-control-allow-origin" > nul
if %errorlevel% equ 0 (
    echo   ⚠ CORS permite origen externo — REVISAR
) else (
    echo   CORS OK — no permite origenes externos
)

REM === 6. REPORTE RAPIDO ===
echo [6/6] Generando reporte rapido...
(
    echo # Security Scan Report
    echo Target: %URL%
    echo Date: %DATE% %TIME%
    echo.
    echo ## Resumen
    echo.
    echo ## Hallazgos
    echo.
    echo ### Security Headers
    type "%OUTDIR%\scans\security-headers.txt" 2>nul
    echo.
    echo ### Metodos HTTP
    echo Revisar evidencia en archivos de salida.
    echo.
    echo ### Archivos Sensibles
    echo Revisar salida de escaneo.
    echo.
    echo ### CORS
    echo Ver resultado del test.
) > "%OUTDIR%\report.md"

echo ========================================
echo  SCAN COMPLETADO
echo  Reporte: %OUTDIR%\report.md
echo  Evidencia: %OUTDIR%\evidence\
echo ========================================
endlocal
