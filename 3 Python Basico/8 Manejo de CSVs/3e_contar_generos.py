# Cree un programa que abra un archivo .csv con la información de videojuegos 
# (en base al CSV que fue generado en el ejercicio 1) y:
# Lea el archivo .csv con videojuegos
# Cuente cuántos videojuegos hay de cada género
# Muestre el resultado de forma ordenada

import csv


def read_csv_file_and_count_genres(file_path):
    genre_count = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            genre = row['genre']
            
            if genre in genre_count:
                genre_count[genre] += 1
            else:
                genre_count[genre] = 1

    for genre, total in sorted(genre_count.items()):
        print(f'{genre}: {total}')


read_csv_file_and_count_genres('videojuegos_1.csv')
    