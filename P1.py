##a = int(input("Enter"))
##x = a
##p = 5.5 # interest rate
##
##i = 0
##while x <= 1.5*a:
##    x = x + p/100*x
##    i = i + 1
##    print (i)
##


    

a = int(input("Enter"))
x = a
p = 5.5
for i in range (100,int(1.5*a)):
    
    a=a+p/100*a
    i=i+1
    print(i)
