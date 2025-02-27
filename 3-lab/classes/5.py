# 5. Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
#class Account:
#    pass

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

owner = input("Введите имя владельца счета: ")
initial_balance = int(input("Введите начальный баланс: "))

acc = Account(owner, initial_balance)

while True:
    print("\nВыберите действие:")
    print("1. Внести деньги")
    print("2. Снять деньги")
    print("3. Проверить баланс")
    print("4. Выйти")
    
    choice = input("Введите номер действия: ")
    
    if choice == "1":
        amount = int(input("Введите сумму депозита: "))
        acc.deposit(amount)
    elif choice == "2":
        amount = int(input("Введите сумму для снятия: "))
        acc.withdraw(amount)
    elif choice == "3":
        print(f"Текущий баланс: {acc.balance}")
    elif choice == "4":
        print("Выход из программы. Спасибо!")
        break
    else:
        print("Некорректный ввод. Попробуйте снова.")