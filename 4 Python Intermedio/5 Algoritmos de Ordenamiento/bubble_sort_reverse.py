# Modifica el bubble_sort para que funcione de derecha a izquierda, ordenando los números menores primero.

def bubble_sort(list_to_sort):
    n = len(list_to_sort)
    for outer_index in range(0, n - 1):
        has_made_changes = False
        
        for inner_index in range (n - 1, outer_index, -1):
            current_value = list_to_sort[inner_index]
            next_value = list_to_sort[inner_index - 1]
            
            print(f"Iteración {outer_index}, {inner_index}. Valor actual: {current_value}, siguiente valor: {next_value}")
            
            if current_value < next_value:
                print(f"Intercambiando {current_value} y {next_value}")
                list_to_sort[inner_index] = next_value
                list_to_sort[inner_index - 1] = current_value
                has_made_changes = True
                
        if not has_made_changes:
            print("No se hicieron cambios en esta iteración, la lista ya está ordenada.")
            break
# my_list = [5, 2, 9, 1, 5, 6]
my_list = [1,2,3,10,4,5,6,7,8]
print("Lista original:", my_list)

bubble_sort(my_list)
print("Lista ordenada:", my_list)