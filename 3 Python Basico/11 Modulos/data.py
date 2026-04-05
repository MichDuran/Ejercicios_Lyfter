import csv


def export_students(students, file_name = "students.csv"):
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
        
        
def import_students(file_name = "students.csv"):
    students = []
    
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = {
                    "name": row["name"],
                    "section": row["section"],
                    "spanish": float(row["spanish"]),
                    "english": float(row["english"]),
                    "sociales": float(row["sociales"]),
                    "science": float(row["science"])
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
