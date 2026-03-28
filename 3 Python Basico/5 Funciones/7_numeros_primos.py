# Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
# [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
# Tip 1: Investigue la lógica matemática para averiguar si un número es primo, 
# y conviértala a código. No busque el código, eso no ayudaría.
# Tip 2: Aquí hay que hacer varias cosas:
# recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista.
# Así que lo mejor es agregar otra función para revisar si el numero es primo o no.

def primality_test(n):
    if n <= 1: # 1 no es primo
        return False
    if n == 2: # 2 es primo
        return True
    if n % 2 == 0: # Los números pares no son primos
        return False
    for i in range(3, int(n**0.5) + 1, 2): # Empezamos en 3 y revisamos en saltos de 2 para SOLO números impares hasta la raíz cuadrada de n
        if n % i == 0:
            return False
    return True # Si no se encontró ningún divisor hasta n, entonces n es primo


def prime_numbers_from_list(numbers):
    prime_numbers = []
    for number in numbers:
        if primality_test(number):
            prime_numbers.append(number)
    return prime_numbers


if __name__ == "__main__":
    number_list = [1, 2, 4, 6, 7, 13, 9, 67, 50, 25, 35, 503]
    primes = prime_numbers_from_list(number_list)
    print(primes)
