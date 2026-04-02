# Cree un programa que lea un archivo con texto línea por línea, 
# quite los saltos de línea (\n) y escriba todo el contenido en un solo renglón en un nuevo archivo

def open_file_and_write(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        delete_n = [item.strip() for item in lines]
        separator = ' '
        str_complete = separator.join(delete_n)

    with open('1e_Texto_sin_saltos.txt', 'w', encoding='utf-8') as file:
        file.write(str_complete)
        print('Archivo creado')


open_file_and_write('1e_hola.txt')