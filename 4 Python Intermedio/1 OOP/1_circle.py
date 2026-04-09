# Cree una clase de Circle con:
# Un atributo de radius (radio).
# Un método de get_area que retorne su área.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = math.pi*(radius**2)
        return area

radius = int(input("Ingrese su radio: "))
my_area = Circle(radius)
print(f"Su área es de: {my_area.get_area()} unidades al cuadrado")
