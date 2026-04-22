# Cree un decorador que haga print de los parámetros y retorno de la función que decore.

def print_params(func):
    def wrapper(*args, **kwargs):
        print(f"Parámetros: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Retorno: {result}")
        return result
    return wrapper


@print_params
def add(a, b, c, d, e):
    return a+b+c+d+e

if __name__ == "__main__":
    add(5, 10, 15, 20, 25)
    add(a=3, b=4, c=5, d=6, e=7)
    add(12, 9, c=3, d=6, e=13)
