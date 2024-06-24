"""
    El Principio de Sustitución de Liskov (Liskov Substitution Principle, LSP) es uno de los principios SOLID del diseño de software orientado a objetos. Este principio establece que los objetos de una clase derivada deben poder sustituir a los objetos de la clase base sin alterar el comportamiento esperado del programa. En otras palabras, una clase derivada debe ser intercambiable por su clase base.

    Para ilustrar este principio en Python, supongamos que estamos trabajando con una jerarquía de clases para diferentes tipos de cuentas bancarias: Account, SavingsAccount, y CurrentAccount.
"""

"""
    Clase base Account
    Primero, definimos la clase base Account que contiene métodos comunes para depositar y retirar dinero:
"""

class Account:
    def __init__(self, balance: float):
        self._balance = balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount: float) -> None:
        if 0 < amount <= self._balance:
            self._balance -= amount

    def get_balance(self) -> float:
        return self._balance
    
    """
        Clases derivadas SavingsAccount y CurrentAccount
        Ahora, creamos dos clases derivadas: SavingsAccount y CurrentAccount.
    """

class SavingsAccount(Account):
    def __init__(self, balance: float, interest_rate: float):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def add_interest(self) -> None:
        self._balance += self._balance * self.interest_rate

class CurrentAccount(Account):
    def __init__(self, balance: float, overdraft_limit: float):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float) -> None:
        if 0 < amount <= self._balance + self.overdraft_limit:
            self._balance -= amount

"""
    Ejemplo de uso del principio LSP
    Con esta jerarquía de clases, podemos demostrar que las instancias de SavingsAccount y CurrentAccount pueden sustituir a Account sin problemas.
"""

def process_account(account: Account) -> None:
    account.deposit(100)
    account.withdraw(50)
    print(f"Balance after transactions: {account.get_balance()}")

# Usando una instancia de Account
account = Account(1000)
process_account(account)

# Usando una instancia de SavingsAccount
savings_account = SavingsAccount(1000, 0.05)
process_account(savings_account)
savings_account.add_interest()
print(f"Balance after adding interest: {savings_account.get_balance()}")

# Usando una instancia de CurrentAccount
current_account = CurrentAccount(1000, 500)
process_account(current_account)