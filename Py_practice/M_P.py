class Library:
    def __init__(self,list,name):
        self.booklist=list
        self.library_name=name
        self.lendDic={}
    def displayBooks(self):
        print(f"We have the following books in our {self.library_name} library:")
        for book in self.booklist:
            print(book)       
zabih=Library(["*Urdu","*English","*Math"],"Zabih")
if __name__ == '__main__':
    while(True):
        print()
        print("""
☆                          ☆
╔uu═════════════════========═╗
❝<Welocme to Zabih Library> ❞
╚══════nn═══════════========═╝
☆                          ☆
""")

        print("1:display the book")
        user_choice=input()
        if user_choice not in ['1']:
            print("please enter a valid input")
            
            continue
        else :
            user_choice=int(user_choice)
        if user_choice==1:
            zabih.displayBooks() 
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
        
        
