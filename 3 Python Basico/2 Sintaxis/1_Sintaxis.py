#Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.
#Si le salen errores, no se asuste. Lealos e intente comprender qué significan.
#Los errores son oportunidades de aprendizaje.
#Por ejemplo:

# string + string → ?
str_plus_str = "Hola " + "Mundo"
print(str_plus_str)  # Resultado: "Hola Mundo"

# string + int → ?
#str_plus_int = "Tengo " + 32 + " años"
#print(str_plus_int)  # Resultado: TypeError: can only concatenate str (not "int") to str
fix_str_plus_int = "Tengo " + str(32) + " años"
print(fix_str_plus_int)  # Resultado: "Tengo 32 años"

# list + list → ?
list_plus_list = [1, 2, 3] + [4, 5, 6]
print(list_plus_list)  # Resultado: [1, 2, 3, 4, 5, 6]

# string + list → ?
#str_plus_list = "Números: " + [1, 2, 3]
#print(str_plus_list)  # Resultado: TypeError: can only concatenate str (not "list") to str
fix_str_plus_list = "Números: " + str([1, 2, 3])
print(fix_str_plus_list)  # Resultado: "Números: [1, 2, 3]"

# float + int → ?
float_plus_int = 3.14 + 2
print(float_plus_int)  # Resultado: 5.14

# bool + bool → ?
bool_plus_bool = True + False
print(bool_plus_bool)  # Resultado: 1 (True se interpreta como 1 y False como 0)