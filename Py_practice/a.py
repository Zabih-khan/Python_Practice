from math import *
h = int(input("Enter the value of height:"))	# height
b = int(input("Enter the value of base:"))	# base
r = int(input("Enter the value of radius:"))	# radius
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

area_parallelogram = h*b
print ("The area of the parallelogram is %.3f" % area_parallelogram)

print("--------------------------------")

area_square = b**2
print ("The area of the square is %g" % area_square)

print("--------------------------------")

area_circle = pi*r**2
print ("The area of the circle is %.3f" % area_circle)

print("--------------------------------")

volume_cone = 1.0/3*pi*r**2*h
print ("The volume of the cone is %.3f" % volume_cone)
print("--------------------------------")
