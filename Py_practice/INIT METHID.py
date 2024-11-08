class Rectangle:
   def __init__(self, length, breadth, unit_cost=0):
       self.length = length
       self.breadth = breadth
       self.unit_cost = unit_cost
   def get_area(self):
       return self.length * self.breadth
   def calculate_cost(self):
       area = self.get_area()
       return area * self.unit_cost
# breadth = 120 units, length = 160 units, 1 sq unit cost = Rs 2000
r = Rectangle(int(input("enter the length:")),
              int(input("enter the breadth:")),
              int(input("enter the unit_cost:"))
    )
print("Area of Rectangle: %s sq units" % (r.get_area()))
