class check:
    def __init__(self,number):
        self.num=number
    def prime(self):
        for i in range(2,int(self.num**1/2)):
            if self.num%1==0:
                return False
        
        return (True)
x=int(input("Enter Number:"))
obj=check(x)
print(obj.prime())


        
