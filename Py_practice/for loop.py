### User input for number of rows  
##rows = int(input("Enter the rows:"))  
### Outer loop will print number of rows  
##for i in range(0,rows,1):  
### Inner loop will print number of Astrisk  
##    for j in range(i):  
##        print("Z",end="")  
##    print()  




# prints all letters except 'a' and 't'
i = 0  
str1 = 'javatpoint'  
  
while i < len(str1):   
    if str1[i] == 'a' or str1[i] == 't':   
        i += 1  
        continue  
    print('Current Letter :', str1[i])   
    i += 1  
