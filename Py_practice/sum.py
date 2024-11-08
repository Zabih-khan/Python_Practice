class Sum:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def value(self):
        self.c=self.a+self.b
        print("Addition is:",self.c)


class derived(Sum):
    def average(self):
        self.x=self.c/2
        print( "The average of the number:",self.x)


class derived2(derived):
    def add_2(self):
        y=self.x+2
        print("After adding 2 with average is:",y)


obj=derived2(2,4)
obj.value()
obj.average()
obj.add_2()

        
        
    
