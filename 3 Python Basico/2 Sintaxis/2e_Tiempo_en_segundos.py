# Cree un código que le pida un tiempo en segundos al usuario y 
# calcule si es menor o mayor a 10 minutos. 
# Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. 
# Si es mayor, muestre “Mayor”. Si es exactamente igual, muestre “Igual”.
# Ejemplos:
# 1040 → Mayor
# 140 → 460
# 600 → Igual
# 599 → 1

time_seconds = int(input("Ingrese un tiempo en segundos: "))
if time_seconds > 600:
    print("Mayor")
elif time_seconds == 600:
    print("Igual")
else:
    time_remaining = 600 - time_seconds
    print(f"Faltan {time_remaining} segundos para llegar a 10 minutos.")
    