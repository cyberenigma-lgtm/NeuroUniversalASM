# 🇺🇸 NUASM - Quick Start Guide

**Welcome to NUASM - The world's first multi-language assembler**

---

## 📦 Installation

```bash
git clone https://github.com/cyberenigma-lgtm/Neuro-OS-Genesis
cd Neuro-OS-Genesis/Neuro-Universal-ASM
```

No external dependencies required.

---

## 🚀 Your First Program

### Step 1: Create File
Create a file called `hello.asm`:

```asm
; My first program in English
put rax, 42
put rbx, 10
add rax, rbx
return
```

### Step 2: Compile
```bash
python src/unasm.py hello.asm -l en -o hello.bin
```

### Step 3: Done!
Your program has been compiled to x86-64 machine code.

---

## 📝 Basic Instructions in English

| Instruction | Meaning | Example |
|-------------|---------|---------|
| `put` | Move value | `put rax, 5` |
| `add` | Add | `add rax, 10` |
| `take` | Subtract | `take rbx, 3` |
| `jump` | Jump | `jump label` |
| `return` | Return | `return` |

---

## 🎯 Examples

### Example 1: Simple Addition
```asm
put rax, 5
put rbx, 3
add rax, rbx
return
```

### Example 2: Loop
```asm
put counter, 5
loop_start:
    take counter, 1
    ; (continue loop)
```

### Example 3: Comparison
```asm
put rax, 10
put rbx, 10
; compare and jump
```

---

## 🔧 Compilation Options

```bash
# Compile to binary
python src/unasm.py program.asm -l en -o program.bin

# Compile to ELF64
python src/unasm.py program.asm -l en -f elf64 -o program.elf

# Compile to PE64 (Windows)
python src/unasm.py program.asm -l en -f pe64 -o program.exe
```

---

## 🧸 Kids Mode

For kids, use simpler words:

```asm
put number, 5
add number, 3
show
```

---

## 🆘 Help

Having issues? Check:
- [Troubleshooting](Troubleshooting-en)
- [Complete Examples](Examples-en)
- [FAQ](FAQ-en)

---

## 📚 Next Steps

- [Learn more instructions](Instructions-en)
- [See advanced examples](Advanced-Examples-en)
- [Contribute to the project](Contributing-en)

---

**Happy coding in English!** 🎉
