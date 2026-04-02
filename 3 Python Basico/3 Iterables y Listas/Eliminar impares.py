# Cree un programa que elimine todos los números impares de una lista.
# Ejemplos:
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] → [2, 4, 6, 8]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in my_list[:]:
    if num % 2 != 0:
        my_list.pop(my_list.index(num))
print(my_list)
