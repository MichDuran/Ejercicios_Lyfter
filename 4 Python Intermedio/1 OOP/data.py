import csv


class Student:
    def __init__(self, name, section, spanish, english, sociales, science):
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.sociales = sociales
        self.science = science

    def to_dict(self):
        return {
            "name": self.name,
            "section": self.section,
            "spanish": self.spanish,
            "english": self.english,
            "sociales": self.sociales,
            "science": self.science
        }
    

def export_students(students, file_name = "students.csv"):
    if len(students) == 0:
        print("No hay estudiantes para exportar.")
        return
    
    try:
        with open(file_name, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["name", "section", "spanish", "english", "sociales", "science"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in students:
                writer.writerow(student.to_dict())
        print(f"Estudiantes exportados exitosamente a {file_name}.")
        
    except Exception as e:
        print(f"Error al exportar estudiantes: {e}")
        
        
def import_students(file_name = "students.csv"):
    students = []
    
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = Student(
                    row["name"],
                    row["section"],
                    float(row["spanish"]),
                    float(row["english"]),
                    float(row["sociales"]),
                    float(row["science"])
                )
                students.append(student)
        print(f"Estudiantes importados exitosamente desde {file_name}.")
        return students
    
    except FileNotFoundError:
        print(f"No se encontró el archivo {file_name}.")
        return None
    
    except Exception as e:
        print(f"Error al importar estudiantes: {e}")
        return None
