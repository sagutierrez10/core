class BankAccount:
    def __init__ (self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else: 
            self.balance -= 5
            print("Insufficient Funds")
        return self
    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True
    def display_account_info(self):
        print("Balance $", self.balance)
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.int_rate * self.balance
            return self

Account1= BankAccount(0.05, 100)
Account2= BankAccount(0.09, 200)
Account1.deposit(10).deposit(20).deposit(40).withdraw(3).yield_interest().display_account_info()

Account2.deposit(25).deposit(38).withdraw(10).withdraw(23).withdraw(15).withdraw(5).yield_interest().display_account_info()


