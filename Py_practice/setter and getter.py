class Employee:
    def __init__(self):
        self.__id=0
        self.__name=''
        self.__salary=''
        self.__gender=''
        self.__city=''

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,value):
        self.__id=value
        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name=value
        
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,value):
        self.__salary=value

    @property
    def gender(self):
        return self.__gender
    @name.setter
    def gender(self,value):
        self.__gender=value


    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self,value):
        self.__city=value


e=Employee()
print("Enter Employee detail:")
i= int(input("Enter id:"))
n= input("Enter Name:")
s= int(input("Enter salary:"))
g= input("Enter Gender:")
c= input("Enter City:")

e.id=i
e.name=n
e.salary=s
e.gender=g
e.city=c
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Display Employee Detail:")
print("Id:",e.id)
print("Name:",e.name)
print("Salary:",e.salary)
print("Gender::",e.gender)
print("City:",e.city)
print("Name:",e.name)


