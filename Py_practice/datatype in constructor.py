class Data_type:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def Find(self):
        print(type(self.a))
        print(type(self.b))
        print(type(self.c))


obj=Data_type(12,"zabih",12.0)
obj.Find()

    
    
