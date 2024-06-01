class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be correct.")
        self.balance += amount
        print(f"Deposit successful. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be correct.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        print(f"Withdrawal successful. New balance: ${self.balance:.2f}")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")               

class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, owner):
        account_number = len(self.accounts) + 1
        self.accounts[account_number] = BankAccount(account_number, owner)
        print(f"Account created successfully. Account number: {account_number}")

    def deposit_money(self, account_number):
        try:
            self.accounts[account_number].deposit(float(input("Enter the amount to deposit: ")))
        except KeyError:
            print("Account Not Found.")
        except ValueError as e:
            print(e)

    def withdraw_money(self, account_number):
        try:
            self.accounts[account_number].withdraw(float(input("Enter the amount to withdraw: ")))
        except KeyError:
            print("Account Not Found.")
        except ValueError as e:
            print(e)

    def check_balance(self, account_number):
        try:
            self.accounts[account_number].check_balance()
        except KeyError:
            print("Account Not Found.")