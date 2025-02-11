nota = int(input("  Que nota te sacaste?"))
desaprobado = nota < 6
aprobado = nota >= 6 and nota < 8
excelente = nota >= 8
if nota > 10:
    print("Nota invalida")
elif desaprobado:
    print("Desaprobaste")
elif aprobado:
    print("Aprobaste")
else:
    print("Excelente")
