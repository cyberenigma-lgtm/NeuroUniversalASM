# NUASM — Neuro Universal Assembler
## Troubleshooting & Diagnostics Guide

> *"A multilingual assembler for humans, not machines."*

---

## 📖 About NUASM

NUASM es un ensamblador universal diseñado para permitir programación de bajo nivel en cualquier idioma humano.  
Forma parte del ecosistema Neuro‑OS Genesis y está construido para ser simple, accesible y extensible.  
Este documento cubre los errores más comunes y cómo resolverlos.

---

## 📑 Table of Contents

- [Quick Error Reference Table](#-quick-error-reference-table)
- [Common Errors & Solutions](#-common-errors--solutions)
- [Language Detection Issues](#4-language-detection-issues)
- [MultiLang-ASM Compatibility](#5-multilang-asm-compatibility)
- [How to Report Bugs](#-how-to-report-bugs)
- [Advanced Troubleshooting](#-advanced-troubleshooting)
- [MultiLang-ASM Migration Guide](#-multilang-asm-migration-guide)
- [Additional Resources](#-additional-resources)
- [Troubleshooting Checklist](#-troubleshooting-checklist)

---


## 📊 Quick Error Reference Table

| Error Code | Error Message | Severity | Quick Fix |
|------------|---------------|----------|-----------|
| `E001` | Instrucción desconocida | 🔴 Critical | Check language pack for valid mnemonics |
| `E002` | Operando inválido | 🟡 Warning | Verify operand syntax (register/immediate) |
| `E003` | Salto fuera de rango | 🔴 Critical | Use near jump or split into multiple jumps |
| `E004` | Etiqueta no definida | 🔴 Critical | Define label before using it |
| `E005` | Registro no válido | 🟡 Warning | Use valid x86-64 registers (rax, rbx, etc.) |
| `E006` | Tamaño de operando incorrecto | 🟠 Error | Match operand sizes (byte/word/dword/qword) |
| `E007` | Sintaxis incorrecta | 🟡 Warning | Check mnemonic syntax in language pack |
| `E008` | Archivo no encontrado | 🔴 Critical | Verify file path exists |
| `E009` | Idioma no soportado | 🟠 Error | Check `languages/` folder for language pack |
| `E010` | Formato de salida inválido | 🟡 Warning | Use `-f bin` (only supported format) |

---

## 🚨 Common Errors & Solutions

### 1. "Instrucción desconocida: 'xyz'"

**Cause**: You used a mnemonic not defined in the active language pack.

**Solutions**:
```bash
# 1. Check which language you're using
python src/unasm.py --help

# 2. View available mnemonics for your language
cat languages/es.json | grep "mov"

# 3. Use correct mnemonic
# ❌ Wrong: mover rax, 5
# ✅ Correct: pon rax, 5  (Spanish)
```

**Language-Specific Examples**:
| Language | MOV | ADD | SUB | JMP |
|----------|-----|-----|-----|-----|
| Spanish | `pon` | `suma` | `resta` | `salta` |
| Hindi | `rakho` | `jodo` | `ghatao` | `kudo` |
| English | `mov`/`put` | `add` | `sub`/`take` | `jump` |
| Arabic | `daa` | `jamaa` | `taqsim` | `qafz` |

---

### 2. "Jump out of range"

**Cause**: Short jump can only reach +/- 127 bytes.

**Solutions**:

**Option A: Use Near Jump** (Coming in v1.1)
```asm
; Future syntax
salta_cerca destino_lejano
```

**Option B: Split Jump** (Current workaround)
```asm
; Instead of:
si_no_cero destino_lejano  ; ❌ Too far

; Use:
si_cero skip_jump          ; ✅ Short jump
salta destino_lejano       ; Unconditional jump
skip_jump:
```

**Option C: Reorganize Code**
```asm
; Move target closer
bucle:
    ; ... code ...
    si_no_cero bucle  ; ✅ Now in range
```

---

### 3. "Operando inválido"

**Cause**: Incorrect operand type or syntax.

**Valid Operand Types**:
| Type | Example | Description |
|------|---------|-------------|
| Register | `rax`, `rbx`, `rcx` | 64-bit registers |
| Immediate | `5`, `0x10`, `42` | Numeric constants |
| Memory | `[rax]`, `[rbx+8]` | Memory addresses |
| Label | `bucle`, `inicio` | Code labels |

**Common Mistakes**:
```asm
; ❌ Wrong
pon 5, rax          ; Immediate as destination
suma rax, [rbx, 8]  ; Wrong memory syntax

; ✅ Correct
pon rax, 5          ; Register as destination
suma rax, [rbx+8]   ; Correct memory syntax
```

---

### 4. Language Detection Issues

**Problem**: NUASM doesn't auto-detect your language correctly.

**Solution**: Explicitly specify language
```bash
# Auto-detect (may fail)
python src/unasm.py mi_codigo.asm

# Explicit language (recommended)
python src/unasm.py mi_codigo.asm -l es
python src/unasm.py mera_code.asm -l hi
python src/unasm.py my_code.asm -l en
```

**Language Codes**:
```
es = Spanish       hi = Hindi         ar = Arabic
ja = Japanese      fr = French        de = German
ru = Russian       zh = Chinese       pt = Portuguese
it = Italian       ko = Korean        en = English
```

---

### 5. MultiLang-ASM Compatibility

**Problem**: Old `.masm` files don't compile in NUASM.

**Solutions**:

**Check 1: File Extension**
```bash
# NUASM accepts both
python src/unasm.py file.asm   # ✅
python src/unasm.py file.masm  # ✅
```

**Check 2: Vocabulary Differences**
```bash
# Compare vocabularies
diff languages/es.json ../MultiLang-ASM/languages/es.json
```

**Check 3: Syntax Changes**
```asm
; Old MultiLang-ASM syntax
mover rax, 5        ; Verbose form

; New NUASM syntax
pon rax, 5          ; Simplified form
```

---

## 🐛 How to Report Bugs

### Before Reporting

**1. Check if it's already known**
- Search [GitHub Issues](https://github.com/cyberenigma-lgtm/Neuro-OS-Genesis/issues)
- Check this troubleshooting guide
- Review `CHANGELOG.md`

**2. Gather Information**
```bash
# Get NUASM version
python src/unasm.py --version

# Get Python version
python --version

# Get OS info
# Windows: systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
# Linux: uname -a
```

**3. Create Minimal Reproduction**
```asm
; Reduce your code to smallest example that shows the bug
pon rax, 5
suma rax, 10  ; Bug happens here
```

### Bug Report Template

```markdown
## Bug Report

**NUASM Version**: [e.g., v1.0.0]
**Python Version**: [e.g., 3.10.5]
**OS**: [e.g., Windows 11, Ubuntu 22.04]
**Language**: [e.g., Spanish (es)]

### Description
[Clear description of the bug]

### Steps to Reproduce
1. Create file `test.asm` with:
   ```asm
   [your minimal code]
   ```
2. Run: `python src/unasm.py test.asm -l es`
3. See error

### Expected Behavior
[What should happen]

### Actual Behavior
[What actually happens]

### Error Output
```
[Paste full error message]
```

### Additional Context
[Any other relevant information]
```

### Where to Report

**GitHub Issues**: [Neuro-OS-Genesis/issues](https://github.com/cyberenigma-lgtm/Neuro-OS-Genesis/issues)

**Email**: neuro-os-team@example.com

**Discord**: [Neuro-OS Community](#)

---

## 🔬 Advanced Troubleshooting

### Debugging NUASM Itself

**Enable Verbose Mode**:
```bash
python src/unasm.py test.asm -l es --verbose
```

**Check Lexer Output**:
```python
# Add to src/lexer.py
print(f"Token: {token.type} = {token.value}")
```

**Check Parser Output**:
```python
# Add to src/parser.py
print(f"Instruction: {instruction}")
```

**Check Code Generation**:
```python
# Add to src/codegen.py
print(f"Opcode: {opcode:02x}")
```

### Language Pack Issues

**Validate JSON Syntax**:
```bash
# Windows
python -m json.tool languages/es.json

# Linux
jq . languages/es.json
```

**Check for Missing Mnemonics**:
```python
# Create check_language.py
import json

with open('languages/es.json') as f:
    lang = json.load(f)

required = ['mov', 'add', 'sub', 'jmp', 'ret']
for mnemonic in required:
    if mnemonic not in lang:
        print(f"Missing: {mnemonic}")
```

### Performance Issues

**Problem**: Compilation is slow

**Solutions**:
```bash
# 1. Check file size
ls -lh mi_codigo.asm

# 2. Profile compilation
python -m cProfile src/unasm.py test.asm

# 3. Reduce complexity
# - Split large files
# - Remove unused labels
# - Simplify macros
```

### Memory Issues

**Problem**: Out of memory errors

**Solutions**:
```bash
# 1. Check available memory
# Windows: systeminfo | findstr "Available Physical Memory"
# Linux: free -h

# 2. Increase Python memory limit
python -X dev src/unasm.py test.asm

# 3. Process in chunks
# Split large .asm files into smaller modules
```

---

## 🔄 MultiLang-ASM Migration Guide

### Differences Between MultiLang-ASM and NUASM

| Feature | MultiLang-ASM | NUASM |
|---------|---------------|-------|
| Transpilation | Yes (to English) | No (direct to machine code) |
| Dependencies | Requires `nasm.exe` | Pure Python, no deps |
| Error Messages | English only | Localized |
| Performance | Slower (2-step) | Faster (1-step) |
| Language Packs | 24 languages | 27+ languages |

### Migration Steps

**1. Update File Extension** (Optional)
```bash
# Both work, but .asm is recommended
mv mi_codigo.masm mi_codigo.asm
```

**2. Update Mnemonics** (If needed)
```bash
# Check for deprecated mnemonics
grep -n "mover" mi_codigo.asm  # Old
# Replace with:
# pon  # New
```

**3. Test Compilation**
```bash
# Old way (MultiLang-ASM)
python mlasm.py mi_codigo.masm -l es
nasm -f bin output.asm -o output.bin

# New way (NUASM)
python src/unasm.py mi_codigo.asm -l es -o output.bin
```

**4. Verify Output**
```bash
# Compare binaries
diff output_old.bin output_new.bin

# Or use hex dump
xxd output_old.bin > old.hex
xxd output_new.bin > new.hex
diff old.hex new.hex
```

---

## 📚 Additional Resources

### Documentation
- [README.md](README.md) - Main documentation
- [Language Pack Format](docs/language_pack.md)
- [Instruction Set](docs/instructions.md)

### Examples
- `examples/hola_mundo.asm` - Spanish Hello World
- `examples/namaste.asm` - Hindi example
- `examples/kids_mode.asm` - Simplified syntax

### Community
- GitHub Discussions
- Discord Server
- Stack Overflow tag: `nuasm`

---

## ✅ Troubleshooting Checklist

Before asking for help, verify:

- [ ] Using latest NUASM version
- [ ] Correct language code specified (`-l es`)
- [ ] Valid mnemonics for your language
- [ ] Proper operand syntax
- [ ] Labels defined before use
- [ ] File path exists and is readable
- [ ] Python 3.7+ installed
- [ ] No syntax errors in .asm file
- [ ] Language pack exists in `languages/`
- [ ] Tried with `--verbose` flag

---

**Last Updated**: 2026-01-17  
**NUASM Version**: 1.0.0  
**Maintainer**: Neuro-OS Team
