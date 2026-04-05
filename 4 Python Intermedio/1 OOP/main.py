# Duplique el proyecto Sistema de Control de Estudiantes y modifíquelo para usar 
# objetos para guardar la información de los estudiantes (creando una clase de Student).
# Hay que cambiar los estudiantes de diccionarios a objetos.
# Hay que convertir la data del csv (que viene por defecto en formato de diccionario) a objetos al importarla.
# Hay que convertir los objetos a diccionarios para poder exportarlos a csv.
# Hay que modificar el acceso a los keys para accesar a atributos.
# student[’Name’] → student.name

# Antes:
# def create_student(students_list):
# 	name = input("Inserte su nombre: ")
# 	score = input("Inserte su nota: ")
# 	# (...)
# 	students_list.append({
# 		"name": name,
# 		"score_1": score_1,
# 		# (...)
# 	})

# Despues:
#     class Student():
# 	    def __init__(self, name, score_1):
# 		self.name = name
# 		self.score_1 = score_1
# 		# (...)

# def create_student(students_list):
# 	name = input("Inserte su nombre: ")
# 	score_1 = input("Inserte su nota: ")
# 	# (...)
# 	students_list.append(
# 		Student(name, score_1, (...))
# 	)

# La única diferencia es que ahora se crea un Student en vez de un diccionario.


from menu import main_menu


def main():
    students = []
    main_menu(students)
    
    
if __name__ == "__main__":
    main()
