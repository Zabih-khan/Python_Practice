class company:
    def F_N(self,fname,lname):
        self.fname=fname
        self.lname=lname
        fullname=self.fname+self.lname
        self.full__name(fullname)
    def S(self,salary):
        adding=salary+1000
        self.your_salary(adding)
class derived1(company):
    def full__name(self,f):
        print("your full name is ",f)
class derived2(company):
    def your_salary(self,s):
        print("youe salary after increment is",s)
class derived3(derived1,derived2):
    print("you are the employee of HBL")
    
        
obj=derived3()
obj.F_N("zabih","ullah")
obj.S(2000)


