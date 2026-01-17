# API Reference

## 🔧 NUASM Command Line Interface

### Basic Usage

```bash
python src/unasm.py <source> [options]
```

---

## 📝 Arguments

### Required Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `source` | Source assembly file | `program.asm` |

### Optional Arguments

| Flag | Description | Default | Example |
|------|-------------|---------|---------|
| `-o, --output` | Output file path | `output.bin` | `-o program.bin` |
| `-l, --lang` | Language code | `es` | `-l en` |
| `-f, --format` | Output format | `bin` | `-f elf64` |
| `--verbose` | Verbose output | `False` | `--verbose` |
| `--help` | Show help | - | `--help` |
| `--version` | Show version | - | `--version` |

---

## 🎯 Examples

### Compile to Binary
```bash
python src/unasm.py program.asm -l es -o program.bin
```

### Compile to ELF64
```bash
python src/unasm.py program.asm -l en -f elf64 -o program.elf
```

### Compile to PE64
```bash
python src/unasm.py program.asm -l es -f pe64 -o program.exe
```

### Verbose Mode
```bash
python src/unasm.py program.asm -l es --verbose
```

---

## 📊 Output Formats

| Format | Extension | Platform | Description |
|--------|-----------|----------|-------------|
| `bin` | `.bin` | All | Raw binary |
| `elf64` | `.elf` | Linux | ELF executable |
| `pe64` | `.exe` | Windows | PE executable |

---

## 🌍 Language Codes

See [Language Packs](Language-Packs) for complete list.

Common codes:
- `es` - Spanish
- `en` - English
- `hi` - Hindi
- `ar` - Arabic
- `ja` - Japanese
- `fr` - French
- `de` - German
- `ru` - Russian
- `zh` - Chinese

---

## 🔍 Exit Codes

| Code | Meaning |
|------|---------|
| `0` | Success |
| `1` | Compilation error |
| `2` | File not found |
| `3` | Invalid arguments |

---

## 📚 See Also

- [Quick Start](Quick-Start-en)
- [Examples](Examples-en)
- [Troubleshooting](Troubleshooting-en)
