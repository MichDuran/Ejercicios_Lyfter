# Cree una función que acepte un string con palabras separadas por un guion 
# y retorne un string igual pero ordenado alfabéticamente.
# Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
# “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

def sort_alphabetically(original_text):
    original_list = original_text.split("-")
    original_list.sort()
    return "-".join(original_list)


if __name__ == "__main__":
    user_text = input("Ingrese su texto separado por guiones medios: ")
    result = sort_alphabetically(user_text)
    print(f'Su texto original: {user_text}')
    print(f'Quedó ordenado alfabéticamente así: {result}')
