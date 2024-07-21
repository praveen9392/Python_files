class BankAccount:
    def __init__(self,accountno,name,ifsc,balance) :
        self.accountno=accountno
        self.name=name
        self.ifsc=ifsc
        self.balance=balance
    def withdrawl(self,amount):
        self.balance -= amount
        print("Balance amount=",self.balance)
    def deposit(self,amount):
        self.balance +=amount
        print("Total ammount=",self.balance)
    def checkbalance(self):
        print(self.balance)

obj1=BankAccount(12345678,'hari','2f3ywr456',1000)
#obj1.withdrawl(200)
obj1.deposit(500)

"""obj1.checkbalance()
obj1.withdrawl(200)
obj1.checkbalance()
obj1.deposit(250)
obj1.checkbalance()
"""