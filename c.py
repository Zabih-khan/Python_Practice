from abc import ABC, abstractmethod


class person(ABC):
    @abstractmethod
    def displayinfo(self):
        pass
    
    
class Manager(person):
    def creatAccount(self):
        pass
    def displayinfo(self):
        pass
        
class Customer(person):
    def displayinfo(self):
        pass
    def login(self):
        pass
    def setpasswordUsername(self):
        pass

class BankAccount:
    def credit(self):
        pass
    def debit(self):
        pass

    def transfer(self):
        pass

while True:
    
    print("""
    1.Creat Account:
    2.Display Info:
    3.Display Customer Info:
    4.Credit
    5.Debit:
    6.Transfer:
""")
    
    ch=int(input("Enter the choice:"))
           
    if ch==1:
        
        pass
           
           
        
               


 
##obj1=Manager()
##obj1.creatAccount()
##obj1.displayinfo()
##
##obj2=Customer()
##obj2.login()
##obj.setpasswordUsername()

