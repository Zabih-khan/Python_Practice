class home:
    var=12
    def A(self):
        print("This is a home")   
class rome1(home):
    def B(self):
        print("i am livivng in room1") 
class rome2(rome1):
    def C(self):
        print("i am livivng in room1")
class rome3(rome2):
    def D(self):
        print("i am livivng in room1")
class rome4(rome3):
    def E(self):
        print("i am livivng in room1")
class rome5(rome4):
    def F(self):
        print("i am livivng in room1")


obj=rome5()
obj.A()
obj.B()
obj.C()
obj.D()
obj.E()
obj.F()
print(rome5.var)



