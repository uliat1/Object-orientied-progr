class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств")
        else:
            self.balance -= amount
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, name, balance=0, interest_rate=0.01):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate

# Создаем новый банковский счет
account = BankAccount("Иван", 1000)
print(account.balance)

# Делаем депозит
account.deposit(500)
print(account.balance)

# Делаем снятие
account.withdraw(200)
print(account.balance)

# Создаем новый сберегательный счет
savings = SavingsAccount("Иван", 1000)
print(savings.calculate_interest())
