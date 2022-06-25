# Exercise week 04 - DevinHouse
# Simulate a bank account
from datetime import date

class Bank:
    def __init__(self, name, account, balance=0, limit=1000):
        self.account = account
        self.name = name
        self.balance = balance
        self.limit = limit
        self.transactions = []

    def deposit(self, amount):
        self.transactions.append(
            {
                "amount": amount,
                "date": date.today(),
                "balance": self.balance,
                "operation": "deposit",
            }
        )
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance + self.limit:
            print(
                f"WARNING - Insufficient funds - value of {amount} exceeds the limit of R${self.limit} + {self.balance} for withdrawals"
            )
            return False

        self.transactions.append(
            {
                "amount": amount,
                "date": date.today(),
                "balance": self.balance,
                "operation": "withdraw",
            }
        )
        self.balance -= amount
        return True

    def getExtract(self):
        print(f"Account:{self.account} - {self.name} has a balance of R${self.balance}")
        print("Transactions:")
        print("-" * 20)
        print("Date | Amount | Balance | Operation")
        for transaction in self.transactions:
            print(
                f"{transaction['date']} | R${transaction['amount']} | R${transaction['balance']} | {transaction['operation']}"
            )

    def transfer(self, amount, account):
        if amount > self.balance + self.limit:
            print(
                f"WARNING - Insufficient funds - value of {amount} exceeds the limit of R${self.limit} + {self.balance} for withdrawals"
            )
            return False

        self.transactions.append(
            {
                "amount": amount,
                "date": date.today(),
                "balance": self.balance,
                "operation": "transfer",
            }
        )
        self.balance -= amount
        account.deposit(amount)
        return print(f"Transfer of R${amount} to {account.name} was successful")

accounts = []

while True:
    # os.system('cls')
    print("-" * 20)
    print("Welcome to the newbank")
    print("-" * 20)
    choose_menu = input(
        """
        1 - Create a new accounts
        2 - Show all accounts
        3 - Show account details
        4 - Access account
        5 - Exit 
        Choose: """
    )

    if choose_menu == "1":
        name = input("Enter your name: ")
        account_number = input("Enter your account: ")
        accounts.append(Bank(name, int(account_number)))
        print(f"Account {account_number} created successfully")
    elif choose_menu == "2":
        for account_number in accounts:
            print(f"Account: {account_number.account} - {account_number.name}")
    elif choose_menu == "3":
        account_number = int(input("Enter your account: "))
        for account_ in accounts:
            if account_.account == account_number:
                account_.getExtract()
                continue

    elif choose_menu == "4":
        while True:
            accountNumber = int(input("Enter your account number or 0 for exit: "))
            if accountNumber == 0:
                break

            for account_ in accounts:
                if account_.account == account_number:
                    while True:
                        menuchoose = input(
                            """  
        1 - Deposit 
        2 - Withdraw
        3 - Transfer
        4 - Get extract
        5 - Exit """
                        )
                        if menuchoose == "1":
                            amount = int(input("Enter the amount to deposit: "))
                            account_.deposit(amount)
                            print(f"Deposit of R${amount} was successful")
                        elif menuchoose == "2":
                            amount = int(input("Enter the amount to withdraw: "))
                            account_.withdraw(amount)
                            print(f"Withdraw of R${amount} was successful")
                        elif menuchoose == "3":
                            amount = int(input("Enter the amount to transfer: "))
                            account_destiny = int(
                                input("Enter the account number to transfer: ")
                            )
                            for account_destiny_ in accounts:
                                if account_destiny_.account == account_destiny:
                                    account_.transfer(amount, account_destiny_)
                                    continue
                        
                        elif menuchoose == "4":
                            account_.getExtract()
                        elif menuchoose == "5":
                            break
