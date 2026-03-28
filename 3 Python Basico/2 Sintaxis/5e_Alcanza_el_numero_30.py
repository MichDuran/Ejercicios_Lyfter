# Cree un diagrama de flujo que pida 3 números al usuario. 
# Si uno de esos números es 30, o si los 3 sumados dan 30, mostrar “Correcto”. 
# Sino, mostrar “incorrecto”.
# Ejemplos:
# 23, 30, 768 → Correcto (hay un 30)
# 10, 15, 5 → Correcto (10 + 15 + 5 = 30)
# 35, 56, 2 → Incorrecto (no hay ningún 30, y la suma de ellos tampoco da 30)

first_numero = int(input("Ingrese el primer número: "))
second_numero = int(input("Ingrese el segundo número: "))
third_numero = int(input("Ingrese el tercer número: "))
if(first_numero + second_numero + third_numero == 30):
    print("Correcto")
elif(first_numero == 30 or second_numero == 30 or third_numero == 30):
    print("Correcto")
else:
    print("Incorrecto")
    