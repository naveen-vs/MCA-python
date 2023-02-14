class bank:
    def __init__(self):
        self.acc_no=int(input("enter the acc no :"))
        print("---------------------------------------------------")
        self.acc_name=str(input("enter the acc name :"))
        print("---------------------------------------------------")
        self.acc_type=str(input("enter the acc holder type s/c :"))
        print("---------------------------------------------------")
        self.acc_balance=0
    def deposit(self):
        amount=int(input("enter the amount to be deposited:"))
        print("---------------------------------------------------")
        self.acc_balance=self.acc_balance+amount
        print("balance:",self.acc_balance)
        print("---------------------------------------------------")
    def withdraw(self):
        amount=int(input("enter the amount to be withdrawn:"))
        print("---------------------------------------------------")
        if self.acc_balance>=amount:
            self.acc_balance=self.acc_balance-amount
            print("balance:",self.acc_balance)
            print("---------------------------------------------------")
        else:
            print("!!! insufficent balance !!!!")
            print("---------------------------------------------------")
obj=bank()
while(True):
    opt=int(input("enter your options:1.deposit 2.withdraw 3.exit \n \t :"))
    print("---------------------------------------------------")
    if opt==1:
        obj.deposit()
    elif opt==2:
        obj.withdraw()
    elif opt ==3:
        break
    else:
        print("Invalid Option !")