class student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollo=rollno
        self.marks=marks

    def get_roll(self):
        return rollno

    def get_marks(self):
        return marks
    def __str__(self):
        return self.name+ ':' +str(self.get_roll())+':' +str(self.get_marks())
    
#Define a fuction for building a record
#which generate list of all the student


def Marks(Record,name,rollno,marks):
    Record.append(obj)
    return Record
#Main code:
Record=[]
x='y'
while x=='y':
    name=input("Enter the name:")
    rollno=int(input("Enter Roll No"))
    marks= int(input("Enter marks"))
    obj=student(name,rollno,marks)#This is object of the class student;
    
    R=Marks(Record,name,rollno,marks)
    x=input("Another student?y/n")


n=1
for i in R:
    print(n,".",i)
    n=n+1











    

    
