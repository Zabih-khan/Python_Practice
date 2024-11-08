class library:
    def __init__(self,list,name):
        self.booklist=list
        self.library_name=name
    def displaybook(self):
        print(f"we have the following book in our {self.library_name} library")
        for book in self.booklist:
              print(book)
obj=library(["*English","*Urdu","*Math","*Computer science","*Islanyat"],"Central")
if __name__=='__main__':
    while(True):
        print("Welcone to my library")
        print("1:Display the book")
        user_choice=input()

        if user_choice not in["1"]:
            print("please enter the valid option")
            continue
        else:
            user_choice=int(user_choice)
        if user_choice==1:
            obj.displaybook()
        else:
             print("Not a valid option ")
        print("press q to quit and c to continue")
        user_choice2=""

        while (user_choice2!="c" and user_choice2!="q"):
            user_choice2=input()
            if user_choice2=="q":
                exit()
            elif user_choice=="c":
                continue
        
        
        
            
            
            
             
     
