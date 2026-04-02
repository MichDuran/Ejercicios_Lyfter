# Cree un programa con un numero secreto del 1 al 10. 
# El programa no debe cerrarse hasta que el usuario adivine el numero.
# Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.

import random
secret_number = random.randint(1, 10)
guessed = False
while not guessed:
    attempt = int(input("Adivina el número secreto (entre 1 y 10): "))
    if attempt == secret_number:
        print(f"¡Felicidades! Has adivinado el número secreto: {secret_number}")
        guessed = True
    else:
        print("Inténtalo de nuevo.")
