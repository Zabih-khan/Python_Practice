class Factorial: 
    num = int(input("Enter a number: "))
    factorial=1
    def fact(self,):
        self.a=self.num
        self.factorial=self.factorial
        if self.a < 0:
            print(" Factorial does not exist for negative numbers")
        elif self.a == 0:    
            print("The factorial of 0 is 1") 
        else:
            for i in range(1,self.a + 1):      
                self.factorial = self.factorial*i          
                print("The factorial of",self.a,"is",self.factorial) 

obj=Factorial()
obj.fact()
        
    
