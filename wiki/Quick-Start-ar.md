# 🇸🇦 NUASM - دليل البدء السريع

**مرحبًا بك في NUASM - أول مجمع متعدد اللغات في العالم**

---

## 📦 التثبيت

```bash
git clone https://github.com/cyberenigma-lgtm/Neuro-OS-Genesis
cd Neuro-OS-Genesis/Neuro-Universal-ASM
```

لا حاجة لتبعيات خارجية.

---

## 🚀 برنامجك الأول

### الخطوة 1: إنشاء ملف
أنشئ ملفًا باسم `marhaba.asm`:

```asm
; برنامجي الأول بالعربية
daa rax, 42
daa rbx, 10
jamaa rax, rbx
rjaa
```

### الخطوة 2: الترجمة
```bash
python src/unasm.py marhaba.asm -l ar -o marhaba.bin
```

### الخطوة 3: تم!
تمت ترجمة برنامجك إلى كود آلة x86-64.

---

## 📝 التعليمات الأساسية بالعربية

| التعليمة | المعنى | مثال |
|----------|--------|------|
| `daa` | نقل قيمة | `daa rax, 5` |
| `jamaa` | جمع | `jamaa rax, 10` |
| `taqsim` | طرح | `taqsim rbx, 3` |
| `qafz` | قفز | `qafz label` |
| `rjaa` | رجوع | `rjaa` |

---

## 🎯 أمثلة

### مثال 1: جمع بسيط
```asm
daa rax, 5
daa rbx, 3
jamaa rax, rbx
rjaa
```

### مثال 2: حلقة
```asm
daa counter, 5
loop_start:
    taqsim counter, 1
    qafz_ida_laysa_sifr loop_start
rjaa
```

---

## 🔧 خيارات الترجمة

```bash
# ترجمة إلى ثنائي
python src/unasm.py program.asm -l ar -o program.bin

# ترجمة إلى ELF64
python src/unasm.py program.asm -l ar -f elf64 -o program.elf
```

---

## 🆘 المساعدة

هل لديك مشاكل؟ تحقق من:
- [استكشاف الأخطاء](Troubleshooting-ar)
- [أمثلة كاملة](Examples-ar)

---

**برمجة سعيدة بالعربية!** 🎉
