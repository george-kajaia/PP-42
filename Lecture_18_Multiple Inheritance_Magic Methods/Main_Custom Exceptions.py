from datetime import datetime

class BankingError(Exception):
    """Base class for all banking-related errors."""
    def __init__(self, message, account_id=None):
        super().__init__(message)
        self.account_id = account_id 
        self.timestamp = datetime.time

class InsufficientFundsError(BankingError):
    def __init__(self, message, account_id, current_balance, attempted_amount):
        super().__init__(message, account_id)
        self.current_balance = current_balance
        self.attempted_amount = attempted_amount
 
    def __str__(self):
        return f"{super().__str__()} | "f"Balance: ${self.current_balance:.2f} | "f"Attempted: ${self.attempted_amount:.2f}"


class PositiveNumber:
    def __init__(self, name):
        self.name = name
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"{self.name} cannot be negative")
        setattr(instance, self.private_name, value) # დაუყენე instance ობიექტის self.private_name პარამეტრს მნიშვნელობა value

class BankAccount:
    balance = PositiveNumber("balance") # Descriptor guards the attribute
    credit_limit = PositiveNumber("credit_limit")

    def __init__(self, account_id, balance=0, credit_limit=1000):
        self.account_id = account_id
        self.balance = balance
        self.credit_limit = credit_limit
 
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Cannot withdraw more than available balance", account_id=self.account_id, current_balance=self.balance, attempted_amount=amount)
        self.balance -= amount
        return self.balance

try:
    acc = BankAccount("ACC-001", balance=100)
    print(acc.withdraw(250))
except InsufficientFundsError as e:
    print(e)
except BankingError as e:
    print("General banking error:", e) # Broad catch