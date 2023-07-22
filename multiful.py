class detail_l:
    def __init__(self):
        self.Name=''
    def set_name(self):
        self.name=input("Enter Name:")
    def get_name(self):
        print('Name:',self.name)
        
class detail_2(detail_l):
    def __init__(self):
        self.RollNo=''
    def set_Roll(self):
        self.set_name()
        self.RollNo=input("Enter RollNo:")
    def get_Roll(self):
        self.get_name()
        print('RollNo:',self.RollNo)
    
class detail_3(detail_2):
    def __init__(self):
        self.Class=''
    def set_Class(self):
        self.set_Roll()
        self.Class=input("Enter Class:")
    def get_Class(self):
        self.get_Roll()
        print('Class:',self.Class)
    
class detail_4(detail_3):
    def __init__(self):
        self.Adress=''
    def set_Adress(self):
        self.set_Class()
        self.Adress=input("Enter Adress:")
        
    def get_Adress(self):
        self.get_Class()
        print('Adress:',self.Adress)
        

class TotalGPA(detail_4):
    def __init__(self):
        self.gpa=''
    def set_GPA(self):
        self.set_Adress()
        self.gpa=float(input('Enter GPA:'))

    def get_GPA(self):
        self.get_Adress()
        print('GPA',self.gpa)
        
        if self.gpa == 4  :
            print( 'Outstanding GPA')
        
        elif self.gpa==3:
            print("Excelence GPA")

        elif self.gpa==2:
            print('Not good GPA')
        
        elif self.gpa==1:
            print('fail')

       
        


obj=TotalGPA()
obj.set_GPA()
obj.get_GPA()


    
    


##class student(detail_4):
##    def __init__(self):
##        self.Marks=''
##    def set_Marks(self):
##        self.set_Adress()
##        self.Marks=input("Enter Marks:")
##    def get_Marks(self):
##        self.get_Adress()
##        print('Marks:',self.Marks)
##        
##
##
##obj=student()
##obj.set_Marks()
##obj.get_Marks()
##










    
