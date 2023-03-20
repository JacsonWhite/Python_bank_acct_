class Bankaccount:
    accounts = []
    def __init__(self, int_rate, balance):
        self.account_type = "Checking"
        self.int_rate = int_rate
        self.balance = balance
        Bankaccount.accounts.append(self)
    
    
    
    def deposit(self, amount):
        self.balance += amount
        print(f'You Now have ${self.balance}')
        return self

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print('not enough funds: charging a $5 fee')
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f'Balance is ${self.balance}')
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

savings = Bankaccount(.05, 2500)
checking = Bankaccount(.025, 5000)

savings.deposit(500).deposit(250).deposit(100).withdraw(300).yield_interest().display_account_info()
checking.deposit(400).deposit(550).deposit(100).withdraw(300).yield_interest().display_account_info()

Bankaccount.print_all_accounts()