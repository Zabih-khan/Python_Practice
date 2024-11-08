
#Initialize array     
arr = [25, 11, 7, 75, 56];

#Initialize min with first element of array.    
min = arr[0];    
     
#Loop through the array    
for i in arr:
    
#Compare elements of array with min    
   if(i < min):    
       min=i;            
print("Smallest element present in given array: " + str(min));   
