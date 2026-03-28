# Cree una función que acepte un string con palabras separadas por un guion
# y retorne un string igual pero ordenado alfabéticamente.

def order_strings_alphabeticly(placeholder):
    split_words = placeholder.split("-")
    print(f'1: {split_words}')
    sorted_string_to_list = sorted(split_words)
    print(f'2: {sorted_string_to_list}')
    add_hyphen = "-".join(sorted_string_to_list)
    print(f'3: {add_hyphen}')
    return add_hyphen

string1 = "standing-here-i-realize"
print(order_strings_alphabeticly(string1))