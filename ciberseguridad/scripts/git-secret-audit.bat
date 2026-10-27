@echo off
REM ============================================
REM git-secret-audit.bat - Auditoria de secretos en un repo git:
REM   [1] archivos sensibles en tracking   [2] .gitignore
REM   [3] gitleaks (working tree)          [4] historial de commits
REM   [5] archivos borrados del historial  [6] frontend (keys embebidas)
REM Ejecutar DENTRO del repositorio a auditar.
REM Salida: security\evidence\
REM ============================================
setlocal enabledelayedexpansion
set OUT=security\evidence
if not exist "%OUT%" mkdir "%OUT%"

echo ========================================
echo  GIT SECRET AUDIT - %CD%
echo ========================================

echo [1/6] Archivos sensibles en tracking...
git ls-files | findstr /i /r "\.env secret credential \.pem \.p12 \.pfx \.key" > "%OUT%\tracked-sensitive.txt" 2>nul
if %errorlevel% equ 0 (
    type "%OUT%\tracked-sensitive.txt"
) else (
    echo   (ninguno)
)

echo [2/6] .gitignore - entradas de secretos...
findstr /i "env secret key" .gitignore >nul 2>nul
if %errorlevel% equ 0 (
    echo   .gitignore contiene entradas de secretos
) else (
    echo   WARN: .gitignore sin entradas de secretos o inexistente
)

echo [3/6] gitleaks - working tree...
where gitleaks >nul 2>nul
if %errorlevel% equ 0 (
    gitleaks detect --source . --report-path "%OUT%\gitleaks.json" --report-format json
    echo   Reporte: %OUT%\gitleaks.json
) else (
    echo   gitleaks NO instalado - instalarlo: choco install gitleaks
    echo   (o usar: npx gitleaks detect --source .)
)

echo [4/6] Historial: commits con patrones de secretos (puede tardar)...
git log --all -p -G "api[_ -]?key|secret|password|token|BEGIN (RSA|EC|OPENSSH|PGP) PRIVATE" 2>nul ^
  | findstr /i "commit api_key api-key apikey secret password token BEGIN" > "%OUT%\git-log-secrets.txt"
if %errorlevel% equ 0 (
    echo   Posibles coincidencias - primeras lineas:
    powershell -NoProfile -Command "Get-Content '%OUT%\git-log-secrets.txt' -TotalCount 15"
    echo   (completo: %OUT%\git-log-secrets.txt)
) else (
    echo   (sin coincidencias)
)

echo [5/6] Archivos sensibles BORRADOS del historial (aun en git)...
git log --all --diff-filter=D --name-only --pretty=format:"%%h %%s" -- "*.env*" "*secret*" "*credential*" 2>nul > "%OUT%\deleted-sensitive.txt"
if %errorlevel% equ 0 (
    if exist "%OUT%\deleted-sensitive.txt" (
        for %%A in ("%OUT%\deleted-sensitive.txt") do if %%~zA gtr 0 (
            echo   Revisar: %OUT%\deleted-sensitive.txt
            type "%OUT%\deleted-sensitive.txt"
        ) else (
            echo   (nada)
        )
    )
) else (
    echo   (nada)
)

echo [6/6] Frontend: keys embebidas en codigo y bundles...
for /r . %%f in (*.js *.jsx *.ts *.tsx *.vue *.html *.json) do (
    findstr /i /c:"AIza" /c:"sk_live_" /c:"sk_test_" /c:"AKIA" /c:"ghp_" /c:"xoxb-" /c:"xoxp-" /c:"-----BEGIN" "%%f" >> "%OUT%\frontend-secrets.txt" 2>nul
)
if exist "%OUT%\frontend-secrets.txt" (
    for %%A in ("%OUT%\frontend-secrets.txt") do if %%~zA gtr 0 (
        echo   Posibles keys - triar falsos positivos:
        type "%OUT%\frontend-secrets.txt"
    ) else (
        echo   (ninguna encontrada)
    )
) else (
    echo   (ninguna encontrada)
)

echo ========================================
echo  COMPLETADO - Evidencia en %OUT%\
echo  RECORDATORIO: secreto expuesto = comprometido - ROTAR primero,
echo  luego limpiar historial (git filter-repo --invert-paths --path ^<archivo^> o BFG).
echo ========================================
endlocal
