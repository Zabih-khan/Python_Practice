class company:
    def full(self,fname ,lname):
        fullname=fname+lname
        self.your_full_name(fullname);
    def salary(self, sal):
        adding1000=sal+1000
        self.your_salary(adding1000)
class derived1(company):
    def your_full_name(self,f):
        print('your full name is: \t',f)
class derived2(company):
    def your_salary(self,s):
        print("your salary after oncrement is:\t",s)
class derived3(derived1,derived2):
    print("you are employee of state bank of pakistan")
obj=derived3()
obj.full('Zabih','ullah')
obj.salary(20000)
