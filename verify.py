#Verify these equations:
#(a + b)2= a2+ 2ab + b2

class verify:
    a=3
    b=4
    def equation(self):
        self.a=self.a
        self.a=self.b
        eq1_sum = self.a**2 + 2*(self.a*self.b) + self.b**2
        eq1_pow = (self.a + self.b)**2
        print ('Equation verified: %g = %g' % (eq1_sum, eq1_pow))
        


obj=verify()
obj.equation()
