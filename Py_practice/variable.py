class varaible:
    def __init__(self,name="XYZ",age=0):
        self.name=name
        self.age=age


    def print(self):
        print("Name:" ,self.name)
        print("Age:",self.age)



obj=varaible()
obj.print()

print()
obj1=varaible("zabih",4)
obj1.print()
