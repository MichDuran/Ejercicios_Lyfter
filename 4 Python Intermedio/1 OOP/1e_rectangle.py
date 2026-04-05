# Cree una clase Rectangle que:
# Tenga atributos width y height
# Tenga un método get_area() que retorne el área
# Tenga un método get_perimeter() que retorne el perímetro
# Valide que ningún valor sea negativo. Si lo es, lance una excepción con un mensaje adecuado
# Ejemplo 1:
# Entrada:
# "Ingrese la altura: " 250
# "Ingrese el ancho: " 300
# Salida:
# print(rectangle.get_area()) #75000
# print(rectangle.get_perimeter()) #1100
# Entrada:
# "Ingrese la altura: " -250
# "Ingrese el ancho: " 300
# Salida:
# "Existe un valor negativo, los valores deben ser positivos"

class Rectangle:
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("Existe un valor negativo, los valores deben ser positivos")
        
        self.width = width
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = 2*self.width + 2*self.height
        return perimeter


def main():
    try:
        print("---Datos de su rectángulo---")
        width = float(input("Ingrese la altura: "))
        height = float(input("Ingrese el ancho: "))
        rectangle = Rectangle(width, height)

        print(f"Área = {rectangle.get_area()} unidades al cuadrado")
        print(f"Perímetro = {rectangle.get_perimeter()} unidades")

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
