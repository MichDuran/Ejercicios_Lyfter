# Cree una función sumar_valores(lista) que reciba una lista de elementos (strings, enteros, flotantes mezclados)
# Intente convertir cada elemento a tipo float
# Si puede, sume el valor y muestre: "<valor> sumado correctamente"
# Si no puede, muestre: "Elemento inválido: <valor>"
# Al final, imprima la suma total

def sum_values(user_list):
    total_sum = 0
    for i in range(len(user_list)):
        try:
            original_value = user_list[i]
            user_list[i] = float(original_value)
            print(f'{user_list[i]} sumado correctamente')
            total_sum += user_list[i] 
        except ValueError:
            print(f'Elemento inválido: {original_value}')
    print(f'Total de la suma: {total_sum}')
                  

def main():
    my_list = ['10', 'manzana', '5.5', '3', 'n/a']
    print('Resultado:')
    sum_values(my_list)


if __name__ == '__main__':
    main()
