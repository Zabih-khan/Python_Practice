class person:
    
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def detail(self):
        print(self.name,self.idnumber)
class Employee(person):
    
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self,name,idnumber)

        
obj=Employee("zabih",18381,2200,"web developer")

obj.detail()
