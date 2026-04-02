# Cree un algoritmo que defina una cantidad de metros (por ejemplo, 5) y luego use print() para mostrar cuántos centímetros son.
meters_str = input("Ingrese un número de metros: ")
meters = int(meters_str)
centimeters = meters * 100
print("Los " + str(meters) + " metros que ingresaste son " + str(centimeters) + " centímetros")
