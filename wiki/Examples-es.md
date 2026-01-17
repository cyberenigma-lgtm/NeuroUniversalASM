# 🇪🇸 Ejemplos Completos - NUASM

**Ejemplos prácticos de NUASM en español para todos los niveles**

---

## 🎓 Nivel Principiante

### Ejemplo 1: Hola Mundo (Mostrar un número)
```asm
; Mostrar el número 42
pon rax, 42
enseña
ret
```

**Compilar**:
```bash
python src/unasm.py hola.asm -l es -o hola.bin
```

**Qué hace**: Pone el número 42 en el registro RAX y lo muestra.

---

### Ejemplo 2: Suma Simple
```asm
; Sumar 5 + 3
pon rax, 5
pon rbx, 3
suma rax, rbx
enseña
ret
```

**Resultado**: RAX = 8

---

### Ejemplo 3: Resta
```asm
; Restar 10 - 4
pon rax, 10
pon rbx, 4
resta rax, rbx
enseña
ret
```

**Resultado**: RAX = 6

---

## 🎯 Nivel Intermedio

### Ejemplo 4: Bucle Simple
```asm
; Contar de 5 a 1
pon rcx, 5

bucle:
    enseña
    resta rcx, 1
    si_no_cero bucle

ret
```

**Qué hace**: Muestra 5, 4, 3, 2, 1

---

### Ejemplo 5: Comparación
```asm
; Comparar dos números
pon rax, 10
pon rbx, 10
comparar rax, rbx
si_igual son_iguales

; No son iguales
pon rax, 0
ret

son_iguales:
    pon rax, 1
    ret
```

**Resultado**: RAX = 1 (son iguales)

---

### Ejemplo 6: Multiplicación
```asm
; Multiplicar 6 * 7
pon rax, 6
pon rbx, 7
multiplicar rbx
enseña
ret
```

**Resultado**: RAX = 42

---

## 🚀 Nivel Avanzado

### Ejemplo 7: Función con Parámetros
```asm
; Función que suma dos números
global inicio

inicio:
    pon rdi, 10      ; Primer parámetro
    pon rsi, 20      ; Segundo parámetro
    llamar sumar
    enseña
    ret

sumar:
    pon rax, rdi
    suma rax, rsi
    ret
```

---

### Ejemplo 8: Bucle con Acumulador
```asm
; Sumar números del 1 al 10
pon rax, 0       ; Acumulador
pon rcx, 10      ; Contador

bucle_suma:
    suma rax, rcx
    resta rcx, 1
    si_no_cero bucle_suma

enseña
ret
```

**Resultado**: RAX = 55 (1+2+3+4+5+6+7+8+9+10)

---

### Ejemplo 9: Factorial
```asm
; Calcular factorial de 5
pon rbx, 5       ; Número
pon rax, 1       ; Resultado

factorial:
    multiplicar rbx
    resta rbx, 1
    comparar rbx, 1
    si_mayor factorial

enseña
ret
```

**Resultado**: RAX = 120 (5! = 5×4×3×2×1)

---

### Ejemplo 10: Fibonacci
```asm
; Calcular 10 números de Fibonacci
pon rax, 0       ; F(0)
pon rbx, 1       ; F(1)
pon rcx, 10      ; Contador

fib_loop:
    enseña           ; Mostrar número actual
    pon rdx, rax
    pon rax, rbx
    suma rbx, rdx
    resta rcx, 1
    si_no_cero fib_loop

ret
```

**Resultado**: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

---

## 🔧 Ejemplos de Manejo de Memoria

### Ejemplo 11: Leer de Memoria
```asm
; Leer valor de memoria
pon rbx, direccion
pon rax, [rbx]
enseña
ret

direccion:
    db 42
```

---

### Ejemplo 12: Escribir en Memoria
```asm
; Escribir valor en memoria
pon rax, 100
pon rbx, buffer
pon [rbx], rax
ret

buffer:
    resb 8
```

---

## 🎨 Ejemplos con Pila

### Ejemplo 13: Usar la Pila
```asm
; Guardar y recuperar valores
pon rax, 42
meter rax        ; Push

pon rax, 0       ; Limpiar RAX

sacar rax        ; Pop
enseña
ret
```

---

### Ejemplo 14: Llamada a Función con Pila
```asm
; Pasar parámetros por pila
meter 10
meter 20
llamar sumar_pila
enseña
ret

sumar_pila:
    sacar rbx
    sacar rax
    suma rax, rbx
    ret
```

---

## 🐛 Ejemplos de Depuración

### Ejemplo 15: Mostrar Valores Intermedios
```asm
; Depurar paso a paso
pon rax, 5
enseña           ; Mostrar: 5

suma rax, 3
enseña           ; Mostrar: 8

multiplicar rax, 2
enseña           ; Mostrar: 16

ret
```

---

## 📝 Plantillas Útiles

### Plantilla Básica
```asm
; Programa básico
global inicio

inicio:
    ; Tu código aquí
    ret
```

### Plantilla con Función
```asm
; Programa con función
global inicio

inicio:
    llamar mi_funcion
    ret

mi_funcion:
    ; Tu código aquí
    ret
```

### Plantilla con Bucle
```asm
; Programa con bucle
global inicio

inicio:
    pon rcx, 10

bucle:
    ; Tu código aquí
    resta rcx, 1
    si_no_cero bucle
    
    ret
```

---

## 🎯 Ejercicios Propuestos

### Ejercicio 1 (Fácil)
Crear un programa que sume 15 + 27 y muestre el resultado.

### Ejercicio 2 (Medio)
Crear un bucle que cuente de 1 a 20.

### Ejercicio 3 (Difícil)
Crear una función que calcule el factorial de un número.

---

## 🔗 Recursos Adicionales

- [Guía de Inicio Rápido](Quick-Start-es)
- [Solución de Problemas](Troubleshooting-es)
- [Referencia de Instrucciones](Instructions-es)

---

**¡Practica y mejora tus habilidades!** 💪
