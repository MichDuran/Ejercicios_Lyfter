# Cree una función que le dé la vuelta a un string y lo retorne.
# Esto ya lo hicimos en iterables.
# “Hola mundo” → “odnum aloH”

def string_in_reverse(s):
    reversed_string = ""
    for i in range(len(s)-1, -1, -1):
        reversed_string += s[i]
    return reversed_string

if __name__ == "__main__":
    original_string = "Hola mundo"
    result = string_in_reverse(original_string)
    print(f'{original_string} --> {result}')
