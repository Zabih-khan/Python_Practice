class check:
    def __init__(self,num):
        self.num=num

    def prime(self):
        for i in range(2,int (self.num**1/2)):

            #if any number is divisible by i
            #Then number is not prime no
            #so return false
            
            if self.num%i==0:
                return False
        return True

x= 'y'
while x=='y':
    a=int(input("enter the no:"))
    obj=check(a)
    print(obj.prime())
    x=input("Another number? y/n")

    


    
