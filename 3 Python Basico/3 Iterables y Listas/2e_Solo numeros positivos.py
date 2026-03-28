# Cree un programa que verifique si todos los elementos de una lista son positivos

list_length = int(input("Ingrese la cantidad de números que desea agregar a la lista: "))
my_list = []
contador = 1
while contador <= list_length:
    num = int(input(f"Ingrese el número {contador}: "))
    my_list.append(num)
    contador += 1
print("La lista ingresada es:", my_list)
for num in my_list:
    if num <= 0:
        print("Hay al menos un número negativo o cero")
        break
else:
    print("Todos los números en la lista son positivos.")
