class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount}원이 입금되었습니다.")
        self.report()
        
    def withdraw(self, amount):
        if self.balance < amount:
            print("잔고가 부족합니다.")
        else:
            print(f"{amount}원이 출금되었습니다.")
            self.balance -= amount
        self.report()
        
    def report(self):
        print(f"현재 잔고는 {self.balance} 입니다.")
        
    def __str__(self):
        return f"잔고 = {self.balance}"
        
a = BankAccount()
a.deposit(100)
a.withdraw(10)
print(a)