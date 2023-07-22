import numpy as np
lst = [ ] 
n = int(input("How many number do you want to enter:")) 
for i in range(0, n): 
    ele =  int(input('>>>'))
    lst.append(ele)
    pass
#find average
average=sum(lst)/2
print()
print('Average:',average)

#find count even number:
even_count=0
for i in lst:
    if i%2==0:
        even_count+=1
print("Even numbers in the list: ", even_count)

#find count prime number:
count=0
for i in lst:
     if i >1:
         for j in range(2,int(i/2)+1):
             if i%j==0:
                 count+=1
print('prime number in the list is:',count)

#find standard deviation:

print('Standard Deviation:', np.std(lst))



