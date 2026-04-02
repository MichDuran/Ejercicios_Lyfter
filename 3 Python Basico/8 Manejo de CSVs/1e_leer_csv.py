# Cree un programa que abra un archivo .csv con la información de videojuegos 
# (el que fue generado en el ejercicio 1) y:
# Lea cada línea usando csv.reader()
# Muestre el contenido en pantalla de forma legible, línea por línea
# Ejemplo:
# Nombre: Grand Theft Auto IV
# Género: Accion
# Desarrollador: Rockstar Games
# Clasificación: M

import csv


def read_csv_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file) 
        for row in reader:
            print(f'Nombre: {row['name']}')
            print(f'Género: {row['genre']}')
            print(f'Desarrollador: {row['developer']}')
            print(f'Clasificación ESRB: {row['esrb_rating']}')
            print('---')
            
            
read_csv_file('videojuegos_1.csv')
