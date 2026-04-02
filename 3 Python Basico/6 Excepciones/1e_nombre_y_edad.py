# Cree un programa que:
# Pida al usuario su nombre
# Si el nombre es numérico (isdigit()), haga raise ValueError("El nombre no puede ser un número")
# Luego pida su edad
# Si no es un número válido, capture el ValueError y muestre un mensaje
# Si todo sale bien, imprima un mensaje: "Hola <nombre>, su edad es <edad>"

def main():
    try:
        name = input('Ingrese su nombre: ')
        if name.isdigit():
            raise ValueError('El nombre no puede ser un número')
        try:
            age = int(input('Ingrese su edad: '))
        except ValueError:
            raise ValueError('Número no válido')
        return
    
        print(f'Hola {name}, su edad es {age}')
    
    except ValueError as ve:
        print(f'Error: {ve}')


if __name__ == '__main__':
    main()
    