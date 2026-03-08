class BankAccount:
    def __init__(self, name, bal):
        self.account_holder = name
        self.__balance = bal

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Rs. {amount} is deposited.")
            print(f"Current Balance: Rs. {self.__balance}")
        else:
            print("Amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print(f"This amount is not withdrawable.")
        elif amount <= self.__balance:
            self.__balance -= amount
            print(f"Rs. {amount} is withdrawn.")
            print(f"Current Balance: Rs. {self.__balance}")
        else:
            print("Insufficient balance")
    
    def show_balance(self):
        print(f"Your balance is Rs. {self.__balance}.\n")

name = input("Enter Name: ").strip()
while True:
    try:
        balance = int(input("Enter your Initial Balance: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if balance > 0:
        acc = BankAccount(name, balance)
        break
    else:
        print("Initail balance must be positive.")
        continue

while True:
    print("1 Deposit")
    print("2 Withdraw")
    print("3 Check Balance")
    print("4 Exit\n")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        amount = int(input("Enter Amount: "))
        acc.deposit(amount)

    elif choice == "2":
        amount = int(input("Enter Amount: "))
        acc.withdraw(amount)

    elif choice == "3":
        acc.show_balance()

    elif choice == "4":
        print("Thank you,", name)
        break
    
    else:
        print("Please choose right option.")
        continue