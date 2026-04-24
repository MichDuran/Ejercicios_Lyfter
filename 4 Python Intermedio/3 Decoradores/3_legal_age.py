# Cree una clase de User que:
# Tenga un atributo de date_of_birth.
# Tenga un property de age.
# Luego cree un decorador para funciones que acepten un User como parámetro que se encargue
# de revisar si el User es mayor de edad y arroje una excepción de no ser así.

from datetime import datetime

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth
    
    @property
    def age(self):
        today = datetime.today()
        age = (
            today.year - self.date_of_birth.year 
            - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        )
        return age


def legal_age(func):
    def wrapper(user, *args, **kwargs):
        if user.age < 18:
            raise ValueError(f"El usuario de {user.age} años no es mayor de edad")
        return func(user, *args, **kwargs)
    return wrapper


@legal_age
def access(user):
    return f"Acceso permitido al usuario de {user.age} años"


if __name__ == "__main__":
    user1 = User(date_of_birth = datetime(1993, 5, 13))
    user2 = User(date_of_birth = datetime(2008, 5, 13))
    
    
    try:
        print(access(user1))
        print(access(user2))
    except ValueError as e:
        print(e)
        