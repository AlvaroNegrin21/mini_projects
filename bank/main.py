"""
Simple Bank
------------
Lets the user create a single bank account and perform deposits,
withdrawals, balance checks, and view the transaction history.
"""

from account import BankAccount

while True:
    print("\n === Bank ===")
    print("""
    1. Create account
    2. Deposit
    3. Withdraw
    4. View balance
    5. View history
    6. Exit""")
    
    option = int(input("\nChoose an option: "))
    
    if option == 1:
        if 'account' in locals():
            print("You already have an account created.")
        else:
            name = input("Owner's name: ")
            account = BankAccount(name)
            print(f"Account created for {account.owner} with an initial balance of {account.balance}€")
        input("\nPress Enter to continue...")
    
    elif option == 2: 
        if 'account' in locals():
            amount = float(input("Amount to deposit: "))
            account.deposit(amount)
        else:
            print("You need to create an account first.")
        input("\nPress Enter to continue...")
    
    elif option == 3:
        if 'account' in locals():
            amount = float(input("Amount to withdraw: "))
            account.withdraw(amount)
        else:
            print("You need to create an account first.")
        input("\nPress Enter to continue...")
    
    elif option == 4:
        if 'account' in locals():
            account.get_balance()
        else:
            print("You need to create an account first.")
        input("\nPress Enter to continue...")
    
    elif option == 5:
        if 'account' in locals():
            account.transaction_history()
        else:
            print("You need to create an account first.")
        input("\nPress Enter to continue...")
        
    elif option == 6:
        print("Thanks for using this Bank. Goodbye")
        break