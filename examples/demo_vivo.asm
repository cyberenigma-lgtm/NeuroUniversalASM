; 🌟 DEMOSTRACIÓN EN VIVO: Universal NASM
; Lenguaje: Español (Nativo)
; Objetivo: Un bucle simple que cuenta de 5 a 0 y sale.

global _inicio

_inicio:
    pon rax, 5              ; Cargar 5 en el acumulador
    pon rcx, 0              ; Inicializar contador

bucle:
    sumar rcx, 1            ; Incrementar contador
    restar rax, 1           ; Decrementar acumulador
    
    comparar rax, 0         ; ¿Es cero? (cmp fake, en realidad sub sin guardar)
                            ; Nota: CMP no está implementado en v1.0, usamos resta/test o flags implícitos
                            ; Por ahora, RESTAR ya actualiza flags.

    si_no_cero bucle        ; Si no es cero, volver a 'bucle'

terminar:
    pon rax, 60             ; Syscall ID: sys_exit
    pon rdi, 0              ; Status: 0
    enseña                  ; Ejecutar syscall
