class student:
    def __init__(self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno
    def detail (self):
        y="\nName is :"+ str(self.name) ,"\nAge is :"+str(self.age),"\nRoll no is:"+str(self.rollno)
        for x in y :
             print(x)

    def more_detail(self,father_name,address):
        self.f=father_name
        self.address=address
        z="\nFather name is :"+ str(self.f) ,"\nAddress is :"+str(self.address)
        for y in z :
             print(y)

        
        
        

obj=student("zabih",12,18381)
obj.detail()
obj.more_detail("Ghalib khan","Mera surizai payan peshawar")

