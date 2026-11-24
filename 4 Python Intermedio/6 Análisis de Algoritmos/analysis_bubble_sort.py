# Análisis de Bubble Sort usando la Big O Notation

def bubble_sort(list_to_sort):
    n = len(list_to_sort) # O(1): Obtener la longitud de la lista es una operación constante.
    for outer_index in range(0, n - 1): # O(n): Ciclo externo que se ejecuta n-1 veces.
        has_made_changes = False # O(1): Asignación de una variable booleana es una operación constante.
        
        for inner_index in range(0, n - 1 - outer_index): # O(n): Ciclo externo que se ejecuta n-1-outer_index veces.
            current_value = list_to_sort[inner_index] # O(1): Acceder a un elemento de la lista por índice es una operación constante.
            next_value = list_to_sort[inner_index + 1] # O(1): Acceder a un elemento de la lista por índice es una operación constante.
            
            print(f"Iteración {outer_index}, {inner_index}. Valor actual: {current_value}, siguiente valor: {next_value}") # O(1): Imprimir en consola es una operación constante.
            
            if current_value > next_value: # O(1): Comparar dos valores es una operación constante.
                print(f"Intercambiando {current_value} y {next_value}") # O(1): Imprimir en consola es una operación constante.
                list_to_sort[inner_index] = next_value # O(1): Acceder a un elemento de la lista por índice y asignarle un valor es una operación constante.
                list_to_sort[inner_index + 1] = current_value # O(1): Acceso por índice y asignación de valor es una operación constante.
                has_made_changes = True # O(1): Asignación de una variable booleana es una operación constante.
                
        if not has_made_changes: # O(1): Evaluar una condición booleana es una operación constante.
            print("No se hicieron cambios en esta iteración, la lista ya está ordenada.") # O(1): Imprimir en consola es una operación constante.
            break # O(1): Romper un ciclo es una operación constante.
my_list = [5, 2, 9, 1, 5, 6]
# my_list = [1,2,3,10,4,5,6,7,8]
print("Lista original:", my_list) # O(1): Imprimir en consola es una operación constante.

bubble_sort(my_list)
print("Lista ordenada:", my_list) # O(1): Imprimir en consola es una operación constante.

# Conclusión: La complejidad temporal del algoritmo Bubble Sort es O(n^2) en el peor caso, 
# ya que se realizan n-1 iteraciones en el ciclo externo y n-1-outer_index iteraciones en el ciclo interno. 
# Sin embargo, gracias a la implementación de la variable "has_made_changes" y la instrucción break, 
# el algoritmo puede finalizar anticipadamente cuando la lista está ordenada, 
# obteniendo una complejidad temporal de O(n) en el mejor caso.