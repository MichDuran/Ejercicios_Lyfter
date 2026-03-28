def mostrar_menu():
    print("\n--- CALCULADORA ---")
    print("Número actual:", numero_actual)
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Borrar resultado")
    print("6. Salir")


def obtener_numero():
    while True:
        try:
            num = float(input("Ingresa un número: "))
            return num
        except ValueError:
            print("❌ Error: Debes ingresar un número válido.")


numero_actual = 0

while True:
    mostrar_menu()

    try:
        opcion = int(input("Selecciona una opción: "))

        if opcion == 6:
            print("👋 Saliendo de la calculadora...")
            break

        elif opcion == 5:
            numero_actual = 0
            print("🧹 Resultado reiniciado a 0")

        elif opcion in [1, 2, 3, 4]:
            numero = obtener_numero()

            if opcion == 1:
                numero_actual += numero
                print("Resultado:", numero_actual)

            elif opcion == 2:
                numero_actual -= numero
                print("Resultado:", numero_actual)

            elif opcion == 3:
                numero_actual *= numero
                print("Resultado:", numero_actual)

            elif opcion == 4:
                if numero == 0:
                    print("❌ Error: No se puede dividir entre 0.")
                else:
                    numero_actual /= numero
                    print("Resultado:", numero_actual)

        else:
            print("❌ Error: Opción inválida.")

    except ValueError:
        print("❌ Error: Debes ingresar un número válido para la opción.")
        