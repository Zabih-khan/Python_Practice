n=int(input("Enter the number:"))
l=[]
for i in range(n):
    inp=input("Enter:")
    if inp.find("insert")>=0:
        a=inp[7:]
        x,y=a.split()
        x=int(x)
        y=int(y)
        l.insert(x,y)
    if inp.find("remove")>=0:
        b=inp[7:]
        b=int(b)
        l.remove(b)

    if inp.find("append")>=0:
        c=inp[7:]

        c=int(c)
        l.append(c)

    if inp.find("sort")>=0:
        
        l.sort()

    elif inp.find("pop")>=0:
        l.pop(-1)

    elif inp.find("print")>=0:
        print(l)
        
    elif inp.find("reverse")>=0:
        l.reverse()
        
        
