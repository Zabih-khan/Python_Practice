class company:
    def name (self,fname,lname):
        fullname=fname+lname
        self.your_full_name(fullname);
    def salary(self,salary):
        adding1000=salary+1000
        self.your_salary(adding1000)
class derived1(company):
    def your_full_name(self,f):
        print("Your full name is:",f)
class derived2(company):
    def your_salary(self,s):
        print("your salary after the increment is:",s)
class derived3(derived1,derived2):
    print("you are employee of state bank of pakistan")
obj=derived3()
obj.name('Zabih','ullah')
obj.salary(20000)
