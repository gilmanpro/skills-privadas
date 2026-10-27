@echo off
REM ============================================
REM fingerprint-scan.bat — Detecta versiones de servidor/framework
REM Uso: fingerprint-scan.bat <url>
REM Ej:  fingerprint-scan.bat https://target.com
REM ============================================
setlocal
set URL=%1
if "%URL%"=="" (
    echo Uso: fingerprint-scan.bat ^<url^>
    exit /b 1
)

echo == HEADERS DE VERSION ==
curl -sI -L --max-time 10 "%URL%" | findstr /i "server: x-powered-by x-aspnet x-generator via x-runtime x-pingback"

echo.
echo == INDICADORES EN BODY ==
curl -sL --max-time 10 "%URL%" | findstr /i "wp-content generator joomla drupal laravel django flask express next nuxt react vue angular asp.net spring rails"

echo.
echo == ENDPOINTS DE VERSION ==
for %%p in (robots.txt CHANGELOG CHANGELOG.md README.md VERSION version.txt package.json composer.json wp-json administrator manager/html actuator swagger-ui.html openapi.json graphql info.php phpinfo.php) do (
    for /f %%c in ('curl -s -o nul -w "%%{http_code}" --max-time 10 "%URL%/%%p"') do echo   %%c /%%p
)
endlocal