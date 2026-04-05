# Cree una clase base Animal y dos clases hijas Dog y Cat:
# Animal debe tener nombre y método speak() que retorne "Hace un sonido"
# Dog debe sobrescribir speak() para decir "Guau"
# Cat debe sobrescribir speak() para decir "Miau"
# Ejemplo:
# Entrada:
# dog = Dog("Firulais")
# Salida:
# print(dog.speak())  # Guau

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} hace un sonido"


class Dog(Animal):
    def speak(self):
        return f"{self.name} hace Guau"


class Cat(Animal):
    def speak(self):
        return f"{self.name} hace Miau"


def main():
    animal = Animal("Otro animal")
    dog = Dog("Firulais")
    cat = Cat("Michi")
    print(animal.speak())
    print(dog.speak())
    print(cat.speak())


if __name__ == "__main__":
    main()
