# Tabla de multiplicar personalizada
# Pida al usuario un número del 1 al 10
# Muestre su tabla de multiplicar del 1 al 12
# Ejemplo:
# Entrada: "Ingrese un número:" 7
# Salida: 
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 12 = 84

number = int(input("Ingrese un número del 1 al 10: "))
print(f"Tabla de multiplicar del {number}:")
for i in range(1, 13):
    result = number * i
    print(f"{number} x {i} = {result}")
    