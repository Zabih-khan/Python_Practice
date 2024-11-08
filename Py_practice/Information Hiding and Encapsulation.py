class Employee: 
   #'Common base class for all employees' 
   empCount = 0 
   def __init__(self, name, salary): 
      self.name = name 
      self.salary = salary 
      Employee.empCount += 1 
##      print("i m constructor") 
   def displayCount(self): 
     print( "Total Employee %d" % Employee.empCount) 
   def displayEmployee(self): 
      print ("Name :{} AND Salary :{}".format(self.name,self.salary))
#This would create first object of Employee class
emp1 = Employee("Zara", 2000) 
#"This would create second object of Employee class 
emp2 = Employee("Manni", 5000)
#"This would create third object of Employee class 
emp3 = Employee("Zabih", 6000)

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
emp1.displayCount()
