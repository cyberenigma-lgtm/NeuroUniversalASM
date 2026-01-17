# Contributing to NUASM

## 🤝 How to Contribute

We welcome contributions to NUASM! Here's how you can help:

---

## 🌍 Add a New Language

### Step 1: Create Language Pack

Create `languages/your_lang.json`:

```json
{
    "meta": {
        "code": "xx",
        "name": "Your Language",
        "version": "1.0"
    },
    "instructions": {
        "mov": ["your_word_for_move"],
        "add": ["your_word_for_add"],
        "sub": ["your_word_for_subtract"],
        "ret": ["your_word_for_return"]
    },
    "comments": {
        "prefix": ";"
    },
    "errors": {
        "ERR_UNKNOWN_OPCODE": "Translated error message"
    }
}
```

### Step 2: Add Examples

Create `examples/hello_xx.asm` with example code in your language.

### Step 3: Submit Pull Request

1. Fork the repository
2. Create a branch: `git checkout -b add-language-xx`
3. Commit your changes
4. Push and create Pull Request

---

## 🐛 Report Bugs

1. Check [existing issues](https://github.com/cyberenigma-lgtm/Neuro-OS-Genesis/issues)
2. Create new issue with:
   - Clear description
   - Steps to reproduce
   - Expected vs actual behavior
   - NUASM version
   - Python version

---

## 📝 Improve Documentation

- Fix typos
- Add examples
- Translate documentation
- Improve clarity

---

## 💻 Code Contributions

### Areas to Contribute

- New output formats
- Optimization improvements
- Better error messages
- Additional instruction support
- Testing improvements

### Code Style

- Follow PEP 8
- Add docstrings
- Include tests
- Update documentation

---

## 🧪 Testing

Run tests before submitting:

```bash
python test_nuasm.py
```

All tests must pass.

---

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

## 🙏 Thank You!

Every contribution helps make NUASM better for everyone!
