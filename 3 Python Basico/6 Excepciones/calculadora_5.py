def mostrar_menu():
    print("\n--- CALCULADORA ---")
    print(f"Número actual: {numero_actual}")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Borrar resultado")
    print("6. Salir")


def obtener_numero():
    while True:
        try:
            return float(input("Ingresa un número: "))
        except ValueError:
            print("❌ Error: Debes ingresar un número válido.")


numero_actual = 0

while True:
    mostrar_menu()

    try:
        opcion = int(input("Selecciona una opción: "))

        match opcion:

            case 1:
                numero = obtener_numero()
                numero_actual += numero
                print("Resultado:", numero_actual)

            case 2:
                numero = obtener_numero()
                numero_actual -= numero
                print("Resultado:", numero_actual)

            case 3:
                numero = obtener_numero()
                numero_actual *= numero
                print("Resultado:", numero_actual)

            case 4:
                numero = obtener_numero()
                if numero == 0:
                    print("❌ Error: No se puede dividir entre 0.")
                else:
                    numero_actual /= numero
                    print("Resultado:", numero_actual)

            case 5:
                numero_actual = 0
                print("🧹 Resultado reiniciado a 0")

            case 6:
                print("👋 Saliendo de la calculadora...")
                break

            case _:
                print("❌ Error: Opción inválida.")

    except ValueError:
        print("❌ Error: Debes ingresar un número válido.")
        