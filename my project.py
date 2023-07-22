class Library:
    def __init__(self,name,list):
        self.library_name=name
        self.booklist=list
        self.lendDic={}


    def displayBooks(self):
        print("we have the following books in our {self.library}")
        for book in self.booklist:
            p
        
    def lendBooks(self,user,book):
        for 
        print("which book do you want to lend")
        
    def addBooks(self,book):
        
        print("which book do you want to add")
    def returnBooks(self,book):


if __name__=='__main__':
    
    zabi=(["python","english","urdu"],"Zabih_Library")

    while(True):
        print(f"===Welcome to {zabi. library_name}===")
        print("Enter the choice :")
        print("1:Display the book:")
        print("2:Lend a book:")
        print("3:Add a book:")
        print("4:Return a book:")

        user_choice=input()
        if user_choice not in ["1","2","3","4"]:
            print("Please enter the valid number")
            continue


        else:
            user_choice=input(user_choice)
            if user_choice==1:
                
                zabi.displayBook()

            elif user_choice==2:
                zabi.lendBook()
            elif user_choice==3:
                zabi.addBook()
            elif user_choice==4:
                zabi.returnBook()
            
            
            
            
            








        

        

    
