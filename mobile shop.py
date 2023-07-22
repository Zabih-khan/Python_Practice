class shop:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def getprice(self):
        return self.price
    def __str__(self):
        return self.name+ ':' + str(self.getprice())
def mobile_list(x,y):
    menu=[]
    for i in range(len(a)):
        menu.append(shop(a[i],b[i]))
    return menu
a=['Nokai','sumsung','iphone','Qmobile']
b=['2000','15000','500000','1000']

m=mobile_list(a,b)

n=1
for i in m:
    print(n,'.',i)
    n=n+1



    


    
