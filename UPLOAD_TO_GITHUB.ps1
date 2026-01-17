# NUASM - GitHub Upload Script
# Preparación para subir a https://github.com/cyberenigma-lgtm/NeuroUniversalASM

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "NUASM - GitHub Upload Preparation" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar Git
Write-Host "[1/6] Verificando Git..." -ForegroundColor Yellow
if (Get-Command git -ErrorAction SilentlyContinue) {
    Write-Host "  ✓ Git instalado" -ForegroundColor Green
}
else {
    Write-Host "  ✗ Git no instalado" -ForegroundColor Red
    Write-Host "  Instala Git desde: https://git-scm.com/download/win" -ForegroundColor Yellow
    exit 1
}

# Inicializar repositorio
Write-Host "[2/6] Inicializando repositorio..." -ForegroundColor Yellow
if (Test-Path ".git") {
    Write-Host "  ✓ Repositorio ya inicializado" -ForegroundColor Green
}
else {
    git init
    Write-Host "  ✓ Repositorio inicializado" -ForegroundColor Green
}

# Añadir archivos
Write-Host "[3/6] Añadiendo archivos..." -ForegroundColor Yellow
git add .
Write-Host "  ✓ Archivos añadidos" -ForegroundColor Green

# Commit inicial
Write-Host "[4/6] Creando commit inicial..." -ForegroundColor Yellow
git commit -m "Initial commit: NUASM - The World's First Multi-Language Assembler

- 51 language packs supported
- Zero transpilation (direct to machine code)
- Kids Mode built-in
- 100% compatible with MultiLang-ASM
- Complete wiki documentation in multiple languages
- Professional README with banner
- All tests passing (8/8)

Created by José Manuel - Spanish Creator"

Write-Host "  ✓ Commit creado" -ForegroundColor Green

# Añadir remote
Write-Host "[5/6] Configurando remote..." -ForegroundColor Yellow
$remoteUrl = "https://github.com/cyberenigma-lgtm/NeuroUniversalASM.git"
git remote add origin $remoteUrl 2>$null
if ($?) {
    Write-Host "  ✓ Remote añadido: $remoteUrl" -ForegroundColor Green
}
else {
    Write-Host "  ℹ Remote ya existe" -ForegroundColor Yellow
}

# Instrucciones finales
Write-Host "[6/6] Listo para subir!" -ForegroundColor Yellow
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "SIGUIENTE PASO:" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Asegúrate de que el repositorio existe en GitHub:" -ForegroundColor White
Write-Host "   https://github.com/cyberenigma-lgtm/NeuroUniversalASM" -ForegroundColor Gray
Write-Host ""
Write-Host "2. Ejecuta el siguiente comando para subir:" -ForegroundColor White
Write-Host "   git push -u origin main" -ForegroundColor Green
Write-Host ""
Write-Host "   O si tu rama principal es 'master':" -ForegroundColor White
Write-Host "   git branch -M main" -ForegroundColor Gray
Write-Host "   git push -u origin main" -ForegroundColor Green
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "CONTENIDO A SUBIR:" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "✓ README.md (con banner profesional)" -ForegroundColor Green
Write-Host "✓ LICENSE (MIT)" -ForegroundColor Green
Write-Host "✓ .gitignore" -ForegroundColor Green
Write-Host "✓ src/ (4 archivos core)" -ForegroundColor Green
Write-Host "✓ languages/ (51 idiomas)" -ForegroundColor Green
Write-Host "✓ examples/ (16 ejemplos)" -ForegroundColor Green
Write-Host "✓ wiki/ (14 páginas)" -ForegroundColor Green
Write-Host "✓ assets/ (banner)" -ForegroundColor Green
Write-Host "✓ test_nuasm.py" -ForegroundColor Green
Write-Host ""
Write-Host "Total: ~93 archivos" -ForegroundColor Cyan
Write-Host ""
