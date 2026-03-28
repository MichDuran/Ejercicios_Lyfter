



import json


def level_avg_by_level():
    with open('pokemones.json', 'r') as file:
        pokemons = json.load(file)
        
        type_list ={}
        for pokemon in pokemons:
            for pokemon_type in pokemon["type"]:
                if pokemon_type not in type_list:
                    type_list[pokemon_type] = [pokemon["level"]]
                else:
                    type_list[pokemon_type].append(pokemon["level"])
        
        for pokemon_type, levels in type_list.items():
            average = sum(levels) / len(levels)
            print(pokemon_type, average)


if __name__ == '__main__':
    level_avg_by_level()
