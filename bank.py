class BankAccount:
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print('insufficient funds:charging a $5 fee')
            self.balance -= 5
            return self
        
    def display_account_info(self):
        print(f"balance: {self.balance}")
        return self

        def yield_interest(self):
            if self.balance > 0:
                self.balance += (self.balance * self.int_rate)
            return self

savings = BankAccount(.05,1000)
checking = BankAccount(.02,5000)

savings.deposit(10).deposit(22).deposit(39).withdraw(400).yield_interest().display_account_info()
checking.deposit(200).deposit(82).deposit(500).withdraw(30).yield_interest().display_account_info()
