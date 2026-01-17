# Installation Guide

## 📦 Installing NUASM

### Requirements
- Python 3.7 or higher
- Git (optional, for cloning)
- No external dependencies required

---

## 🚀 Installation Methods

### Method 1: Git Clone (Recommended)
```bash
git clone https://github.com/cyberenigma-lgtm/Neuro-OS-Genesis
cd Neuro-OS-Genesis/Neuro-Universal-ASM
```

### Method 2: Download ZIP
1. Go to [GitHub Repository](https://github.com/cyberenigma-lgtm/Neuro-OS-Genesis)
2. Click "Code" → "Download ZIP"
3. Extract to your desired location
4. Navigate to `Neuro-Universal-ASM` folder

---

## ✅ Verify Installation

```bash
# Check Python version
python --version

# Test NUASM
python src/unasm.py --help
```

You should see the help message if installation is successful.

---

## 🔧 First Compilation

```bash
# Compile an example
python src/unasm.py examples/test_es.asm -l es -o test.bin
```

---

## 🌍 Next Steps

- [Quick Start Guide](Quick-Start-en)
- [Language Packs](Language-Packs)
- [Examples](Examples-en)
