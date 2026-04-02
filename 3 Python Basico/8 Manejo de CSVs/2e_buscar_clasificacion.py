# Cree un programa que abra un archivo .csv con la información de videojuegos 
# (en base al CSV que fue generado en el ejercicio 1) y:
# Lea el archivo CSV de videojuegos
# Pida al usuario una clasificación ESRB (por ejemplo: "T")
# Muestre todos los videojuegos que tengan esa clasificación.

import csv


def read_csv_file_and_look_for(file_path, esrb_rating):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file) 
        for row in reader:
            if row['esrb_rating'] == esrb_rating:
                print(f'Nombre: {row['name']}')
                print(f'Género: {row['genre']}')
                print(f'Desarrollador: {row['developer']}')
                print(f'Clasificación ESRB: {row['esrb_rating']}')
                print('---')


esrb_rating = str(input('Ingrese la clasificación ESRB que desea buscar: '))
read_csv_file_and_look_for('videojuegos_1.csv', esrb_rating)
