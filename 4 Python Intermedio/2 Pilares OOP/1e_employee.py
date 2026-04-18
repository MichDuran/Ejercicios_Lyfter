# Cree una clase Employee con los siguientes requisitos:
# Atributos privados: _name, _salary
# Use @property y @<atributo>.setter para:
# Mostrar el nombre y el salario
# Validar que el salario nunca sea negativo
# Cree un método promote que aumente el salario un porcentaje definido

class Employee:
    def __init__ (self, name, salary):
        self.name = name
        self.salary = salary
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("El nombre no puede estar vacío")
        self._name = value
        
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("El salario no puede ser negativo")
        self._salary = value
        
    def promote(self, percentage):
        if percentage < 0:
            raise ValueError("El porcentaje de aumento no puede ser negativo")
        self._salary += self._salary * (percentage / 100)

if __name__ == "__main__":
    employee = Employee("Mich Duran", 1000)
    print(f"Empleado: {employee.name}, Salario: {employee.salary}")
    employee.promote(10)
    print(f"Empleado: {employee.name}, Salario después de promoción: {employee.salary}")
    
    try:
        employee.salary = -1000
    except ValueError as e:
        print(f"Error al establecer salario: {e}")
    try:        
        employee.promote(-5)
    except ValueError as e:
        print(f"Error al promover empleado: {e}")
