# Cree una función convertir_a_entero(lista) que reciba una lista de strings
# Intente convertir cada elemento a entero usando int()
# Use try-except para atrapar los errores ValueError
# Si algún elemento no puede convertirse, mostrar "No se pudo convertir el elemento: <valor>" 
# y continuar con los demás

def change_to_int(user_list):
    for i in range(len(user_list)):
        try:
            original_value = user_list[i]
            user_list[i] = int(original_value)
            print(f'"{original_value}" convertido a {user_list[i]}')
        except ValueError:
            print(f'No se pudo convertir el elemento: "{original_value}"')


def main():
    my_list = ['4', 'hola', '10', '5.2']
    print('Resultado:')
    change_to_int(my_list)


if __name__ == '__main__':
    main()
