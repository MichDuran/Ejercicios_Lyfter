# Cree un decorador @requires_login que:
# Verifique si la variable global user_logged_in es True
# Si no lo es, debe lanzar una excepción "Usuario no autenticado"
# Si lo es, la función decorada se ejecuta normalmente

user_logged_in = False

def requires_login(func):
    def wrapper(*args, **kwargs):
        if not user_logged_in:
            raise ValueError("Usuario no autenticado")
        return func(*args, **kwargs)
    return wrapper


@requires_login
def view_profile():
    print("Mostrando perfil del usuario")
    
    
if __name__ == "__main__":
    try:
        view_profile()
    except ValueError as e:
        print(e)
    
    user_logged_in = True
    try:
        view_profile()
    except ValueError as e:
        print(e)
