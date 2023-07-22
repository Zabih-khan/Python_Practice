print("Enter the distance between two cities(in km) : ")
km = float(input())
m = km * 1000      # 1km = 1000m
feet = km * 3280.84  # 1km=3280.84feet
inch = km * 39370.1  #1 km=39370.1inches
cm = km * 100000   #1km = 100000cm
yard = km * 1093.61  # 1km=1093.61yard
print("\nDistance in Kilometres = ", km)
print("\nDistance in Metres = ", m)
print("\nDistance in Feet = ", feet)
print("\nDistance in Inches = ", inch)
print("\nDistance in Centimetres = ", cm)
print("\nDistance in Yards = ", yard)
