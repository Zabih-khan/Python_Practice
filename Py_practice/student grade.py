class student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        
        
    def subject_marks(self):
        self.english=int(input("Enter Marks:"))
        self.urdu=int(input("Enter Marks:"))
        self.algebra=int(input("Enter Marks:"))
        self.islamyat=int(input("Enter Marks:"))
        self.pakstudy=int(input("Enter Marks:"))
        
    def per(self):
        self.total=(self.english+self.urdu+self.algebra+self.islamyat+self.pakstudy)
        self.percentage=round(self.total/6,0)
        print("Percentage:",self.percentage)

    def grade(self):
        if self.percentage>=85 or self.percentage<=100:
            print("Grade :A")
        elif self.percentage>=50 or self.percentage<=84:
            print("Grade :A")
        else:
            print("Not found")
            
    def print(self):
        print("Name:",self.name,"\nRoll_No:",self.roll_no)
        print()
        self.subject_marks()
        print()
        self.per()
        self.grade()

        
obj=student("zabih",18381)
obj.print()        
