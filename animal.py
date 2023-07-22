class animal:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
    def getname(self):
        return self.name
    def getsound(self):
        return self.sound
    def __str__(self):
        return self.name + ':' + self.sound
l=[]

def getlist(x,y):
    l.append(obj)
    return l
x='y'
while x=='y' :
    a=input("Enter the name of animal:")
    b=input("Enter the Sound of animal:")
    obj=animal(a,b)
    var=getlist(a,b)
    x=input("Another animal? y/n")

n=1
for i in var:
    print(n,".",i)
    n=n+1
    
    




    
