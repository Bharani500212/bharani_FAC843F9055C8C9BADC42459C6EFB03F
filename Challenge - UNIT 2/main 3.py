#BANK ACCOUNT
class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = initial_balance
    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited {amount}. New balance: {self._account_balance}")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")
    def withdraw(self, amount):
        if amount > 0 and amount <= self._account_balance:
            self._account_balance -= amount
            print(f"Withdraw {amount}. New balance: {self._account_balance}")
        else:
            print("Invalid withdraw amount or insufficient balance.")
account = BankAccount("300304", "HARISH", 1000.0)
account.deposit(500)
account.withdraw(200)