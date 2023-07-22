from math import pi
class Area:
    h = 5.0 # height
    b = 2.0 # base
    r = 1.5 # radius

    def Area_parallelogram(self):
        self.h=self.h
        self.b=self.b
        p=self.h*self.b
        print("\nArea_parallelogram is:",p)

    def Area_square(self):
        self.h=self.h
        self.b=self.b
        self.r=self.r
        p=self.h*self.h
        print("\nArea_square is:",p)

    def Area_circule(self):
        self.h=self.h
        self.b=self.b
        self.r=self.r
        p=pi*self.r**2
        print("\nArea_circule:",p)

    def Area_cone(self):
        self.h=self.h
        self.b=self.b
        self.r=self.r
        p=1.0/3*pi*self.r**2*self.h
        print("\nArea_cone:",p)



obj=Area()
obj.Area_parallelogram()
obj.Area_square()
obj.Area_circule()
obj.Area_cone()




