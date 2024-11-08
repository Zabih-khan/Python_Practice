class Class1:
    def m(self):
        print("in Class1")


class Class2(Class1):
    def m(self):
        print("in Class2")



class Class3(Class1):
    def m(self):
        print("in Class3")


class Class4(Class2,Class3):
    pass

obj=Class4()
obj.m()
