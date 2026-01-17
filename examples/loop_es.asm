; Universal NASM Loop Test (Spanish)

pon rcx, 10       ; Contador = 10 (0x0A)
inicio:           ; Etiqueta
    resta rcx, 1  ; Decrementar
    si_no_cero inicio  ; Salt si no es cero (JNZ / JNE)

enseña            ; Syscall final
