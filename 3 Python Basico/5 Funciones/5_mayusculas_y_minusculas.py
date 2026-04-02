# Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string.
# “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

def count_upper_and_lower(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count


if __name__ == "__main__":
    input_string = str(input("Ingrese su palabra: "))
    upper, lower = count_upper_and_lower(input_string)
    print(f'Su palabra "{input_string}" --> contiene {upper} mayúsculas y {lower} minúsculas')
