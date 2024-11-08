class company:
    def Add(self,a,b):
        self.a=a
        self.b=b
        addition=self.a+self.b
        self.full__name(addition)
    def mul(self,a,b):
        self.a=a
        self.b=b
        multiflication=self.a*self.b
        self.your_salary(multiflication)
class derived1(company):
    def full__name(self,f):
        self.x=f
        print("Addition of two number is : ",f)
class derived2(company):
    def your_salary(self,s):
        self.y=s
        print("Multiflication of two number is:",s)
class derived3(derived1,derived2):
    print("Addition and Multiflication")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    
        
obj=derived3()
obj.Add(12,2)
obj.mul(2,3)



