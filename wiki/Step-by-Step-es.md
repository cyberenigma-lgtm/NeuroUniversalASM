# 🇪🇸 Guía Paso a Paso - NUASM

**Tutorial completo para aprender NUASM desde cero**

---

## 📚 Tabla de Contenidos

1. [Instalación](#-paso-1-instalación)
2. [Tu Primer Programa](#-paso-2-tu-primer-programa)
3. [Entender los Registros](#-paso-3-entender-los-registros)
4. [Operaciones Básicas](#-paso-4-operaciones-básicas)
5. [Bucles](#-paso-5-bucles)
6. [Funciones](#-paso-6-funciones)
7. [Depuración](#-paso-7-depuración)
8. [Proyectos Completos](#-paso-8-proyectos-completos)

---

## 🔧 Paso 1: Instalación

### 1.1 Descargar NUASM
```bash
git clone https://github.com/cyberenigma-lgtm/Neuro-OS-Genesis
cd Neuro-OS-Genesis/Neuro-Universal-ASM
```

### 1.2 Verificar Python
```bash
python --version
```
Necesitas Python 3.7 o superior.

### 1.3 Probar NUASM
```bash
python src/unasm.py --help
```

✅ Si ves el mensaje de ayuda, ¡está instalado!

---

## 👶 Paso 2: Tu Primer Programa

### 2.1 Crear el Archivo
Crea un archivo llamado `primero.asm`:

```asm
; Mi primer programa
pon rax, 42
ret
```

### 2.2 Compilar
```bash
python src/unasm.py primero.asm -l es -o primero.bin
```

### 2.3 Verificar
Deberías ver:
```
[1/3] Tokenizing using language 'es'...
[2/3] Two-Pass Assembly...
Generated XX bytes.
[3/3] Success! Saved to primero.bin
```

✅ ¡Felicidades! Has compilado tu primer programa.

---

## 🎯 Paso 3: Entender los Registros

### 3.1 ¿Qué son los Registros?
Los registros son como "cajas" donde guardas números.

### 3.2 Registros Principales
| Registro | Uso |
|----------|-----|
| `rax` | Acumulador (resultados) |
| `rbx` | Base |
| `rcx` | Contador (bucles) |
| `rdx` | Datos |

### 3.3 Ejemplo Práctico
```asm
pon rax, 10      ; RAX = 10
pon rbx, 5       ; RBX = 5
pon rcx, 3       ; RCX = 3
```

---

## ➕ Paso 4: Operaciones Básicas

### 4.1 Suma
```asm
pon rax, 5
pon rbx, 3
suma rax, rbx    ; RAX = RAX + RBX = 8
```

**Ejercicio**: Suma 15 + 27

<details>
<summary>Ver solución</summary>

```asm
pon rax, 15
pon rbx, 27
suma rax, rbx
ret
```
</details>

### 4.2 Resta
```asm
pon rax, 10
pon rbx, 4
resta rax, rbx   ; RAX = RAX - RBX = 6
```

**Ejercicio**: Resta 50 - 23

### 4.3 Multiplicación
```asm
pon rax, 6
pon rbx, 7
multiplicar rbx  ; RAX = RAX * RBX = 42
```

**Ejercicio**: Multiplica 8 × 9

---

## 🔄 Paso 5: Bucles

### 5.1 Bucle Simple
```asm
pon rcx, 5       ; Contador

bucle:
    ; Tu código aquí
    resta rcx, 1
    si_no_cero bucle
```

### 5.2 Ejemplo: Contar de 5 a 1
```asm
pon rcx, 5

contar:
    enseña           ; Mostrar RCX
    resta rcx, 1
    si_no_cero contar

ret
```

**Salida**: 5, 4, 3, 2, 1

### 5.3 Ejemplo: Sumar 1 a 10
```asm
pon rax, 0       ; Suma total
pon rcx, 10      ; Contador

sumar:
    suma rax, rcx
    resta rcx, 1
    si_no_cero sumar

enseña
ret
```

**Resultado**: 55

**Ejercicio**: Crear un bucle que cuente de 1 a 20

---

## 📞 Paso 6: Funciones

### 6.1 Crear una Función
```asm
; Función que suma dos números
sumar_dos:
    pon rax, rdi
    suma rax, rsi
    ret
```

### 6.2 Llamar la Función
```asm
pon rdi, 10      ; Primer parámetro
pon rsi, 20      ; Segundo parámetro
llamar sumar_dos
enseña
ret
```

### 6.3 Función Completa
```asm
global inicio

inicio:
    pon rdi, 15
    pon rsi, 27
    llamar sumar
    enseña
    ret

sumar:
    pon rax, rdi
    suma rax, rsi
    ret
```

**Ejercicio**: Crear una función que multiplique dos números

---

## 🐛 Paso 7: Depuración

### 7.1 Mostrar Valores
```asm
pon rax, 5
enseña           ; Ver: 5

suma rax, 3
enseña           ; Ver: 8
```

### 7.2 Comentarios Útiles
```asm
pon rax, 10      ; Inicializar a 10
suma rax, 5      ; Sumar 5 (ahora es 15)
enseña           ; Mostrar resultado
```

### 7.3 Errores Comunes

#### Error 1: Instrucción Desconocida
```asm
mover rax, 5     ; ❌ Error: usa 'pon'
```

**Solución**:
```asm
pon rax, 5       ; ✅ Correcto
```

#### Error 2: Etiqueta No Definida
```asm
salta bucle      ; ❌ Error: 'bucle' no existe
```

**Solución**:
```asm
bucle:           ; ✅ Definir etiqueta
    ret
```

---

## 🏆 Paso 8: Proyectos Completos

### Proyecto 1: Calculadora Simple
```asm
; Calculadora: suma, resta, multiplica
global inicio

inicio:
    ; Suma
    pon rdi, 10
    pon rsi, 5
    llamar sumar
    enseña

    ; Resta
    pon rdi, 10
    pon rsi, 5
    llamar restar
    enseña

    ; Multiplicación
    pon rdi, 10
    pon rsi, 5
    llamar multiplicar
    enseña

    ret

sumar:
    pon rax, rdi
    suma rax, rsi
    ret

restar:
    pon rax, rdi
    resta rax, rsi
    ret

multiplicar:
    pon rax, rdi
    pon rbx, rsi
    multiplicar rbx
    ret
```

### Proyecto 2: Contador Avanzado
```asm
; Contar de 1 a N con saltos
global inicio

inicio:
    pon rcx, 1       ; Inicio
    pon rdx, 20      ; Fin

contar:
    enseña
    suma rcx, 1
    comparar rcx, rdx
    si_menor_igual contar

    ret
```

### Proyecto 3: Fibonacci
```asm
; Generar secuencia Fibonacci
global inicio

inicio:
    pon rax, 0       ; F(0)
    pon rbx, 1       ; F(1)
    pon rcx, 10      ; Cantidad

fib:
    enseña
    pon rdx, rax
    pon rax, rbx
    suma rbx, rdx
    resta rcx, 1
    si_no_cero fib

    ret
```

---

## 📋 Checklist de Aprendizaje

### Nivel Principiante
- [ ] Instalar NUASM
- [ ] Compilar primer programa
- [ ] Usar registros básicos
- [ ] Hacer suma y resta
- [ ] Mostrar resultados

### Nivel Intermedio
- [ ] Crear bucles simples
- [ ] Usar comparaciones
- [ ] Crear funciones básicas
- [ ] Depurar programas

### Nivel Avanzado
- [ ] Funciones con parámetros
- [ ] Bucles anidados
- [ ] Proyectos completos
- [ ] Optimizar código

---

## 🎓 Próximos Pasos

1. **Practica**: Haz los ejercicios propuestos
2. **Experimenta**: Modifica los ejemplos
3. **Crea**: Haz tus propios programas
4. **Comparte**: Ayuda a otros a aprender

---

## 🔗 Recursos

- [Ejemplos Completos](Examples-es)
- [Solución de Problemas](Troubleshooting-es)
- [Referencia Rápida](Quick-Reference-es)

---

**¡Sigue practicando y llegarás lejos!** 🚀
