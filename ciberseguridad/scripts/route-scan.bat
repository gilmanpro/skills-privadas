@echo off
REM ============================================
REM route-scan.bat — Verifica rutas sensibles
REM Uso: route-scan.bat <url>
REM Lista: scripts\paths\common-sensitive-paths.txt
REM Imprime rutas con status != 404/403 y contenido > 0
REM ============================================
setlocal enabledelayedexpansion
set URL=%1
if "%URL%"=="" (
    echo Uso: route-scan.bat ^<url^>
    exit /b 1
)
set LIST=%~dp0paths\common-sensitive-paths.txt
if not exist "%LIST%" (
    echo No existe %LIST%
    exit /b 1
)
if not exist security mkdir security
set OUT=security\route-scan-%DATE:~-4%%DATE:~3,2%%DATE:~0,2%-%TIME:~0,2%%TIME:~3,2%.txt
set OUT=%OUT: =0%
echo ========================================
echo  ROUTE SCAN — %URL%
echo ========================================
echo Filtrando: status ^<^> 404/403 con contenido ^> 0 bytes
echo.
for /f "usebackq delims=" %%p in ("%LIST%") do (
    for /f "tokens=1-3 delims=|" %%a in ('curl -s -o nul -w "%%{http_code}^|%%{size_download}^|%%{content_type}" --max-time 10 "%URL%/%%p"') do (
        set code=%%a
        set size=%%b
        set ctype=%%c
        if not "!code!"=="404" if not "!code!"=="403" if !size! gtr 0 (
            echo   !code!  !size!B  /%%p  [!ctype!]
            echo !code!  !size!B  /%%p  [!ctype!] >> "%OUT%"
        )
    )
)
echo.
echo Resultados guardados en: %OUT%
endlocal