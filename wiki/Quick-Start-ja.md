# 🇯🇵 NUASM - クイックスタートガイド

**NUASMへようこそ - 世界初の多言語アセンブラ**

---

## 📦 インストール

```bash
git clone https://github.com/cyberenigma-lgtm/Neuro-OS-Genesis
cd Neuro-OS-Genesis/Neuro-Universal-ASM
```

外部依存関係は不要です。

---

## 🚀 最初のプログラム

### ステップ1: ファイルを作成
`konnichiwa.asm`というファイルを作成:

```asm
; 日本語での最初のプログラム
irete rax, 42
irete rbx, 10
tasu rax, rbx
modoru
```

### ステップ2: コンパイル
```bash
python src/unasm.py konnichiwa.asm -l ja -o konnichiwa.bin
```

### ステップ3: 完了!
プログラムがx86-64マシンコードにコンパイルされました。

---

## 📝 日本語の基本命令

| 命令 | 意味 | 例 |
|------|------|-----|
| `irete` | 値を入れる | `irete rax, 5` |
| `tasu` | 足す | `tasu rax, 10` |
| `hiku` | 引く | `hiku rbx, 3` |
| `tobu` | 飛ぶ | `tobu label` |
| `modoru` | 戻る | `modoru` |

---

## 🎯 例

### 例1: 簡単な足し算
```asm
irete rax, 5
irete rbx, 3
tasu rax, rbx
modoru
```

### 例2: ループ
```asm
irete counter, 5
loop_start:
    hiku counter, 1
    tobu_moshi_zero_denai loop_start
modoru
```

---

## 🔧 コンパイルオプション

```bash
# バイナリにコンパイル
python src/unasm.py program.asm -l ja -o program.bin

# ELF64にコンパイル
python src/unasm.py program.asm -l ja -f elf64 -o program.elf
```

---

## 🆘 ヘルプ

問題がありますか？確認してください:
- [トラブルシューティング](Troubleshooting-ja)
- [完全な例](Examples-ja)

---

**日本語でのコーディングを楽しんでください!** 🎉
