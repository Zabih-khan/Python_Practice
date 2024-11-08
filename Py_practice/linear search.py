def linear_search(arr,key,size):
    flag=0
    for i in range(size):
        if (arr[i]==key):
            flag=1
            pos=i+1
            break
    if flag==1:
        print("number found at position ",pos,"position")

    else:
        print("Number not found :")

size=int (input("Enter size of the list:"))
arr=[]

for i in range (size):
    val=int(input("Enter the number "))
    arr.append(val)

key =int(input("enter number to search:"))
linear_search(arr,key,size)
