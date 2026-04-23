# Cree una función que se llame multiply, la cual obtiene dos valores y los multiplica entre si
# A esta función se le debe combinar dos decoradores:
# @log_call: imprime el nombre de la función, los argumentos, fecha actual y el retorno
# @validate_numbers: revisa que todos los argumentos sean numéricos

from datetime import datetime
from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args):
        result = func(*args)
        print(f"func: {func.__name__} - args: {args} - [{datetime.now()}] - Resultado: {result}")
        return result
    return wrapper


def validate_numbers(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError(f"El argumento '{arg}' no es un número")
        return func(*args)
    return wrapper


@log_call
@validate_numbers
def multiply(a,b):
    return a*b


if __name__ == "__main__":
    try:
        print(f"Resultado: {multiply(3,4)}")
        print(f"Resultado: {multiply(3,"4")}")
    except ValueError as e:
        print(e)
    try:
        print(f"Resultado: {multiply(3.5,10)}")
        print(f"Resultado: {multiply(3.5,'b')}")
    except ValueError as e:
        print(e)
