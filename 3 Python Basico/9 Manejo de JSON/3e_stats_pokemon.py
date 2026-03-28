# Cree un programa que abra un archivo .json con la información de Pokemón 
# (en base al JSON que fue generado en el ejercicio 1) y:
# Lea el archivo JSON de Pokemón
# Para cada Pokemón, muestre sus estadísticas principales (por ejemplo: ataque, defensa, velocidad, etc.)

import json


def stats_pokemon():
    with open('pokemones.json', 'r') as file:
        pokemons = json.load(file)
        for pokemon in pokemons:
            print(f'Nombre: {pokemon["name"]["english"]}')
            print(f'Ataque: {pokemon["base"]["Attack"]}')
            print(f'Defensa: {pokemon["base"]["Defense"]}')
            print(f'Velocidad: {pokemon["base"]["Speed"]}')
            print()

if __name__ == "__main__":
    stats_pokemon()
