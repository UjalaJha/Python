class Bank:
    def __init__(self,name,accno=123,roi=4,balance=0.0):
        self.balance = balance
        self.name=name
        self.accno=accno
        self.interest=0.0
        
    def withdraw(self, amount):
        if amount>self.balance:
            print("No balance in account")
            return
        else:
            self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def computeinterest(self, amount,year,roi):
        self.interest=amount*year*roi*0.01
        return self.interest


name=input("Enter name : ")
accno=input("enter acc no : ")
b=Bank(name,accno)

while(True):
    print('\nd -Deposit w -Withdraw r -rate of interest')
    choice=input('Enter Choice : ')
    amt=float(input('Enter Amount : '))

    if choice=='d':
            print('Balance after deposit: ',b.deposit(amt))
    elif choice=='w':
            print('Balance after withdrawal: ',b.withdraw(amt))
    elif choice=='r':
            roi=8
            year=float(input("enter year : "))
            print('ROI: ',b.computeinterest(amt,year,roi))
