#Cree un programa que le pida al usuario su nombre, apellido, y edad, y 
#muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.

name = input("Ingrese su nombre: ")
lastName = input("Ingrese su apellido: ")
age = int(input("Ingrese su edad: "))
if age < 2:
    print(name, lastName, "es un bebé.")
elif age < 12:
    print(name, lastName, "es un niño.")
elif age < 18:
    print(name, lastName, "es un adolescente.")
elif age < 30:
    print(name, lastName, "es un adulto joven.")
elif age < 60:
    print(name, lastName, "es un adulto.")
else:
    print(name, lastName, "es un adulto mayor.")
    