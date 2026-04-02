# Cree una función que retorne la suma de todos los números de una lista.
# La función va a tener un parámetro (la lista) y retornar un número (la suma de todos sus elementos).

def sum_of_list(numbers):
    total_sum = 0
    for number in numbers:
        total_sum += number
    return total_sum


if __name__ == "__main__":
    my_list = [4, 6, 2, 29]
    result = sum_of_list(my_list)
    print(f'La suma de los números en la lista {my_list} es: {result}')
