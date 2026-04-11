from actions import (
    add_students,
    show_all_students,
    show_top_3,
    show_general_average,
    delete_student,
    show_failed_students
)
from data import (
    export_students,
    import_students
)


def show_menu():
    print("\nMenú de opciones:")
    print("1. Agregar estudiantes")
    print("2. Mostrar todos los estudiantes")
    print("3. Mostrar los 3 mejores estudiantes")
    print("4. Mostrar el promedio general")
    print("5. Eliminar un estudiante")
    print("6. Mostrar estudiantes reprobados")
    print("7. Exportar estudiantes a CSV")
    print("8. Importar estudiantes desde CSV")
    print("9. Salir")


def main_menu(students):
    while True:
        show_menu()
        choice = input("Seleccione una opción: ")

        if choice == "1":
            add_students(students)
        elif choice == "2":
            show_all_students(students)
        elif choice == "3":
            show_top_3(students)
        elif choice == "4":
            show_general_average(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            show_failed_students(students)
        elif choice == "7":
            export_students(students)
        elif choice == "8":
            imported_students = import_students()
            if imported_students is not None:
                students.clear()
                students.extend(imported_students)
        elif choice == "9":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
