#Creat a food menu for resturent:



class Resturent:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def getprice(self):
        return self.price
    def __str__(self):
        return self.name + ':' + str(self.getprice())
#Define a function to build a menu
#which generate list of food
def builtmenu(x,y):
    menu=[]
    for i in range (len(a)):
        obj=Resturent(a[i],b[i])
        menu.append(obj)
    return menu

#items
a=['Coffee','Tea','Pizza','Burger','Cake'
      ,'Apple','Fries']
#price
b=['100','343','23','34','545','454','322']

#build a food menu
#From Here we call (builtmenu)function
#and pass the value of a and b to x ,y:

Foods=builtmenu(a,b)


#This is for list of food and price

n=1
for i in Foods:
    print(n,'.',i)
    n=n+1



        
        
