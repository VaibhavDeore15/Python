"""Q.4)Bank Account Simulation
Create a class BankAccount with deposit, withdraw, and check balance functionalities.
Prevent withdrawal if balance is insufficient."""

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance. Withdrawal denied.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. Remaining balance: ₹{self.balance}")

    def check_balance(self):
        print(f"Current balance: ₹{self.balance}")


account = BankAccount("Vaibhav", 1000)

account.check_balance()
account.deposit(500)

account.withdraw(300)

account.withdraw(2000)

account.check_balance()
