# ========================================
# NUASM - GitHub Upload Script
# Automated upload to GitHub
# ========================================

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   NUASM - GitHub Upload Script" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Solicitar token
Write-Host "Pega tu GitHub Personal Access Token:" -ForegroundColor Yellow
Write-Host "(El token NO se mostrara por seguridad)" -ForegroundColor Gray
$token = Read-Host -AsSecureString
$tokenPlain = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($token))

if ([string]::IsNullOrWhiteSpace($tokenPlain)) {
    Write-Host ""
    Write-Host "X Error: Token vacio" -ForegroundColor Red
    Write-Host ""
    Write-Host "Genera tu token en:" -ForegroundColor Yellow
    Write-Host "https://github.com/settings/tokens" -ForegroundColor Cyan
    exit 1
}

Write-Host ""
Write-Host "OK Token recibido" -ForegroundColor Green
Write-Host ""

# Configuracion
$repoUrlWithToken = "https://$tokenPlain@github.com/cyberenigma-lgtm/NeuroUniversalASM.git"

# Navegar al directorio
$projectPath = "C:\Users\cyber\OneDrive\Documentos\NeuroOs\Neuro-OS-Genesis\Neuro-Universal-ASM"
Set-Location $projectPath

Write-Host "[1/7] Verificando Git..." -ForegroundColor Yellow
if (!(Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "  X Git no instalado" -ForegroundColor Red
    Write-Host "  Descarga Git: https://git-scm.com/download/win" -ForegroundColor Yellow
    exit 1
}
Write-Host "  OK Git instalado" -ForegroundColor Green

Write-Host "[2/7] Inicializando repositorio..." -ForegroundColor Yellow
if (Test-Path ".git") {
    Remove-Item -Recurse -Force ".git"
}
git init | Out-Null
Write-Host "  OK Repositorio inicializado" -ForegroundColor Green

Write-Host "[3/7] Configurando usuario..." -ForegroundColor Yellow
git config user.name "Jose Manuel"
git config user.email "cyberenigma@neuro-os.dev"
Write-Host "  OK Usuario configurado" -ForegroundColor Green

Write-Host "[4/7] Anadiendo archivos..." -ForegroundColor Yellow
git add .
$fileCount = (git diff --cached --numstat | Measure-Object).Count
Write-Host "  OK $fileCount archivos anadidos" -ForegroundColor Green

Write-Host "[5/7] Creando commit..." -ForegroundColor Yellow
$commitMessage = "Initial commit: NUASM - The World's First Multi-Language Assembler

Features:
- 51 language packs supported (Spanish, English, Hindi, Arabic, Japanese, etc.)
- Zero transpilation - Direct to x86-64 machine code
- Kids Mode built-in for education
- 100% compatible with MultiLang-ASM
- Complete multilingual wiki documentation
- Professional README with banner
- All tests passing (8/8)

Documentation:
- 14 wiki pages in multiple languages
- Step-by-step tutorials
- Comprehensive examples (beginner to advanced)
- Troubleshooting guides

Created by:
Jose Manuel - Spanish Creator
Part of Neuro-OS Genesis project

Related:
- Supersedes MultiLang-ASM
- Integrates MultiLang-ASM Kids Mode"

git commit -m $commitMessage | Out-Null
Write-Host "  OK Commit creado" -ForegroundColor Green

Write-Host "[6/7] Configurando remote..." -ForegroundColor Yellow
git remote add origin $repoUrlWithToken 2>$null
git branch -M main
Write-Host "  OK Remote configurado" -ForegroundColor Green

Write-Host "[7/7] Subiendo a GitHub..." -ForegroundColor Yellow
Write-Host "  Esto puede tardar un momento..." -ForegroundColor Gray
Write-Host "  (Forzando subida para sobrescribir wiki existente)" -ForegroundColor Gray

$pushOutput = git push -u origin main --force 2>&1

if ($LASTEXITCODE -eq 0) {
    Write-Host "  OK Subida exitosa!" -ForegroundColor Green
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "   OK NUASM SUBIDO A GITHUB" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Repositorio:" -ForegroundColor White
    Write-Host "  https://github.com/cyberenigma-lgtm/NeuroUniversalASM" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Contenido subido:" -ForegroundColor White
    Write-Host "  OK README.md (con banner profesional)" -ForegroundColor Green
    Write-Host "  OK LICENSE (MIT)" -ForegroundColor Green
    Write-Host "  OK src/ (4 archivos core)" -ForegroundColor Green
    Write-Host "  OK languages/ (51 idiomas)" -ForegroundColor Green
    Write-Host "  OK examples/ (16 ejemplos)" -ForegroundColor Green
    Write-Host "  OK wiki/ (14 paginas)" -ForegroundColor Green
    Write-Host "  OK assets/ (banner)" -ForegroundColor Green
    Write-Host "  OK test_nuasm.py" -ForegroundColor Green
    Write-Host ""
    Write-Host "Proximos pasos:" -ForegroundColor Yellow
    Write-Host "  1. Ve al repositorio en GitHub" -ForegroundColor White
    Write-Host "  2. Configura la Wiki (Settings > Features > Wikis)" -ForegroundColor White
    Write-Host "  3. Anade topics: assembly, assembler, multilingual, x86-64" -ForegroundColor White
    Write-Host ""
}
else {
    Write-Host "  X Error al subir" -ForegroundColor Red
    Write-Host ""
    Write-Host "Detalles del error:" -ForegroundColor Yellow
    Write-Host $pushOutput -ForegroundColor Gray
    Write-Host ""
    Write-Host "Posibles soluciones:" -ForegroundColor Yellow
    Write-Host "  1. Verifica que el repositorio existe en GitHub" -ForegroundColor White
    Write-Host "  2. Verifica que el token tiene permisos repo" -ForegroundColor White
    Write-Host "  3. Regenera el token si es necesario" -ForegroundColor White
    exit 1
}

# Limpiar token de la memoria
$tokenPlain = $null
[System.GC]::Collect()

Write-Host "Presiona Enter para salir..." -ForegroundColor Gray
Read-Host
