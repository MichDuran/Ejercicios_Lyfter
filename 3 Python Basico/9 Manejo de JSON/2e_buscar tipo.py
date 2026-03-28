# Cree un programa que abra un archivo .json con la información de Pokemón 
# (en base al JSON que fue generado en el ejercicio 1) y:
# Lea el archivo JSON de Pokemón
# Pida al usuario un tipo de Pokemón
# Muestre todos los Pokemón que sean de ese tipo
# Entrada:
# "Ingrese el tipo de pokemon desea buscar(agua,electrico,fuego,etc): "
# "Fuego"
# Salida:
# "Los pokemos que existen de ese tipo son: "
# Charmander
# Growlithe
# Victini

import json


def look_for_pokemon():
    with open('pokemones.json', 'r') as file:
        pokemons = json.load(file)

        pok_type = input('Ingrese un tipo de pokemon desea buscar (agua, electrico, fuego, etc): ')
        found_pokemons = []
        for pokemon in pokemons:
            if pok_type in pokemon["type"]:
                found_pokemons.append(pokemon["name"]["english"])

        if len(found_pokemons) > 0:
            print("Los pokemones que existen de ese tipo son:")
            for name in found_pokemons:
                print(name)
        else:
            print(f"No se encontraron pokemones del tipo {pok_type}.")

if __name__ == '__main__':
    look_for_pokemon()
