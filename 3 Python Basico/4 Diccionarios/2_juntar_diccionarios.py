# Cree un programa que cree un diccionario usando dos listas del mismo tamaño,
# usando una para sus keys, y la otra para sus values.
# Ejemplos:
# list_a = [’first_name’, ‘last_name’, ‘role’]
# list_b = [’Alek’, ‘Castillo’, ‘Software Engineer’]
# {’first_name’: ‘Alek’, ‘last_name’: ‘Castillo’, ‘role’: ‘Software Engineer’}

list_keys = ['first_name', 'last_name', 'role']
list_values = ['Mich', 'Duran', 'Software Engineer']
new_dictionary = {}
for i in range(len(list_keys)):
    new_dictionary[list_keys[i]] = list_values[i]
print(new_dictionary)
