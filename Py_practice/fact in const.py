class factorial:
    num = int(input("Enter a number: "))

    def __init__(self,num,factorial):
        self.a=self.num
        self.factorial=self.factorial
    def fac(self):
        factorial=1
        if self.num <0:
            print("factorial of zero does not exist")
        elif self.num==0:
            print("the factorial of 0 is 1")
        else:
            for i in range(1,self.num+1):   
                factorial=self.factorial*1
            print("The factorial of",self.num,"is",self.factorial)
    


obj=factorial(2,4)
obj.fac()
