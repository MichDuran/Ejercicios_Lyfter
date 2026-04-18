# Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.

class Logger:
    def log(self, message):
        print(f"[LOG]: {message}")

class Calculator:
    def add(self, a, b):
        return a+b
    
    def subtract(self, a, b):
        return a-b    
    
class AdvanceCalculator(Logger, Calculator):
    def multiply(self, a, b):
        resultado = a*b
        self.log(f"Multiplicando {a} por {b} = {resultado}")
        return resultado


if __name__ == "__main__":
    school_calculator = AdvanceCalculator()
    print(f"Suma: {school_calculator.add(5, 3)}")
    print(f"Resta: {school_calculator.subtract(3, 5)}")
    school_calculator.multiply(4, 6)
    school_calculator.log("Operaciones realizadas con éxito")
