class Abasyn:
    def __init__(self,a):
        self.a=a
    def __mul__(self, other):
        return self.a * other.a

ob1=Abasyn(3)
ob2=Abasyn(2)
print("The Multiflication of two object is :",ob1*ob2)
