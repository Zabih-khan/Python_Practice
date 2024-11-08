class student:
    
    def getstudent(self):
        self.name=input("Enter the name:")
        self.age=int(input("Enter the age:"))
        self.genter=str(input("Enter the genter:"))

class Test(student):
    
    def getmarks(self):
        self.s=int(input("Enter the class"))
        self.s1=int(input("Marks in english:"))
        self.s2=int(input("Marks in islamyat:"))
        self.s3=int(input("Marks in programming:"))
        self.s4=int(input("Marks in computing:"))
        self.s5=int(input("Marks in calculas:"))
        self.t=self.s1+self.s2+self.s3+self.s4+self.s5
        print("~~~~~~~~~~~~~~~~~~~~~~")
        

class Marks(Test):
    def display(self):
        print("\nName is :",self.name)
        print("\nAge is :",self.age)
        print("\nGenter is :",self.genter)
        print("\nTotal marks:",self.t)

        self.gpa= input("\nGPA is :")

obj=Marks()
obj.getstudent()
obj.getmarks()
obj.display()

