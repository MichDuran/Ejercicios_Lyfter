# Cree un programa que lea nombres de canciones de un archivo (línea por línea) 
# y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

def open_and_save_songs_per_line(path):
    with open(path,'r', encoding = 'utf-8') as file:
        lines = file.readlines()
        sorted_lines = sorted(lines)
        print(sorted_lines)

    with open('canciones_ordenadas.txt', 'w', encoding = 'utf-8') as file:
        file.writelines(sorted_lines)


open_and_save_songs_per_line('canciones.txt')
