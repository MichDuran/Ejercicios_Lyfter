# Cree un programa que abra un archivo .csv con la información de videojuegos
# (en base al CSV que fue generado en el ejercicio 1) y:
# Lea el archivo .csv con videojuegos
# Pida al usuario ingresar el nombre de un desarrollador (ej. "Ubisoft")
# Muestre todos los videojuegos desarrollados por esa empresa en formato legible:

import csv


def read_csv_file_and_look_for(file_path, developer):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file) 
        for row in reader:
            if row['developer'] == developer:
                print(f'- {row["name"]} (Clasificación: {row["esrb_rating"]}, Género: {row["genre"]})')


developer = str(input('Ingrese el nombre de un desarrollador: '))
print(f'Videojuegos desarrollados por {developer}:')
read_csv_file_and_look_for('videojuegos_1.csv', developer)
