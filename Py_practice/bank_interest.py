class bank:
    def __init__(self,p,A,n):
        self.p=p
        self.A=A
        self.n=n
    def bank_interest(self):
        i=self.A*(1+self.p/100)**self.n
        print("After n year Money growth is :" ,i)

p= int(input("Enter the bank interest per year:"))#in percent

A= int(input("Enter the initial amount:"))
    
n= int(input("Enter the years to find interest rate after n year:  "))

obj=bank(p,A,n)
obj.bank_interest()
