class student:
    def __init__(self,name,height):
        self.name=name
        self.height=height

    def getname(self):
        return self.name

    def getheight(self):
        return self.height

    def __str__(self):
        return self.getname()+ ':' + self.getheight()

l=[]
def menu(x,y):
    l.append(obj)
    return(l)

x='y'
while x=='y':
    a=input("Enter Name:")
    b=input("Enter Height:")
    obj=student(a,b)
    m=menu(a,b)
    x=input("Another student? y/n:")


n=1
for i in m:
    print(n,'.',i)
    



