# Cree un programa que:
# Lea un archivo línea por línea
# Convierta cada línea a mayúsculas
# Escriba el contenido en un nuevo archivo.

def open_and_save_upper_text(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        upper_list = [item.upper() for item in lines]

    with open('TEXTO_EN_MAYUSCULAS.txt', 'w', encoding='utf-8') as file:
        file.writelines(upper_list)


open_and_save_upper_text('3e_texto_a_mayusculas.txt')
