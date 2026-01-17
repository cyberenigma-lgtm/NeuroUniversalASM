# Language Packs

## 🌍 All 51 Supported Languages

NUASM supports **51 language packs** including dialects and regional variations.

---

## 📊 Complete Language List

| Code | Language | Native Name | Status |
|------|----------|-------------|--------|
| `ar` | Arabic | العربية | ✅ |
| `ar_eg` | Egyptian Arabic | العربية المصرية | ✅ |
| `de` | German | Deutsch | ✅ |
| `de_at` | Austrian German | Österreichisches Deutsch | ✅ |
| `de_bay` | Bavarian | Bairisch | ✅ |
| `de_sw` | Swabian | Schwäbisch | ✅ |
| `el` | Greek | Ελληνικά | ✅ |
| `en` | English | English | ✅ |
| `en_aus` | Australian English | Australian English | ✅ |
| `en_cockney` | Cockney | Cockney | ✅ |
| `en_ie` | Irish English | Irish English | ✅ |
| `en_scots` | Scots English | Scots | ✅ |
| `en_tx` | Texas English | Texan | ✅ |
| `es` | Spanish | Español | ✅ |
| `es_and` | Andalusian | Andaluz | ✅ |
| `es_ast` | Asturian | Asturianu | ✅ |
| `es_gad` | Gaditan | Gaditano | ✅ |
| `es_mad` | Madrid Spanish | Madrileño | ✅ |
| `es_sev` | Sevillian | Sevillano | ✅ |
| `es_val` | Valencian | Valencià | ✅ |
| `fa` | Persian | فارسی | ✅ |
| `fr` | French | Français | ✅ |
| `fr_qc` | Quebec French | Français Québécois | ✅ |
| `he` | Hebrew | עברית | ✅ |
| `hi` | Hindi | हिन्दी | ✅ |
| `id` | Indonesian | Bahasa Indonesia | ✅ |
| `it` | Italian | Italiano | ✅ |
| `it_nap` | Neapolitan | Napulitano | ✅ |
| `it_rom` | Roman | Romanesco | ✅ |
| `it_sic` | Sicilian | Sicilianu | ✅ |
| `ja` | Japanese | 日本語 | ✅ |
| `ja_kan` | Kansai Japanese | 関西弁 | ✅ |
| `ko` | Korean | 한국어 | ✅ |
| `ms` | Malay | Bahasa Melayu | ✅ |
| `nl` | Dutch | Nederlands | ✅ |
| `nl_be` | Belgian Dutch | Vlaams | ✅ |
| `pl` | Polish | Polski | ✅ |
| `pl_sil` | Silesian | Ślōnski | ✅ |
| `pt` | Portuguese | Português | ✅ |
| `pt_br` | Brazilian Portuguese | Português Brasileiro | ✅ |
| `ro` | Romanian | Română | ✅ |
| `ru` | Russian | Русский | ✅ |
| `sv` | Swedish | Svenska | ✅ |
| `sw` | Swahili | Kiswahili | ✅ |
| `th` | Thai | ไทย | ✅ |
| `tl` | Tagalog | Tagalog | ✅ |
| `tr` | Turkish | Türkçe | ✅ |
| `uk` | Ukrainian | Українська | ✅ |
| `vi` | Vietnamese | Tiếng Việt | ✅ |
| `zh` | Chinese | 中文 | ✅ |
| `zh_yue` | Cantonese | 粵語 | ✅ |

---

## 🔍 How to Use

```bash
# Specify language with -l flag
python src/unasm.py program.asm -l es    # Spanish
python src/unasm.py program.asm -l hi    # Hindi
python src/unasm.py program.asm -l ja    # Japanese
```

---

## 📝 Language Pack Structure

Each language pack (`languages/xx.json`) contains:
- Instruction mnemonics
- Comment syntax
- Error messages (localized)

---

## 🌐 Quick Start by Language

- [Spanish Guide](Quick-Start-es)
- [English Guide](Quick-Start-en)
- [Hindi Guide](Quick-Start-hi)
- [Arabic Guide](Quick-Start-ar)
- [Japanese Guide](Quick-Start-ja)
