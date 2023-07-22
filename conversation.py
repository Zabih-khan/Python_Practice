#conversation of degree in the form of table using while loop:

print('F    C')
print()

C = 0
while C <= 100:
    F = 9 * C / 5 + 32
    print(F,"=", C)
    C += 10                                                
##============================================================

##class degree:
##    def __init__(self,F):
##        self .F=F
##    def conversation(self):
##        print(' F     C')
##        ##======================================================
##        #Here in this line the first number mean(10)is  starting number
##        #The second number (100) is a last number
##        #And the last number(10) means that gap between the numbers
##        #e.g:   10,20,30,40.....in this series there is 10 in between the numbers:
##        #Here We can create user define variable and then define in the range
##        ##======================================================
##
##        for C in range(10,100,10):
##            self.F = 9 * C / 5 + 32
##            print('%4.0f %4.0f' % (self.F, C))
##
##obj=degree("Fahrenhait")
##obj.conversation()






##print('   F   C')
##print()
##for C in range(10, 100, 10):    
##    F = 9 * C / 5 + 32
##    print('%4.0f %4.0f' % (F, C))
