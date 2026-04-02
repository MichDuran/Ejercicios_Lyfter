# Cree un programa que le pida al usuario ingresar 5 palabras. 
# Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras.

words = []
for i in range(5):
    word = input(f"Ingrese la palabra {i+1}: ")
    words.append(word)
more_than_4 = []
for word in words:
    if len(word) > 4:
        more_than_4.append(word)
print("Las palabras ingresadas son:", words)
print("Las palabras con más de 4 letras son:", more_than_4)
