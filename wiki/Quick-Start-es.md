# 🇪🇸 NUASM - Guía de Inicio Rápido

**Bienvenido a NUASM - El primer ensamblador multi-idioma del mundo**

---

## 📦 Instalación

```bash
git clone https://github.com/cyberenigma-lgtm/Neuro-OS-Genesis
cd Neuro-OS-Genesis/Neuro-Universal-ASM
```

No se requieren dependencias externas.

---

## 🚀 Tu Primer Programa

### Paso 1: Crear archivo
Crea un archivo llamado `hola.asm`:

```asm
; Mi primer programa en español
pon rax, 42
pon rbx, 10
suma rax, rbx
ret
```

### Paso 2: Compilar
```bash
python src/unasm.py hola.asm -l es -o hola.bin
```

### Paso 3: ¡Listo!
Tu programa ha sido compilado a código máquina x86-64.

---

## 📝 Instrucciones Básicas en Español

| Instrucción | Significado | Ejemplo |
|-------------|-------------|---------|
| `pon` | Mover valor | `pon rax, 5` |
| `suma` | Sumar | `suma rax, 10` |
| `resta` | Restar | `resta rbx, 3` |
| `salta` | Saltar | `salta etiqueta` |
| `ret` | Retornar | `ret` |

---

## 🎯 Ejemplos

### Ejemplo 1: Suma Simple
```asm
pon rax, 5
pon rbx, 3
suma rax, rbx
ret
```

### Ejemplo 2: Bucle
```asm
pon rcx, 5
bucle:
    resta rcx, 1
    si_no_cero bucle
ret
```

### Ejemplo 3: Comparación
```asm
pon rax, 10
pon rbx, 10
comparar rax, rbx
si_igual son_iguales
; no son iguales
ret

son_iguales:
    pon rax, 1
    ret
```

---

## 🔧 Opciones de Compilación

```bash
# Compilar a binario
python src/unasm.py programa.asm -l es -o programa.bin

# Compilar a ELF64
python src/unasm.py programa.asm -l es -f elf64 -o programa.elf

# Compilar a PE64 (Windows)
python src/unasm.py programa.asm -l es -f pe64 -o programa.exe
```

---

## 🧸 Modo Niños

Para niños, usa palabras más simples:

```asm
pon numero, 5
suma numero, 3
enseña
```

---

## 🆘 Ayuda

¿Problemas? Consulta:
- [Solución de Problemas](Troubleshooting-es)
- [Ejemplos Completos](Examples-es)
- [Preguntas Frecuentes](FAQ-es)

---

## 📚 Siguiente Paso

- [Aprender más instrucciones](Instructions-es)
- [Ver ejemplos avanzados](Advanced-Examples-es)
- [Contribuir al proyecto](Contributing-es)

---

**¡Feliz programación en español!** 🎉
