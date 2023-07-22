class library:
    def __init__(self,list,name):
        self.booklist=list
        self.library_name=name
        self.lendDic={}
    def displaybook(self):
        print(f"We have the following book in {self.library_name} library:")
        print("============================================")
        for book in self.booklist :
            print(book)

    def lendbook(self,user,book):
        if book not in self.lendDic.keys():
            self.lendDic.update({book:user})
            print("Lender -database has been updated.You can take the book now.")
        else:
            print(f"Book is already being used by {self.lendDic[book]}")

            

    def addbook(self,book ):
        print("Book has been added ")
        self.booklist.append(book)
    def returnbook(self,book):
        self.lendDic.pop(book)
         

if __name__=='__main__':
    
    obj=library(['--English','--Urdu','--islamyat','--Intro to computing'],'Cenral')



    while(True):
        print()
        print("===< WELCOME >===")
        print("1:Display Book")
        print("2:Lend Book")
        print("3:Add Book")
        print("4:return Book")
        user_choice=input("\nchoice option:")
        if user_choice not in ['1','2','3','4']:
            print('please Enter the correct option:')
            continue
        else:
            user_choice=int(user_choice)


        if user_choice==1:
            obj.displaybook()
            
            
        elif user_choice==2:
            book=input("Enter the name of the book that you want to lend:")
            user=input("Enter your name:")
            obj.lendbook(user,book)
            
        elif user_choice==3:

            book=input("Enter the name of the book that you want to add:")
            obj.addbook(book)
            
        elif user_choice==4:
            book=input("Enter the name of the book that you want to return:")
            obj.retrnbook(book)

        else:
            print("Not a valid option")
            
        print()

        print('_________________')
        print("Press __q__ to quit or press __c__ to continue:")
        print()
        user_choice2=()
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2=input("ENNTER:")
            if user_choice2=="q":
                exit()
            if user_choice2=='c':
                continue
            
        
        
            
        
        

        
            

            
            

        
        



