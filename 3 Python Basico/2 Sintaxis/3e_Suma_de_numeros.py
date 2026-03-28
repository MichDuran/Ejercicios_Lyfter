# Cree un algoritmo que le pida un numero al usuario, 
# y realice una suma de cada numero del 1 hasta ese número ingresado. 
# Luego muestre el resultado de la suma.
# 5 → 15 (1 + 2 + 3 + 4 + 5)
# 3 → 6 (1 + 2 + 3)
# 12 → 78 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12)

desired_number = 0
counter = 1
sum_of_numbers = 0
desired_number = int(input("Ingrese el número deseado para la suma: "))
if desired_number < 1:
    print("Por favor, ingrese un número mayor o igual a 1.")
else:
    while counter <= desired_number:
        sum_of_numbers = sum_of_numbers + counter
        counter = counter + 1
    print(f"La suma progresiva de los números del 1 al {desired_number} es: {sum_of_numbers}")
    