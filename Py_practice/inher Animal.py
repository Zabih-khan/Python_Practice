class Animal:
    def __init__(self,name,weight):  
        self.name=name
        self.weight=weight
    def who(self):   
        print("The name of the animal is ",self.name,"and its weight is :",self.weight)
    def sound(self):
        print("The sound of the animal class")
class sheep(Animal):
    def sound(self):   
        print("The sound of sheep is bee bee")
class Dog(Animal):
    def sound(self):
        print("The sound of dog is ghap ghap")
class Cow(Animal):
    def sound(self):

        print("The sound of cow is ba ba")
        

class Zoo:
    def __init__(self,x):
        self.a=x
        
        address.append(x)
    def object(self):
        print("The Adress of the Object is Saved at:\n",self.a)


        
address=[]

print("\n")   
obj1=sheep("sheep",200)
obj1.who()
obj1.sound()



#Here (obj1) is value of x and pass this value with x
#and then obj1 append in address

zoo=Zoo(obj1)  
zoo.object()

print("\n")   

obj2=Dog("Dog",150)
obj2.who()
obj2.sound()
zoo=Zoo(obj2)
zoo.object()


print("\n")   


obj3=Cow("Cow",500)
obj3.who()
obj3.sound()
zoo=Zoo(obj3)
zoo.object()


##obj=sheep("sheep",200)
##obj.who()
##obj.sound()
