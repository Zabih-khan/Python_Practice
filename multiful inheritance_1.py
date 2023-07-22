class detail:
    def __init__(self):
        self.id=None
    def setid(self):
        self.id=int(input("Enter id :"))
    def showid(self):
        print("id:",self.id)

        
        
class detai2(detail):
    def __init__(self):
        self.name=''
    def setname(self):
        self.setid()
        self.name=input("Enter Name:")
    def showname(self):
        self.showid()
        print("Name",self.name)

        
        
class detai3(detai2):
    def __init__(self):
        self.gender=''
    def setgender(self):
        self.setname()
        self.gender=input("Enter Gender:")
    def showgender(self):
        self.showname()
        print("Gender",self.gender)
        

        
class Employee(detai3):
    def __init__(self):
        self.desig=''
        self.depart=''
    def setemployee(self):
        self.setgender()
        self.desig=input("Enter designation:")
        self.depart=input("Enter Department:")
    def showemployee(self):
        self.showgender()
        print("Designation:",self.desig)
        print("Department:",self.depart)


obj=Employee()
obj.setemployee()
obj.showemployee()
















