class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Fondos insuficientes: Intentaste retirar {amount}, pero solo tienes {balance} disponible.")

try:
    balance = 100
    amount_to_withdraw = 150
    if amount_to_withdraw > balance:
        raise InsufficientFundsError(balance, amount_to_withdraw)
except InsufficientFundsError as e:
    print(f"Error detectado: {e}")