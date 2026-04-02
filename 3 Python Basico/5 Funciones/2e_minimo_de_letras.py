# Cree una función que reciba una lista de palabras y un número n,
# y retorne una nueva lista con solo las palabras que tengan más de n letras
# Ejemplo: ["cielo", "sol", "maravilloso", "día"]
# "Ingrese el numero de letras minimas en la palabra: " 4
# ["cielo", "maravilloso"]

def min_of_chars(words, min_chars):
    words_with_min_of_chars = []
    for word in words:
        if len(word) > min_chars:
            words_with_min_of_chars.append(word)
    return words_with_min_of_chars


if __name__ == "__main__":
    user_phrase = input("Ingrese su frase completa:")
    words = user_phrase.split()
    user_list = print(f'Su frase quedó en la siguiente lista: {words}')
    min_chars = int(input("Ingrese el número de letras mínimo: "))
    result = min_of_chars(words, min_chars)
    print(result)
