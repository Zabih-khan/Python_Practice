class triangle:
    def __init__(self,b,h):
        self.b = b
        self.h = h

    def find_area(self):
        print(1/2*self.b*self.h)

x= int(input("Enter value for base."))
y = int(input("Enter value for height."))
obj = triangle(x,y)
obj.find_area()