#Example of multiful inheritance:

class detail1:
    def sum (self,a,b):
        self.a=a
        self.b=b
        print('Addition:',a+b)
        
class detail2(detail1):
    def sub (self,a,b):
        self.a=a
        self.b=b
        print('Subtraction:',a-b)
    
class detail3(detail2):
    def mul (self,a,b):
        self.a=a
        self.b=b
        print('Multiflication:',a*b)

obj=detail3()
obj.sum(21,4)
obj.sub(21,4)
obj.mul(21,4)


#Example of without inheritance


##class detail1:
##    def sum (self,a,b):
##        self.a=a
##        self.b=b
##        print('Addition:',a+b)   
##
##class detail2:
##    def sub (self,a,b):
##        self.a=a
##        self.b=b
##        print('Subtraction:',a-b)
##    
##class detail3:
##    def mul (self,a,b):
##        self.a=a
##        self.b=b
##        print('Multiflication:',a*b)
##
##obj=detail1()
##obj.sum(21,4)
##
##obj=detail2()
##obj.sub(21,4)
##
##obj=detail3()
##obj.mul(21,4)



























