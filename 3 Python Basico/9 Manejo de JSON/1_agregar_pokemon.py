# Cree un programa que permita agregar un pokemon nuevo al archivo de la lección de JSON
# Debe leer el archivo para importar los pokemones existentes.
# Luego debe pedir la información del pokemon a agregar.
# Finalmente debe guardar el nuevo pokemon en el archivo.
# Se agrega este comentario para validación en GitHub

import json


def add_pokemon():
    with open("pokemones.json", "r") as file:
        pokemons = json.load(file)

    print("Ingrese la información básica de su Pokemón.")
    new_pokemon = {
        "name": {
            "english": input("Ingrese el nombre: ")
        },
        "level": int(input("Ingrese el nivel: ")),
        "type": [input("Ingrese el tipo: ")],
        "base": {
            "HP": int(input("Ingrese los puntos de salud: ")),
            "Attack": int(input("Ingrese el nivel de ataque: ")),
            "Defense": int(input("Ingrese el nivel de defensa: ")),
            "Sp. Attack": int(input("Ingrese el nivel de ataque especial: ")),
            "Sp. Defense": int(input("Ingrese el nivel de defensa especial: ")),
            "Speed": int(input("Ingrese la velocidad: "))
        }
    }

    pokemons.append(new_pokemon)

    with open("pokemones.json", "w") as file:
        json.dump(pokemons, file, indent=4)

    print(f'Pokemón {new_pokemon["name"]["english"]} agregado exitosamente.')

    
if __name__ == "__main__":
    add_pokemon()
