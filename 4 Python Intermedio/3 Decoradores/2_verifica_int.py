# Cree un decorador que se encargue de revisar si todos los parámetros de 
# la función que decore son números, y arroje una excepción de no ser así.

def verify_int(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError(f"El parámetro ingresado '{arg}' no es un número entero")
        for key, value in kwargs.items():
            if not isinstance(value, int):
                raise ValueError(f"El parámetro {key}={value} no es un número entero")
        return func(*args, **kwargs)
    return wrapper
        

@verify_int
def add(a,b,c,d,e):
    return a+b+c+d+e


if __name__ == "__main__":
    try:
        add(5, 10, 15, 20, 25)
        add("1", 2, 3, d=4, e=5)
    except ValueError as e:
        print(e)
    try:
        add(12, 9, c=3, d=6, e=13)
        add(1, 2, 3, d=4, e=5.2)
    except ValueError as e:
        print(e)
    try:
        add(a=3, b=4, c=5, d=6, e=7)
        add(1, 2, 3, d=4, e="e")
    except ValueError as e:
        print(e)
