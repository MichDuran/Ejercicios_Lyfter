# Agrupar empleados por departamento
# Dada una lista de empleados donde cada uno tiene nombre, correo y departamento.
# Cree un diccionario que agrupe los empleados por su departamento:

employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
    {"name": "Miguel", "email": "miguel@empresa.com", "department": "TI"},
    {"name": "Laura", "email": "laura@empresa.com", "department": "RRHH"}
]

grouped_employees = {}
for employee in employees:
    department = employee["department"]
    if department not in grouped_employees:
        grouped_employees[department] = []
    grouped_employees[department].append(employee)
print(grouped_employees)
