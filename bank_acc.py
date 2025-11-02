class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float):
        self.holder = account_holder
        self.balance = initial_balance
        
    def transfer_funds(self, other_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            other_account.balance += amount
            print('transfer succeeded')
        else:
            print('transfer error')
    
    def __str__(self):
        return f'{self.holder}, {self.balance}'
    
b1 = BankAccount('gad', 10.0)
b2 = BankAccount('dag', 100.5)

b1.transfer_funds(b2, 9.4)

print(b1, b2)