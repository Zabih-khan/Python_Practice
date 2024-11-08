class greater:
    a = int(input("Enter a? "));  
    b = int(input("Enter b? "));  
    c = int(input("Enter c? "));
    
    def find(self):
        self.a=self.a
        self.b=self.b
        self.c=self.c

        if self.a>self.b and self.a>self.c: 
            print("a is largest");  
        if self.b>self.a and self.b>self.c:  
            print("b is largest");  
        if self.c>self.a and self.c>self.b:  
            print("c is largest");

obj=greater()
obj.find()
        


  
