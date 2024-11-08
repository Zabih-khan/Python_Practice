class company:
    def Name(self,fname,lname):
        self.fname=fname
        self.lname=lname
        full_n=self.fname+self.lname
        self.Full_name(full_n)


    def Salary(self,sal):
        self.sal=sal+1000
        self.S(self.sal)

class derived1(company):
    def Full_name(self,f):
        print("your full name is ",f)

class derived2(company):
    def S(self,s):
        print("your salary after increment",s)


class derived3(derived1,derived2):
    print ("I am employee of HBL")


obj=derived3()
obj.Name("zabih","khan")
obj.Salary(2000)
