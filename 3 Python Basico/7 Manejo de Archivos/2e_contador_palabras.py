# Cree un programa que abra un archivo de texto y cuente cuántas palabras contiene en total.
# (Considere que las palabras están separadas por espacios y/o saltos de línea)

def open_file_and_count(path):
    with open(path, 'r', encoding='utf-8') as file:
        words = file.read()
        split_text = words.split()
        count_words = len(split_text)
        print(f'Este archivo contiene {count_words} palabras')


open_file_and_count('2e_texto_a_contar.txt')