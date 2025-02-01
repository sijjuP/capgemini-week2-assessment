class BankAccount:
    def __init__(self):
        self.savings=0
    def deposit(self,money):
        self.savings+=money

    def withdraw(self,money):
        if(money>self.savings):
            print("\nInvalid process : overdraft\n")
        else:
            self.savings-=money
    def get_savings(self):
        print(f"\nsavings: \t{self.savings}")

account=BankAccount()
while True:
    ch=input("\nEnter 1 to view savings\nEnter 2 to deposit\nEnter 3 to withdraw\n1Enter any other key to exit\n")
    if ch=="1":
        account.get_savings()
    elif ch=="2":
        money=int(input("\nEnter the amount to deposit\t"))
        account.deposit(money)
    elif ch=="3":
        money=int(input("\nEnter the amount to withdraw\t"))
        account.withdraw(money)
    else:
        break