from abc import ABC,abstractmethod

class Father(ABC):
    def __init__(self,a,b):
        
        self.a=a
        self.b=b
    @abstractmethod
    def Addition(self):
        pass
    @abstractmethod
    def subtraction(self):
        pass
class child1(Father):
    def Addition(self):
        c=self.a+self.b
        print("Addition__abstractmethod")
        print("Addition=",c)
        print()
class child2(child1):
    def subtraction(self):
        c=self.a-self.b
        print("subtraction__abstractmethod")
        print("subtraction=",c)
obj=child2(2,3)
obj.Addition()
obj.subtraction()
