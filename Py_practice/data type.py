class Data_type:

    a=10  
    b="Hi Python"  
    c = 10.5  
    def Find(self):
        self.a=self.a
        self.b=self.b
        self.c=self.c
        print(type(self.a))  
        print(type(self.b))  
        print(type(self.c))  

obj=Data_type()
obj.Find()
