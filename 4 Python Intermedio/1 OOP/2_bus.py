# Cree una clase de Bus con:
# Un atributo de max_passengers.
# Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase Person 
# vista en la lección). Este solo debe agregar pasajeros si lleva menos de su máximo. 
# Sino, debe mostrar un mensaje de que el bus está lleno.
# Un método para bajar pasajeros uno por uno (en cualquier orden).

class Person():
	def __init__(self, name):
		self.name = name
            
            
class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []


    def get_on_the_bus(self, person):
        if len(self.passengers) >= self.max_passengers:
             print("El bus está lleno")
             return
        self.passengers.append(person)
        print(f"{person.name} subió al bus")

    
    def get_off_the_bus(self, name):
        for passenger in self.passengers:
             if passenger.name == name:
                self.passengers.remove(passenger)
                print(f"{name} bajó del bus")
                return
          
        print(f"{name} no subió al bus")


mx_bus = Bus(3)

person_1 = Person("Juan")
person_2 = Person("Pedro")
person_3 = Person("Jose")
person_4 = Person("Maria")
person_5 = Person("Luis")

mx_bus.get_on_the_bus(person_1)
mx_bus.get_on_the_bus(person_2)
mx_bus.get_on_the_bus(person_3)
mx_bus.get_on_the_bus(person_4)
mx_bus.get_on_the_bus(person_5)

mx_bus.get_off_the_bus("Jose")
mx_bus.get_off_the_bus("Juan")
mx_bus.get_off_the_bus("Maria")
mx_bus.get_off_the_bus("Luis")
mx_bus.get_off_the_bus("Pablo")
mx_bus.get_off_the_bus("Pedro")
mx_bus.get_off_the_bus("Michelle")
mx_bus.get_off_the_bus("Usuario Lyfter")
