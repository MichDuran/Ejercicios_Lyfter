# Experimente con el concepto de scope:
# Intente acceder a una variable definida dentro de una función desde afuera.
# Intente acceder a una variable global desde una función y cambiar su valor.

# Variable local
def local_variable():
    variable_inside_function_scope = 5
    print('Variable local:')
    print(f'Dentro de la función: {variable_inside_function_scope}')


local_variable()
# print(f'Fuera de la función: {variable_inside_function_scope}' ) # Esto no funciona porque la variable está definida dentro de la función
print('----------')

# Variable global
global_variable = 10

def print_variable():
    print('Variable global:')
    print(f'Dentro de la función: {global_variable}')
    # global_variable = 30 # Esto no funciona porque no se puede acceder a la variable global dentro de la función


print_variable()
print(f'Fuera de la función (+5 unidades): {global_variable + 5}')
print('----------')

# Variable global con el global dentro de la función
global_variable_2 = 20
print(f'Variable global antes del cambio en la función: {global_variable_2}')

def change_global_variable():
    global global_variable_2
    global_variable_2 = 30
    print(f'Variable global modificada dentro de la función con el global: {global_variable_2}')


change_global_variable()
