# Cree una clase abstracta de Shape que:
# Tenga los métodos abstractos de calculate_perimeter y calculate_area.
# Ahora cree las siguientes clases que hereden de Shape e implementen esos métodos: Circle, Square y Rectangle.
# Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.


import math

class Shape:
    def calculate_perimeter(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")
    
    def calculate_area(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")
    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    
    def calculate_area(self):
        return math.pi * self.radius**2
    
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def calculate_perimeter(self):
        return 4 * self.side
    
    def calculate_area(self):
        return self.side**2
    

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    
    def calculate_area(self):
        return self.width * self.height
    
    
if __name__ == "__main__":
    circle = Circle(radius=5)
    print(f"Radio del círculo: {circle.radius}")
    print(f"Perímetro del círculo: {circle.calculate_perimeter()}")
    print(f"Área del círculo: {circle.calculate_area()}")
    
    square = Square(side=5)
    print(f"Lado del cuadrado: {square.side}")
    print(f"Perímetro del cuadrado: {square.calculate_perimeter()}")
    print(f"Área del cuadrado: {square.calculate_area()}")
    
    rectangle = Rectangle(width=5, height=10)
    print(f"Base del rectángulo: {rectangle.width} y altura del rectángulo: {rectangle.height}")
    print(f"Perímetro del rectángulo: {rectangle.calculate_perimeter()}")
    print(f"Área del rectángulo: {rectangle.calculate_area()}")
