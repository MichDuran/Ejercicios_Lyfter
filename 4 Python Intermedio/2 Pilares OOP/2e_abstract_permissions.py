# Cree una clase abstracta User con los siguientes métodos abstractos:
# get_role()
# has_permission(permission)
# Luego cree dos clases que hereden de ella:
# AdminUser
# RegularUser
# Cada una debe implementar los métodos
# Por ejemplo:
# AdminUser siempre tiene permisos
# RegularUser solo tiene permisos limitados ("read", por ejemplo)

from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self, permission):
        pass


class AdminUser(User):
    def get_role(self):
        return "Admin"
    
    def has_permission(self, permission):
        return True


class RegularUser(User):
    def get_role(self):
        return "Regular"
    
    def has_permission(self, permission):
        return permission == "read"
    
    
if __name__ == "__main__":
    user1 = AdminUser("Carlos")
    user2 = RegularUser("Andrea")
    
    print(f"Rol del admin: {user1.get_role()}")
    print(f"Rol del usuario regular: {user2.get_role()}")
    
    print(f"Admin write: {user1.has_permission('write')}")
    print(f"Admin delete: {user1.has_permission('delete')}")
    print(f"Regular write: {user2.has_permission('write')}")
    print(f"Regular read: {user2.has_permission('read')}")
    print(f"Regular delete: {user2.has_permission('delete')}")
