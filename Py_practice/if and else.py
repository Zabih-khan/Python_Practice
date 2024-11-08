class vote:
    age = int (input("Enter your age? "))  

    def find(self):
        if self.age>=18:
            
            print("You are eligible to vote !!");  
        else:  
            print("Sorry! you have to wait !!");  

        
obj=vote()
obj.find()
