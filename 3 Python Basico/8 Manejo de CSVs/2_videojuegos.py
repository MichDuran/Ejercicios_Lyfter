# Lea sobre el resto de métodos del módulo csv y cree una version alternativa del ejercicio anterior
# que guarde el archivo separado por tabulaciones en vez de por comas.

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
        writer = csv.DictWriter(file, headers, delimiter='\t')
        writer.writeheader()
        writer.writerows(data)
        
        
while True:    
    menu()
    write_csv_file('videojuegos_2.csv', games_list)
    option = input('Desea agregar otro videojuego? (s/n): ')
    if option != 's':
        print('Saliendo...')
        break
