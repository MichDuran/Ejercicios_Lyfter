# Cree una calculadora por linea de comando. 
# Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
# 1. Suma
# 2. Resta
# 3. Multiplicación
# 4. División
# 5. Borrar resultado
# Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar,
# o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
# Debe de mostrar mensajes de error usando excepciones si el usuario selecciona una opción invalida, 
# o si ingresa un número invalido a la hora de hacer la operación.

def main():
    current_number = 0
    while True:
        print(f"Current number: {current_number}")
        print("Menu:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Borrar resultado")
        choice = input("Seleccione una opción (1-5): ")
        
        try:
            if choice == '1':
                num = float(input("Ingrese un número para sumar: "))
                current_number += num
            elif choice == '2':
                num = float(input("Ingrese un número para restar: "))
                current_number -= num
            elif choice == '3':
                num = float(input("Ingrese un número para multiplicar: "))
                current_number *= num
            elif choice == '4':
                num = float(input("Ingrese un número para dividir: "))
                if num == 0:
                    raise ValueError("No se puede dividir por cero.")
                current_number /= num
            elif choice == '5':
                current_number = 0
            else:
                raise ValueError("Opción inválida. Por favor seleccione una opción entre 1 y 5.")
        except ValueError as e:
            print(f"Error: {e}")
if __name__ == "__main__":    main()
