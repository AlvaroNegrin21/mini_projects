"""
BankAccount class: a simple bank account that supports
deposits, withdrawals, balance checks, and transaction history.
"""

class BankAccount:
    """Represents a simple bank account with a balance and transaction history."""

    def __init__(self, owner, balance=0):
        """Initializes a new bank account.

        Args:
            owner (str): name of the account owner.
            balance (float): initial balance. Defaults to 0.
        """
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        """Deposits an amount into the account and logs the transaction.

        Args:
            amount (float): amount to deposit.
        """
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}€")
        print(f"Deposit of {amount}€. Current balance: {self.balance}€")

    def withdraw(self, amount):
        """Withdraws an amount from the account if there are sufficient funds.

        Args:
            amount (float): amount to withdraw.
        """
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew: {amount}€")
            print(f"Withdrawal of {amount}€. Current balance: {self.balance}€")
    
    def get_balance(self):
        """Prints the current account balance."""
        print(f"Current balance: {self.balance}€")
    
    def transaction_history(self):
        """Prints the full transaction history, or a message if there are none."""
        print("Transaction history:")
        if len(self.transactions) > 0:
            for transaction in self.transactions:
                print(transaction)
        else:
            print("No transactions to show.")