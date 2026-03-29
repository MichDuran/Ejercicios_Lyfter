def is_valid_name(name):
    if name.strip() == "":
        return False
    
    for char in name:
        if char.isdigit():
            return False
    
    return True


def is_valid_section(section):
    section = section.strip()
    
    if len(section) < 2 or len(section) > 3:
        return False
    
    numbers_part = section[:-1]
    letter_part = section[-1]
    
    if not numbers_part.isdigit():
        return False
    
    if not letter_part.isalpha():
        return False
    
    if not letter_part.isupper():
        return False
    
    return True


def student_exists(students, name, section):
    for student in students:
        if (
            student["name"].lower() == name.lower() and 
            student["section"].upper() == section.upper()
        ):
            return True
    return False


def get_valid_name():
    while True:
        name = input("Ingrese el nombre del estudiante: ")
        if is_valid_name(name):
            return name
        else:
            print("Nombre no válido. Por favor, intente de nuevo.")
            

def get_valid_section():
    while True:
        section = input("Ingrese la sección del estudiante (ej. 11A, 12B): ")
        if is_valid_section(section):
            return section
        else:
            print("Sección no válida. Por favor, intente de nuevo.")
            
            
def get_valid_grade(subject):
    while True:
            grade = float(input(f"Ingrese la calificación de {subject}: "))
            
            try:
                grade = float(grade)
                if 0 <= grade <= 100:
                    return grade
                else:
                    print("La calificación debe estar entre 0 y 100. Intente de nuevo.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número válido.")
                

def calculate_average(student):
    average = (
        student["spanish"] +
        student["english"] +
        student["sociales"] +
        student["science"]
    ) / 4
    return average


def add_students(students):
    while True:
        amount = input("¿Cuántos estudiantes desea agregar? ")
        
        try:
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Por favor, ingrese un número mayor a cero.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")
            
    for i in range(amount):
        print(f"\nAgregando estudiante {i + 1} de {amount}")
        name = get_valid_name()
        section = get_valid_section()
                
        if student_exists(students, name, section):
            print("El estudiante ya existe. No se agregará nuevamente.")
            continue
                
        spanish = get_valid_grade("Español")
        english = get_valid_grade("Inglés")
        sociales = get_valid_grade("Sociales")
        science = get_valid_grade("Ciencias")
                
        student = {
            "name": name,
            "section": section,
            "spanish": spanish,
            "english": english,
            "sociales": sociales,
            "science": science
                }
                
        students.append(student)
        print(f"Estudiante {name} agregado exitosamente.")
                
                
def show_all_students(students):
    if len(students) == 0:
        print("No hay estudiantes registrados.")
        return
    
    print("\nLista de estudiantes:")
    for i, student in enumerate(students, start=1):
        print("\nEstudiante", i)
        print("Nombre:", student["name"])
        print("Sección:", student["section"])
        print("Español:", student["spanish"])
        print("Inglés:", student["english"])
        print("Sociales:", student["sociales"])
        print("Ciencias:", student["science"])
        print("Promedio:", calculate_average(student))
        
    
def show_top_3(students):
    if len(students) == 0:
        print("No hay estudiantes registrados.")
        return
    
    sorted_students = sorted(students, key=calculate_average, reverse=True)
    
    print("\nLos 3 mejores estudiantes:")
    limit = 3
    if len(sorted_students) < 3:
        limit = len(sorted_students)
        
    for i in range(limit):
        student = sorted_students[i]
        print(f"\nEstudiante {i + 1}")
        print("Nombre:", student["name"])
        print("Sección:", student["section"])
        print("Promedio:", calculate_average(student))
        
        
def show_general_average(students):
    if len(students) == 0:
        print("No hay estudiantes registrados.")
        return
    
    total = 0
    
    for student in students:
        total += calculate_average(student)
        
    general_average = total / len(students)
    print(f"\nEl promedio general de todos los estudiantes es: {general_average:.2f}")
    
    
def delete_student(students):
    if len(students) == 0:
        print("No hay estudiantes registrados.")
        return
    
    name = input("Ingrese el nombre del estudiante a eliminar: ")
    section = input("Ingrese la sección del estudiante a eliminar: ")
    
    for student in students:
        if (
            student["name"].lower() == name.lower() and 
            student["section"].upper() == section.upper()
        ):
            confirm = input(f"¿Está seguro que desea eliminar al estudiante {name} de la sección {section}? (s/n): ")
            if confirm.lower() == "s":
                students.remove(student)
                print(f"Estudiante {name} eliminado exitosamente.")
            else:
                print("Eliminación cancelada.")
            return
    
    print("No se encontró un estudiante con ese nombre y sección.")
    
    
def get_failed_students(students):
    failed_students = []
    
    if student["spanish"] < 60:
        failed_students.append(("Español", student["spanish"]))
    if student["english"] < 60:
        failed_students.append(("Inglés", student["english"]))
    if student["sociales"] < 60:
        failed_students.append(("Sociales", student["sociales"]))
    if student["science"] < 60:
        failed_students.append(("Ciencias", student["science"]))
        
    return failed_students


def show_failed_students(students):
    if len(students) == 0:
        print("No hay estudiantes registrados.")
        return
    
    found_failed = False
    print("\nEstudiantes reprobados:")
    for student in students:
        failed_subjects = get_failed_students(student)
        
        if len(failed_subjects) > 0:
            found_failed = True
            print(f"\nNombre: {student['name']}")
            print(f"Sección: {student['section']}")
            print("Materias reprobadas:")
            for subject, grade in failed_subjects:
                print(f"{subject}: {grade}")
                
    if not found_failed == False:
        print("No hay estudiantes reprobados.")
           