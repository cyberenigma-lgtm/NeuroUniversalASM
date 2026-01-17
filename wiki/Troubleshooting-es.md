# 🇪🇸 Solución de Errores - NUASM

**Guía completa para resolver problemas en NUASM**

---

## 🚨 Errores Más Comunes

### Error 1: "Instrucción desconocida"

**Mensaje**:
```
Tokenizer Error: [Line 5] Instrucción desconocida: 'mover'
```

**Causa**: Usaste una palabra que no está en el paquete de idioma español.

**Solución**:
```asm
; ❌ Incorrecto
mover rax, 5

; ✅ Correcto
pon rax, 5
```

**Palabras correctas en español**:
- `pon` (no `mover`)
- `suma` (no `sumar`)
- `resta` (no `restar`)

---

### Error 2: "Operando inválido"

**Mensaje**:
```
Encoder Error: Operando inválido para 'pon'
```

**Causa**: Orden incorrecto de operandos.

**Solución**:
```asm
; ❌ Incorrecto
pon 5, rax       ; No puedes poner en un número

; ✅ Correcto
pon rax, 5       ; Destino primero, valor segundo
```

---

### Error 3: "Salto fuera de rango"

**Mensaje**:
```
Encoder Error: Jump out of range
```

**Causa**: La etiqueta está muy lejos (>127 bytes).

**Solución**:
```asm
; ❌ Problema
si_no_cero etiqueta_muy_lejana

; ✅ Solución 1: Usar salto incondicional
si_cero skip
salta etiqueta_lejana
skip:

; ✅ Solución 2: Reorganizar código
; Mover la etiqueta más cerca
```

---

### Error 4: "Etiqueta no definida"

**Mensaje**:
```
Encoder Error: Undefined label 'bucle'
```

**Causa**: Usaste una etiqueta que no existe.

**Solución**:
```asm
; ❌ Incorrecto
salta bucle      ; 'bucle' no existe

; ✅ Correcto
salta bucle

bucle:           ; Definir la etiqueta
    ret
```

---

### Error 5: "Archivo no encontrado"

**Mensaje**:
```
Error: File programa.asm not found
```

**Causa**: El archivo no existe o la ruta es incorrecta.

**Solución**:
```bash
# Verificar que el archivo existe
dir programa.asm

# Usar ruta completa
python src/unasm.py C:\ruta\completa\programa.asm -l es
```

---

## 🔍 Diagnóstico Paso a Paso

### Paso 1: Verificar Sintaxis
```asm
; Revisar cada línea
pon rax, 5       ; ✅ Correcto
suma rax 10      ; ❌ Falta coma
suma rax, 10     ; ✅ Correcto
```

### Paso 2: Verificar Etiquetas
```asm
; Todas las etiquetas usadas deben estar definidas
salta inicio     ; Usar etiqueta

inicio:          ; Definir etiqueta
    ret
```

### Paso 3: Verificar Idioma
```bash
# Asegúrate de usar el idioma correcto
python src/unasm.py programa.asm -l es  # Español
python src/unasm.py programa.asm -l en  # Inglés
```

---

## 🛠️ Herramientas de Depuración

### Mostrar Valores
```asm
pon rax, 10
enseña           ; Ver valor de RAX

suma rax, 5
enseña           ; Ver nuevo valor
```

### Comentarios de Depuración
```asm
pon rax, 5       ; DEBUG: RAX = 5
suma rax, 3      ; DEBUG: RAX = 8
enseña           ; DEBUG: Mostrar 8
```

### Compilación Verbosa
```bash
# Ver más detalles durante compilación
python src/unasm.py programa.asm -l es --verbose
```

---

## 📝 Checklist de Errores

Antes de pedir ayuda, verifica:

- [ ] ¿Usaste las palabras correctas en español?
- [ ] ¿El orden de operandos es correcto?
- [ ] ¿Todas las etiquetas están definidas?
- [ ] ¿El archivo existe en la ruta correcta?
- [ ] ¿Especificaste el idioma correcto (`-l es`)?
- [ ] ¿Hay comas donde deben estar?
- [ ] ¿Los registros son válidos (rax, rbx, rcx, rdx)?

---

## 🆘 Obtener Ayuda

### 1. Revisar Documentación
- [Guía de Inicio Rápido](Quick-Start-es)
- [Ejemplos](Examples-es)
- [Guía Paso a Paso](Step-by-Step-es)

### 2. Buscar en Issues
[GitHub Issues](https://github.com/cyberenigma-lgtm/Neuro-OS-Genesis/issues)

### 3. Crear Issue Nuevo
Incluye:
- Código que causa el error
- Mensaje de error completo
- Comando usado para compilar
- Versión de Python

---

## 💡 Consejos

1. **Empieza simple**: Prueba con programas pequeños
2. **Usa comentarios**: Explica qué hace cada línea
3. **Compila frecuentemente**: No escribas todo antes de compilar
4. **Lee los errores**: El mensaje te dice qué está mal
5. **Consulta ejemplos**: Compara con código que funciona

---

**¡No te rindas! Todos cometemos errores al aprender.** 💪
