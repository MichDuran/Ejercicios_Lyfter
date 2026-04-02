# Cree un programa que le pida tres números al usuario y muestre el mayor.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
higher = num1  # Asumimos que el primer número es el mayor inicialmente
if num2 > higher:
    higher = num2
if num3 > higher:
    higher = num3
print(f"El número mayor es: {higher}")
