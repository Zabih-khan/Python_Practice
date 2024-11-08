class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def formula(self):
        return (self.a**2+self.b**2+2*self.a*self.b)
a = Equation(
    int(input("Enter the first number:")),
    int(input("Enter the second number:"))
    )
print (a.formula())
