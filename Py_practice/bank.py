class Bankaccount:               
    def __init__(self,name,age,address,gender):
        self.name=name
        self.age=age
        self.address=address
        self.gender=gender
        self.balance=0
    def detail(self):
        print("")
        print("Personal detail:")
        print("Name :",self.name)
        print("Age :",self.age)
        print("Address :",self.address)
        print("Gender :",self.gender)


    def withdraw(self,amount):
        self.balance-=amount
        return (self.balance)

    def deposit( self,amount):
         self.balance+=amount
         return  self.balance

name=str(input("Enter your name:"))
age=int(input("Enter your age:"))
address=str(input("Enter your address:"))
gender=str(input("Enter your gender:"))


a= Bankaccount(name,age,address,gender)
a.detail()

print()
x=int(input("Enter the amount that you want to deposit:"))
a.deposit(x)
print()
y=int(input("Enter the amount that you want to withdraw:"))
a.withdraw(y)

print("The remain balance in your account is :",a.balance)
