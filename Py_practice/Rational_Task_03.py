from fractions import Fraction

class Rational:
    def __init__(self,numerator,denominator):
        self.numerator=numerator
        self.denominator=denominator
    def Adding_R(self):
         x=self.numerator+self.denominator
         y=Fraction(x)
         print("\nThe addition of two rational number is:",x)
         print("a/b form is:")
         print ("%s = %s  " % (x,y))

         
    def Sub_R(self):
         x=self.numerator-self.denominator
         y=Fraction(x)
         print("\nThe subtrction of two rational number is:",x)
         print("a/b form is:")
         print ("%s= %s " % ( x,y))

    def Mul_R(self):
         x=self.numerator*self.denominator
         y=Fraction(x)
         print("\nThe Multiflication of two rational number is:",x)
         print("a/b form is:")
         print ("%s = %s  " % ( x,y))

    def Div_R(self):
         x=self.numerator/self.denominator
         y=Fraction(x)
         print("\nThe Division of two rational number is:",x)
         print("a/b form is:")
         print ("%s = %s " % ( x,y))

obj=Rational(1/5,5/10)
obj.Adding_R()
obj.Sub_R()
obj.Mul_R()
obj.Div_R()

