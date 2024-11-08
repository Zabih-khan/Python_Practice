class databirth:
    def __init__(self):
        self.dic={"khan":"2015"}
        
    def showdatabirth(self):
        name=input("What is your friend name:")
        if name in self.dic:
            print(self.dic[name])
        else:
            print("Not found:")

    def Add_birthdata_list(self):
        name=input("Enter your friend name:")
        date=input("Enter date:")
        self.dic[name]=(date)
        print("Birthday list has been added:")

        
birth=databirth()
if __name__=="__main__":
    
    while True:
        print("""
            1.Show Birthday:
            2.Add Birthday List:   
        """)
        ch=int(input("Select choice:"))
        if ch==1:
            birth.showdatabirth()

        if ch==2:
            birth.Add_birthdata_list()

            
