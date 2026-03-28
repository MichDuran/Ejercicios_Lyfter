# Cree un programa que reciba una lista de números.
# Calcule el promedio de los valores.
# Luego cree una nueva lista con solo los valores mayores al promedio.

list_length = int(input("Ingrese la cantidad de números que desea agregar a la lista: "))
my_list = []
contador = 1
sum_my_list = 0
for i in range(list_length):
    num = int(input(f"Ingrese el número {contador}: "))
    my_list.append(num)
    contador += 1
    sum_my_list += num
average = sum_my_list / len(my_list)
greater_than_average = []
for num in my_list:
    if num > average:
        greater_than_average.append(num)
print("Los números ingresados en la lista son:", my_list)
print("El promedio de los números es:", average)
print("Los números mayores al promedio son:", greater_than_average)
