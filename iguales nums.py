import random
computadora = random.randint(1, 10)
numero = int(input("Adivina el número que estoy pensando"))
if numero == computadora:
        print("¡Felicidades! Adivinaste el número")
else:
    print("Número incorrecto")

# while True:b    pero agregando el break cuando termina el if,
#  para que no se quede en un loop infinito

 # numero = int(input("Adivina el número que estoy pensando (entre 1 y 10): "))