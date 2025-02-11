letra= str(input("Digite una letra: "))

if len(letra) == 1 and letra.isalpha():
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print("Es una vocal")
    else:
        print("Es una consonante")
else:
    print("Entrada inválida. Por favor, digite solo una letra.")