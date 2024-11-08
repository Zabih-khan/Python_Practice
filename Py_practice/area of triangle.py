class Area:
    a = float(input('Enter first side: '))  
    b = float(input('Enter second side: '))  
    c = float(input('Enter third side: '))
    def triangle(self):
        self.x=self.a
        self.y=self.b
        self.z=self.c

        s = (self.a + self.b +self.c) / 2
        area = (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)


obj=Area()
obj.triangle()




##
##
##
### Three sides of the triangle is a, b and c:  
##a = float(input('Enter first side: '))  
##b = float(input('Enter second side: '))  
##c = float(input('Enter third side: '))  
##  
### calculate the semi-perimeter  
##s = (a + b + c) / 2  
##  
### calculate the area  
##area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
##print('The area of the triangle is %0.2f' %area)   
