class Complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
        
    def add (self):
        addition=self.real+self.imaginary
        print(addition)

obj=Complex(2,3j)
obj.add()

        
        
