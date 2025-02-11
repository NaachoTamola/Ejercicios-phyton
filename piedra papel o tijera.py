import random

opciones = ["piedra", "papel", "tijera"]
usuario = input("Elegí piedra, papel o tijera: ").lower()
computadora = random.choice(opciones)
print(f"La computadora eligió: {computadora}")

if usuario == computadora:
    print("Empate!")
elif (usuario == "piedra" and computadora == "tijera") or \
     (usuario == "papel" and computadora == "piedra") or \
     (usuario == "tijera" and computadora == "papel"):
    print("¡Ganaste!")
else:
    print("¡Perdiste, suerte la prox!")
