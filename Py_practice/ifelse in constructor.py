class greater:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def find(self):
        if self.a>self.b and self.a>self.c:
            print("a is the largest number")
        elif self.b>self.a and self.b>self.c:
            print("b is the largest number")
        elif self.c>self.a and self.c>self.b:
            print("c is the largest number")
            

a = int(input("Enter a? "));  
b = int(input("Enter b? "));  
c = int(input("Enter c? "));

obj=greater(a,b,c)
obj.find()
