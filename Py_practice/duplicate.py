
numbers=[2,3,4,5,6,3,2,4]
duplicate=None

for i in range(0,len(numbers)):
    
    for j in range(i+1,len(numbers)):
        if numbers[i]==numbers[j]:
            
            duplicate=numbers[i]
            print(duplicate)
            break
