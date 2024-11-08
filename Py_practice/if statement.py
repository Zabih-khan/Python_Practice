class Test:
  
    def marks(self,a):
        self.marks=a       
        if self.marks > 85 and self.marks <= 100:            
            print("\nCongrats ! you scored grade A ...")  
        elif self.marks > 60 and self.marks <= 85:  
            print("\nYou scored grade B + ...")  
        elif self.marks > 40 and self.marks <= 60:  
            print("\nYou scored grade B ...")  
        elif self.marks > 30 and self.marks <= 40:  
            print("\nYou scored grade C ...")  
        else:  
            print("\nSorry you are fail ?")

obj=Test()
obj.marks(int(input("\nEnter the marks:")))
