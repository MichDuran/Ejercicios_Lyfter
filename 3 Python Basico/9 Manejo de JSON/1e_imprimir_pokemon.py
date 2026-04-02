# Cree un programa que abra un archivo .json con la información de Pokemón 
# (en base al JSON que fue generado en el ejercicio 1) y:
# Lea el archivo JSON de Pokemón
# Recorra la lista de Pokemón y muestre en consola su nombre, tipo y nivel (o cualquier otro atributo definido)

import json


def print_pokemon():
    with open("pokemones.json", "r") as file:
        pokemons = json.load(file)
        
        print("Lista de Pokemones:")
    for pokemon in pokemons:
        name = pokemon["name"]["english"]
        type_ = ", ".join(pokemon["type"])
        level = pokemon["level"]
        print(f"Nombre: {name} | Tipo: {type_} | Nivel: {level}")

if __name__ == "__main__":
    print_pokemon()
    