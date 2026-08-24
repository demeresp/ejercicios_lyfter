class BankAccount:
    def __init__(self, balance):
        self.balance = balance


    def add_money(self, amount):
        self.balance += amount

    
    def take_money(self, amount):
        self.balance -= amount



class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance


    def take_money(self, amount):
        result = self.balance - amount
        if result < self.min_balance:
            raise ValueError("Insuffiecient founds to proceed!")
        self.balance = result
        return self.balance




account = SavingsAccount(10000, 2000)
after_saving = account.take_money(2000)
print("Remaining balance is:", after_saving)