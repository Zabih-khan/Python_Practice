class person :
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

class Employee(person):
    def __init__(self,name,idnumber,salary,destination):
        self.salary=salary
        self.destination=destination
        
        person.__init__(self,name,idnumber)

obj=Employee('Rahul', 886012, 200000, "Intern")
obj.display()
    
