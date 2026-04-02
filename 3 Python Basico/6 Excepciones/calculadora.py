# Cree una calculadora por linea de comando. 
# Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
# 1. Suma
# 2. Resta
# 3. Multiplicación
# 4. División
# 5. Borrar resultado
# Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar,
# o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
# Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, 
# o si ingresa un número invalido a la hora de hacer la operación.


def menu(current_num):
    print('Bienvenido a su calculadora\n')
    print(f'Su número actual es: {current_num}')
    print('\n|   Menu:')
    print('|     1. Suma')
    print('|     2. Resta')
    print('|     3. Multiplicación')
    print('|     4. División')
    print('|     5. Borrar resultado')
    print('|     6. Salir')


def user_num():
    while True:
        try:
            return float(input('Ingrese un número: '))
        except ValueError as e:
            print(f'Error [Value Error]: Debe ingresar un número válido. Detalles: {e}')


def main():
    current_num = 0

    while True:
        menu(current_num)
        try:
            operator = int(input('\nSeleccione una opción del menú: '))
            
            match operator:
                case 1:
                    current_num += user_num()
                    print(f'Resultado de suma: {current_num}')

                case 2:
                    current_num -= user_num()
                    print(f'Resultado de resta: {current_num}')

                case 3:
                    current_num *= user_num()
                    print(f'Resultado de multiplicación: {current_num}')

                case 4:
                    no_zero_num = user_num()
                    try:
                        current_num /= no_zero_num
                        print(f'Resultado de división: {current_num}')
                    except ZeroDivisionError as e:
                        print(f'Error: No puede dividir entre 0. Detalles: {e}')

                case 5:
                    current_num = 0
                    print(f'Se reinició el resultado: {current_num}')
            
                case 6:
                    print('Bye')
                    break
        
                case _:
                    print('Error: Opción No Disponible. Debe ingresar una opción del menú')
        
        except ValueError as e:
            print(f'Error: Opción No Válida. Detalles {e}')


if __name__ == '__main__':
    main()
