nota = int(input("¿Qué nota te sacaste? "))

# Validamos que la nota esté entre 0 y 10
if 0 <= nota <= 10:
    if nota < 4:  # Nota menor a 4
        nota += 2
        print("A recuperatorio")
    elif nota < 7:  # Nota entre 4 y 6
        nota += 1
        print("A final")
    else:  # Nota 7 o más
        print("Aprobado")
    
    # Imprimimos la nota final
    print("Tu nota es:", nota)
else:
    print("Nota inválida. Por favor, ingresá una nota entre 0 y 10.")