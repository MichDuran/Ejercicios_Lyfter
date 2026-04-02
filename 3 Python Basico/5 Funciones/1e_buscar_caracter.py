# Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto.
# Ejemplo: palabra "programacion"
# "Ingrese el carácter que desea buscar:" "o"
# "Se ha encontrado 2 veces el carácter solicitado"

def look_for_char():
    counter = 0
    user_text = input("Ingrese su palabra: ")
    char_wished = input ("Ingrese la letra que desea buscar: ")
    text_to_list = list(user_text)
    for i in range(len(text_to_list)):
        if text_to_list[i] == char_wished:
            counter += 1
    print(f'Se ha encontrado {counter} veces el carácter solicitado')


if __name__ == "__main__":
    look_for_char()
