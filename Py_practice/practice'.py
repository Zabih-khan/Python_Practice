a=["Apple","orange","banana","Pineapple"]
#Display element and count the element of the list:
count=0
n=1
for i in a:
    count+=1
    print(n,".",i)
    n=n+1
print("Total element is :",count)
    
#insert the element:
x="y"
while x=="y":
    element=input("Enter the element that you want to insert:")
    a.append(element)
    x=input("Another element ? y/n")
#This line is for printing the element in top to bottom:
n=1
for i in a:
    print(n,".",i)
    n=n+1
#what is the first element of the list:
print(a[0])
