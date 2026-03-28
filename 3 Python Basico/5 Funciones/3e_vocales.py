# Cree una función que reciba un string y retorne cuántas vocales contiene

def count_vowels(word):
    vowels = "aeiouAEIOU"
    counter = 0
    for letter in word:
        if letter in vowels:
            counter += 1
    return counter

if __name__ == "__main__":
    user_text = input('Ingrese una oración para buscar vocales: ')
    print(f'Se encontraron {count_vowels(user_text)} vocales en su oración')
