def mostrar_menu(numero_actual):
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


def main():
    numero_actual = 0

    while True:
        mostrar_menu(numero_actual)

        try:
            opcion = int(input("Selecciona una opción: "))

            match opcion:

                case 1:
                    numero_actual += obtener_numero()
                    print("Resultado:", numero_actual)

                case 2:
                    numero_actual -= obtener_numero()
                    print("Resultado:", numero_actual)

                case 3:
                    numero_actual *= obtener_numero()
                    print("Resultado:", numero_actual)

                case 4:
                    numero = obtener_numero()
                try:
                    numero_actual /= numero
                    print("Resultado:", numero_actual)
                except ZeroDivisionError:
                    print("❌ Error: No se puede dividir entre 0.")

                case 5:
                    numero_actual = 0
                    print("🧹 Resultado reiniciado a 0")

                case 6:
                    print("👋 Saliendo...")
                    break

                case _:
                    print("❌ Error: Opción inválida.")

        except ValueError:
            print("❌ Error: Debes ingresar un número válido.")


if __name__ == "__main__":
    main()
    