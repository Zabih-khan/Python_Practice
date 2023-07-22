class person:
    counter=0
    def __init__(self):
        person.counter+=1        
    def displayinfo(self,name,id_number,city,gender):
        pass
    
class Manager(person):

    def creatAccount(self,name,id_number,city,gender):
        print()
        print("<---Your Detail--->")
        print("Name:",name)
        print("Id:",id_number)
        print("City:",city)
        print("Gender:",gender)
        print("your account has been Created:")
    
    def displayinfo(self,name,id_number,city,gender):
        print("<---Manager Detail--->")
        print("Name:",name)
        print("Id:",id_number)
        print("City:",city)
        print("Gender:",gender)
        
    
class Customer(person):
    
    def displayinfo(self,name,id_number,city,gender):
        print()
        print("<---Customer Detail--->")
        print("Name:",name)
        print("Id:",id_number)
        print("City:",city)
        print("Gender:",gender)

    def login(self,name,password):
        pass
    def setpassword(self,username,password):
        pass
c=Customer()
m=Manager()
if __name__=="__main__":

    while True:
        print("""
        1.Show Customer Detaial:
        2.Show Manager Detail:
        3.Create Account:
        4.login:
        5.setpassword:
""")
        
        ch=int(input("Select choice:"))
        if ch==1:
            c.displayinfo("khan",45949,"Lahour","male")
            print()
            print("Number of object in Manager class and Customer class is :",person.counter)

        if ch==2:
            m.displayinfo("Zabih",45949,"Peshawar","male")
            print()
            print("Number of object is :",person.counter)

        if ch==3:
            n=input("Enter Name:")
            i=int(input("Enter Id:"))
            c=input("Enter City:")
            g=input("Enter Gender:")
            m.creatAccount(n,i,c,g)

        if ch==4:
            pass

        if ch==5:
            pass

            
    
    


