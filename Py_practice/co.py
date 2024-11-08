from collections import Counter

shoes=int(input("No of shoes:"))
siz=list(map(int,input().split()))
dict=Counter(siz)
c=int(input("Enter customer:"))
p=0
for i in range(c):
    size,price=map(int,input("size ad price").split())
    if dict[size]:
        dict[siz]-=1
        p=p+price
print(p)
        
        
    
    
