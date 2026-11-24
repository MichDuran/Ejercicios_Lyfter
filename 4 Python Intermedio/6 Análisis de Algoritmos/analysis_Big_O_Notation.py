## Análisis 1: print_numbers_times_2
def print_numbers_times_2(numbers_list):
	for number in numbers_list: # O(n): Iterar sobre cada elemento de la lista es una operación lineal.
		print(number * 2) # O(1): Imprimir en consola es una operación constante, al igual que la multiplicación.

# Complejidad temporal: O(n) - lineal ya que recorre todos los elementos una sola vez y no crea ninguna estructura de datos adicional.
# donde n es la longitud de la lista numbers_list.



## Análisis 2: check_if_lists_have_an_equal
def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a: # O(n): Iterar sobre cada elemento de la lista_a es una operación lineal.
		for element_b in list_b: # O(m): Recorre la segunda lista por cada elemento de la primera.
			if element_a == element_b: # O(1): Comparar dos valores es una operación constante.
				return True # O(1): Finaliza la función anticipadamente. Retornar un valor es una operación constante.
				
	return False # O(1): Retorna un valor si no hay coincidencias. Es una operación constante.

# Complejidad temporal: O(n * m) - donde n es la longitud de la lista_a y m es la longitud de la lista_b.
# En el peor caso, se deben comparar todos los elementos de ambas listas.
# Es un algoritmo de complejidad cuadrática si ambas listas tienen el mismo tamaño, 
# aunque la notación más precisa es O(n * m).



## Análisis 3: print_10_or_less_elements
def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print) # O(1): Obtener la longitud de la lista es una operación constante.
	for index in range(min(list_len, 10)):  # O(1): Calcular el mínimo entre dos valores es una operación constante.
		print(list_to_print[index]) # O(1): Acceder a un elemento de la lista por índice es una operación constante, al igual que imprimir en consola.
  
  # Aunque tenemos un ciclo for, este nunca realizará más de 10 iteraciones, independientemente del tamaño de la lista.
  # Por lo tanto, la complejidad temporal de esta función es O(1) - constante, 
  # ya que el número de operaciones no depende del tamaño de la lista de entrada.
  
  
  
  ## Análisis 4: generate_list_trios
def generate_list_trios(list_a, list_b, list_c):
	result_list = [] # O(1): Inicializar una lista vacía es una operación constante.
	for element_a in list_a: # O(n): Iterar sobre cada elemento de la lista_a es una operación lineal.
		for element_b in list_b: # O(m): Recorre la segunda lista por cada elemento de la primera.
			for element_c in list_c: # O(p): Recorre la tercera lista por cada par de elementos de las dos primeras.
				result_list.append(f'{element_a} {element_b} {element_c}') # O(1): Agregar un elemento al final de la lista es una operación constante, aunque se realiza n * m * p veces.
				
	return result_list # O(1): Retorna la lista resultante. Es una operación constante.

# Complejidad temporal: O(n * m * p) - donde n es la longitud de la lista_a, 
# m es la longitud de la lista_b y p es la longitud de la lista_c.
# En el peor caso, se deben generar todas las combinaciones posibles de elementos de las tres listas.
# Es un algoritmo de complejidad cúbica cuando las tres listas tienen el mismo tamaño.
# Si alguna lista está vacía, no se generan combinaciones, aunque los ciclos exteriores podrían realizar algunas iteraciones.