# Cree un programa que me permita ingresar información de n cantidad de videojuegos y los guarde en un archivo csv.
# Debe incluir:
# Nombre
# Género
# Desarrollador
# Clasificación ESRB

import csv


games_list = []
def menu():
    print('Ingrese la información del videojuego:')
    name = input('Nombre: ')
    genre = input('Género: ')
    developer = input('Desarrollador: ')
    esrb_rating = input('Clasificación ESRB: ')
    videogame_headers = {
        'name': name,
        'genre': genre,
        'developer': developer,
        'esrb_rating': esrb_rating,
    }
    games_list.append(videogame_headers)
    
    
def write_csv_file(file_path, data):
    headers = (
        'name',
        'genre',
        'developer',
        'esrb_rating',
    )
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)
        
        
while True:    
    menu()
    write_csv_file('videojuegos_1.csv', games_list)
    option = input('Desea agregar otro videojuego? (s/n): ')
    if option != 's':
        print('Saliendo...')
        break
