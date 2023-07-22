class mobile_shop:
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self.price=price
    def getmodel(self):
        return self.model
    def getprice(self):
        return self.price
    def __str__(self):
        return self.name + ':' + str(self.getmodel())+':' + str(self.getprice())
record=[]

def m_list(record,pname,pmodel,pprice):
    record.append(obj)
    return rec

x='y'
while x== 'y':
    a=input("Enter Phone name:")
    b=input("Enter phone model:")
    c=input("Enter phone price")
    obj=mobile_shop(a,b,c)
    
    Record =m_list(record,a,b,c)
    x=input("Another phone? y/n")

n=1
for i in Record :
    print(n,'.',i)
    n=n+1
    






    

    











    
        
