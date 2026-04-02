# Cree un programa que:
# Pida al usuario una línea de texto
# Agregue esa línea al final de un archivo existente
# Si el archivo no existe, lo crea automáticamente.
# Entrada: "Este es un nuevo registro"
# Salida: "El texto se agrega al final del archivo sin borrar lo anterior"

def add_lines(path):
    user_text = str(input('Ingrese su texto: '))
    with open(path, 'a', encoding='utf-8') as file:
        file.write(user_text + '\n')
    print("El texto se agrega al final del archivo sin borrar lo anterior")


add_lines("archivo_creado.txt")
