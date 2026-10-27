@echo off
REM ============================================
REM rate-limit-test.bat — Verifica rate limit
REM Uso: rate-limit-test.bat <url> [n_requests] [metodo] [data]
REM Ej:  rate-limit-test.bat http://target.local/login 20 POST "user=admin&pass=wrong"
REM Nota: ráfaga controlada; no uses valores altos de n.
REM ============================================
setlocal enabledelayedexpansion
set URL=%1
set N=%2
set METHOD=%3
set DATA=%4
if "%URL%"=="" (
    echo Uso: rate-limit-test.bat ^<url^> [n_requests] [metodo] [data]
    exit /b 1
)
if "%N%"=="" set N=20
if "%METHOD%"=="" set METHOD=GET

echo == BASELINE ==
for /f %%t in ('curl -s -o nul -w "%%{http_code} en %%{time_total}s" --max-time 10 "%URL%"') do echo   %%t

echo.
echo == %N% REQUESTS (%METHOD%) ==
for /l %%i in (1,1,%N%) do (
    if "%DATA%"=="" (
        curl -s -o nul -w "%%{http_code}\n" --max-time 10 -X %METHOD% "%URL%"
    ) else (
        curl -s -o nul -w "%%{http_code}\n" --max-time 10 -X %METHOD% --data "%DATA%" "%URL%"
    )
)

echo.
echo == HEADERS DE RATE LIMIT ==
curl -sI --max-time 10 "%URL%" | findstr /i "ratelimit retry-after 429"
if errorlevel 1 echo   Sin headers de rate limit
endlocal