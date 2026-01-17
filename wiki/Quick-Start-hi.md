# 🇮🇳 NUASM - त्वरित प्रारंभ गाइड

**NUASM में आपका स्वागत है - दुनिया का पहला बहु-भाषा असेंबलर**

---

## 📦 स्थापना

```bash
git clone https://github.com/cyberenigma-lgtm/Neuro-OS-Genesis
cd Neuro-OS-Genesis/Neuro-Universal-ASM
```

कोई बाहरी निर्भरता की आवश्यकता नहीं है।

---

## 🚀 आपका पहला प्रोग्राम

### चरण 1: फ़ाइल बनाएं
`namaste.asm` नामक फ़ाइल बनाएं:

```asm
; हिंदी में मेरा पहला प्रोग्राम
rakho rax, 42
rakho rbx, 10
jodo rax, rbx
wapas
```

### चरण 2: संकलित करें
```bash
python src/unasm.py namaste.asm -l hi -o namaste.bin
```

### चरण 3: हो गया!
आपका प्रोग्राम x86-64 मशीन कोड में संकलित हो गया है।

---

## 📝 हिंदी में मूल निर्देश

| निर्देश | अर्थ | उदाहरण |
|---------|------|--------|
| `rakho` | मान रखें | `rakho rax, 5` |
| `jodo` | जोड़ें | `jodo rax, 10` |
| `ghatao` | घटाएं | `ghatao rbx, 3` |
| `kudo` | कूदें | `kudo label` |
| `wapas` | वापस | `wapas` |

---

## 🎯 उदाहरण

### उदाहरण 1: सरल जोड़
```asm
rakho rax, 5
rakho rbx, 3
jodo rax, rbx
wapas
```

### उदाहरण 2: लूप
```asm
rakho counter, 5
loop_shuru:
    ghatao counter, 1
    kudo_yadi_na_shunya loop_shuru
wapas
```

---

## 🔧 संकलन विकल्प

```bash
# बाइनरी में संकलित करें
python src/unasm.py program.asm -l hi -o program.bin

# ELF64 में संकलित करें
python src/unasm.py program.asm -l hi -f elf64 -o program.elf
```

---

## 🆘 सहायता

समस्या है? देखें:
- [समस्या निवारण](Troubleshooting-hi)
- [पूर्ण उदाहरण](Examples-hi)

---

**हिंदी में कोडिंग का आनंद लें!** 🎉
