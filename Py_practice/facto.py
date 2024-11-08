class Fact:
    
    def factorial(self,n):
        self.n=n
    #n here should be an integer
        if self.n == 0:
            return 1
        else:
            return self.n*self.factorial(self.n-1)
        

x=Fact()
a=int(input("enter the number:"))
print(x.factorial(a))
