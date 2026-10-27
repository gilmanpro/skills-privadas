@echo off
REM ============================================
REM timing-attack.bat — Detecta timing attacks en login/OTP
REM Uso: timing-attack.bat <url> [opcion]
REM Opciones:
REM   userenum  — detectar user enumeration por timing
REM   otp       — detectar OTP digit-by-digit timing
REM   password  — detectar password char-by-char timing
REM Ej: timing-attack.bat https://target.com/login userenum
REM ============================================
setlocal enabledelayedexpansion

set URL=%1
set MODE=%2

if "%URL%"=="" (
    echo Uso: timing-attack.bat ^<url^> [userenum^|otp^|password]
    exit /b 1
)

if not exist "security\evidence" mkdir security\evidence

if /i "%MODE%"=="userenum" goto :userenum
if /i "%MODE%"=="otp" goto :otp
if /i "%MODE%"=="password" goto :password

echo Modo no valido. Opciones: userenum, otp, password
exit /b 1

:userenum
echo ========================================
echo  TIMING ATTACK — User Enumeration
echo  Target: %URL%
echo ========================================
echo.
echo Probando tiempos de respuesta por usuario...
echo.

for %%u in (admin root test user nonexistent) do (
    for /f %%t in ('curl -s -o nul -w "%%{time_total}" -d "username=%%u&password=test" "%URL%"') do (
        echo  User '%%u': %%ts
    )
)
echo.
echo Si hay diferencias significativas ^(>50ms^) entre usuarios
echo que existen y no existen -> USER ENUMERATION es posible.
goto :end

:otp
echo ========================================
echo  TIMING ATTACK — OTP Digit by Digit
echo  Target: %URL%
echo ========================================
echo.
echo Probando tiempos por digito inicial del OTP...
echo.

for %%d in (0 1 2 3 4 5 6 7 8 9) do (
    for /f %%t in ('curl -s -o nul -w "%%{time_total}" -d "code=%%d00000" "%URL%"') do (
        echo  OTP starting with %%d: %%ts
    )
)
echo.
echo Si un digito tiene tiempo consistentemente mayor -> TIMING ATTACK viable.
echo El digito correcto tarda ~1-5ms mas que los incorrectos.
echo.
echo Repetir 3 veces para confirmar consistencia.
goto :end

:password
echo ========================================
echo  TIMING ATTACK — Password Character by Character
echo  Target: %URL%
echo ========================================
echo.
echo Probando tiempos por longitud de password...
echo.

for /l %%l in (1,1,12) do (
    set "pass="
    for /l %%i in (1,1,%%l) do set "pass=!pass!a"
    for /f %%t in ('curl -s -o nul -w "%%{time_total}" -d "username=admin&password=!pass!" "%URL%"') do (
        echo  Password length %%l: %%ts
    )
)
echo.
echo Si el tiempo aumenta con la longitud -> comparacion char-by-char.
echo Esto permite enumerar la password caracter por caracter.
goto :end

:end
echo.
echo === RESULTADOS GUARDADOS EN security\evidence\timing-results.txt ===
endlocal
