# Cree un programa que muestre el valor más pequeño de una lista sin usar min().
# Use una variable para comparar uno a uno

list_length = int(input("Ingrese la cantidad de números que desea agregar a la lista: "))
my_list = []
for i in range(list_length):
    num = int(input("Ingrese un número: "))
    my_list.append(num)
    if i == 0:
        min_num = num
    elif num < min_num:
        min_num = num
print("Los números ingresados en la lista son:", my_list)
print("El número más pequeño es:", min_num)
