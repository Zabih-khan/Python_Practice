class calculator1:
    def addition(self,a,b):
        print("Addition=",a+b)


class calculator2:
    def Multiflication(self,a,b):
        print("multiflication=",a*b)

class calculator3(calculator1,calculator2):
    def Division(self,a,b):
        print("Division=",a/b)

d=calculator3()

d.addition(12,3)
d.Multiflication(12,3)
d.Division(12,3)
