import csv


file_name = "students.csv"


def export_students(students):
    if len(students) == 0:
        print("No hay estudiantes para exportar.")
        return
    
    try:
        with open(file_name, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "section", "spanish", "english", "sociales", "science"])
            for student in students:
                writer.writerow([
                    student["name"],
                    student["section"],
                    student["spanish"],
                    student["english"],
                    student["sociales"],
                    student["science"]
                ])
        print(f"Estudiantes exportados exitosamente a {file_name}.")
        
    except Exception as e:
        print(f"Error al exportar estudiantes: {e}")
        
        
def import_students():
    students = []
    
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = {
                    "name": row["name"],
                    "section": row["section"],
                    "spanish": int(row["spanish"]),
                    "english": int(row["english"]),
                    "sociales": int(row["sociales"]),
                    "science": int(row["science"])
                }
                students.append(student)
        print(f"Estudiantes importados exitosamente desde {file_name}.")
        return students
    
    except FileNotFoundError:
        print(f"No se encontró el archivo {file_name}.")
        return None
    
    except Exception as e:
        print(f"Error al importar estudiantes: {e}")
        return None
