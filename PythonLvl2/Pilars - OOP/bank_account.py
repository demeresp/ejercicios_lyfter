class BankAccount:
    def __init__(self, balance):
        self.balance = balance


    def add_money(self, amount):
        self.balance -= amount

    
    def take_money(self, amount):
        self.balance += amount



class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance

    
    def take_money(self, amount):
        if self.balance - amount < self.min_balance:
            raise ValueError("No sufficent founds to create this savings account, please work")




account = SavingsAccount(1000, 2000)
account.take_money(2000)
