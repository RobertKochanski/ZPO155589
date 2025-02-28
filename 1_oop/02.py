# ========= Zadanie 2 =============
from collections import namedtuple

Transaction = namedtuple("Transaction", ["transaction_id", "amount", "currency"])

class BankAccount:
    balance: float

    def __init__(self, balance:float):
        self.balance = balance

    def apply_transaction(self, transaction: Transaction):
        self.balance += transaction.amount

bankAccount = BankAccount(100)
print(f"Before: {bankAccount.balance}")
bankAccount.apply_transaction(Transaction(1, 10, "PLN"))
print(f"After: {bankAccount.balance}")
