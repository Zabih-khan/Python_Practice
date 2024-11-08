class Employee:
    def __init__(self,name,age,salary,destination):
        self.name=name
        self.age=age
        self.salary=salary
        self.destination=destination

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Salary:",self.salary)
        print("Destination:",self.destination)


obj=Employee("Zabih",19,25000,"software engineer")
obj.display()
