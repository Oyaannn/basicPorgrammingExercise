from banking import BankAccount, BankingSystem

def run():
    banking_system = BankingSystem()
    while True:
        print("|>> Welcome to Bank Emokk <<|")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            owner = input("Enter the name for the new account: ")
            banking_system.create_account(owner)
        elif choice == '2':
            account_number = int(input("Enter your account number: "))
            banking_system.deposit_money(account_number)
        elif choice == '3':
            account_number = int(input("Enter your account number: "))
            banking_system.withdraw_money(account_number)
        elif choice == '4':
            account_number = int(input("Enter your account number: "))
            banking_system.check_balance(account_number)
        elif choice == '5':
            print("=== Thank you:) ===")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    run()