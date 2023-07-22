#Initialize array     
arr = [25, 11, 7, 75, 56];     
     
#Initialize max with first element of array.    
max = arr[0];    
     
#Loop through the array    
for i in range(0, len(arr)):    
    #Compare elements of array with max    
   if(arr[i] > max):    
       max = arr[i];    
           
print("Largest element present in given array: " + str(max));   




##def large(a):
##    m=a[0]
##    for i in range (0,len(a)):
##        if a[i]>m:
##            m=a[i]
##    return m
##x=[2,34,5,6]
##print(large(x))
