# Cree un programa que abra un archivo .json con la información de Pokemón 
# (en base al JSON que fue generado en el ejercicio 1) y:
# Lea el archivo JSON
# Agrupe los Pokemón por tipo (por ejemplo, "agua", "fuego", etc.)
# Calcule y muestre el promedio de nivel para cada tipo:
# Tipo: Agua → Promedio de nivel: 42.6
# Tipo: Fuego → Promedio de nivel: 37.2
# Tipo: Planta → Promedio de nivel: 30.4


import json


def level_avg_by_type():
    with open("pokemones.json", "r") as file:
        pokemons = json.load(file)
        
        type_list = {}
        for pokemon in pokemons:
            for pok_type in pokemon["type"]:
                if pok_type not in type_list:
                    type_list[pok_type] = [pokemon["level"]]
                else:
                    type_list[pok_type].append(pokemon["level"])
        
        print("Promedio de nivel por tipo:")
        for pok_type, levels in type_list.items():
            average_level = sum(levels) / len(levels)
            print(f"Tipo: {pok_type} --> Promedio de nivel: {average_level}")


if __name__ == "__main__":
    level_avg_by_type()
