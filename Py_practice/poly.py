from math import pi

class Rectangle:
   def __init__(self, length, breadth):
      self.l = length
      self.b = breadth
   def perimeter(self):
      return 2*(self.l + self.b)
   def area(self):
      return self.l * self.b

class Circle:
   def __init__(self, radius):
      self.r = radius
   def perimeter(self):
      return 2 * pi * self.r
   def area(self):
      return pi * self.r ** 2

# Initialize the classes
rec = Rectangle(5,3)
cr = Circle(4)
print("Perimter of rectangel: ",rec.perimeter())
print("Area of rectangel: ",rec.area())

print("Perimter of Circle: ",cr.perimeter())
print("Area of Circle: ",cr.area())
