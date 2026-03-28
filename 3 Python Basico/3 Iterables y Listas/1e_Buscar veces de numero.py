# Cree un programa que cuente cuántas veces aparece un número específico en una lista. 
# Pida al usuario una lista de números y otro número a buscar.

list_length = int(input("Ingrese la cantidad de números que desea agregar a la lista: "))
my_list = []
contador = 1
while contador <= list_length:
    num = int(input(f"Ingrese el número {contador}: "))
    my_list.append(num)
    contador += 1
number_to_find = int(input("Ingrese el número que desea buscar: "))
count = my_list.count(number_to_find)
print(f"El número {number_to_find} aparece {count} veces en la lista.")
