class area:
    
    def __init__(self,a,b,c):
        
        self.x=a
        self.y=b
        self.z=c
    
    def triangle(self):
        s = (self.x + self.y +self.z) / 2
        area = (s*(s-self.x)*(s-self.y)*(s-self.z)) ** 0.5
        print('The area of the triangle is %0.2f' %area)


a=float(input('Enter first side: '))  
b=float(input('Enter second side: '))
c=float(input('Enter third side: '))
obj=area(a,b,c)
obj.triangle()
        
        
