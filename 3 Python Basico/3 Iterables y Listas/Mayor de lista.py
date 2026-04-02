# Cree un programa que le pida al usuario 10 números
# y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
# Ejemplos:
# 86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [86, 54, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86.

numbers = []
for i in range(10):
    num = int(input("Ingrese un número: "))
    numbers.append(num)
    if i == 0:
        max_num = num
    elif num > max_num:
        max_num = num
print("Los números ingresados son:", numbers)
print("El número más alto fue:", max_num)
