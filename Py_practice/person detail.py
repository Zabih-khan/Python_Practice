class person:
    def __init__(self,list):
        self.Rollnolist=list
##        self.studentlist=list1
        self.Dict={}
        

    def displayroll(self):
        print("we have the following student Roll No list please select rollno to show detail")
        for roll in self.Rollnolist:
            print(roll)
    def addstudent(self,list1):
        self.studentlist=list1
        self.studentlist.append(student)
        print("Student has been added :")
        
obj=person(["1821","18381"])

if __name__=='__main__':

    while(True):

        print("=====Welcome=====")
        print("1:Display roll number:")
        print("2:Display Student name:")

        
        user_choice=input()
        if user_choice not in ['1','2']:
            print("please enter the valid option")
        else:
            user_choice=int(user_choice)
        if user_choice==1:
            obj.displayroll()

        elif user_choice==3:
            lsit1 = input("Enter the name of the student you want to add:")
            obj.addstudent(list1)


       
        print("press q to quit and c to continue")
        user_choice2=""
        while(user_choice2!='c' and user_choice2!='q'):
            
            if user_choice2=='c':
                   continue
            if user_choice2=='q':
                   exit()
                





                    
                
          
