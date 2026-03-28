# Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.

def function1():
    print("Esta es la primera función")
    function2()


def function2():
    print("Esta es la segunda función")


if __name__ == "__main__":
    function1()
