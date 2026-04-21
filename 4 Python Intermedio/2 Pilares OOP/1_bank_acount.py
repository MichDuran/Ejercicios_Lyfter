# Cree una clase de BankAccount que:
# Tenga un atributo de balance.
# Tenga un método para ingresar dinero.
# Tengo un método para retirar dinero.
# Cree otra clase que herede de esta llamada SavingsAccount que:
# Tenga un atributo de min_balance que se pueda asignar al crearla.
# Arroje un error si al intentar retirar dinero, el retiro haría que el balance quede debajo del min_balance. 
# Es decir que sí se pueden hacer retiros siempre y cuando el balance quede arriba del min_balance.


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        
    def deposit(self, amount):
        if amount <= 0:
            print("El monto a depositar debe ser mayor que cero")
            return
        self.balance += amount
        print(f"Depósito exitoso. Nuevo balance: {self.balance}")
        
    def withdraw(self, amount):
        if amount <= 0:
            print("El monto a retirar debe ser mayor que cero")
            return
        if amount > self.balance:
            print("Fondos insuficientes para realizar el retiro")
            return
        self.balance -= amount
        print(f"Retiro exitoso. Nuevo balance: {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, balance=0, min_balance=0):
        super().__init__(balance)
        self.min_balance = min_balance
        
    def withdraw(self, amount):
        if amount <= 0:
            print("El monto a retirar debe ser mayor que cero")
            return
        if self.balance - amount < self.min_balance:
            print(f"Retiro no permitido. El balance no puede quedar por debajo de {self.min_balance}")
            return
        super().withdraw(amount)
        

if __name__ == "__main__":
    savings = SavingsAccount(balance=1000, min_balance=200)
    print(f"Balance inicial: {savings.balance} y mínimo requerido: {savings.min_balance}")
    savings.deposit(500)
    savings.withdraw(300)
    savings.withdraw(1200)
    savings.withdraw(100)
    print(f"Balance final: {savings.balance}")
