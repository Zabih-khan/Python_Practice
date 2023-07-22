# creating parent class
class Parent:
    BloodGroup = 'A'
    Gender = 'Male'
    Hobby = 'Chess'
    
# creating child class
class Child(Parent): # inheriting parent class
    BloodGroup = 'A+'
    Gender = 'Female'
    
    
    def print_data():
        
        print(BloodGroup, Gender, Hobby)
    
# creating object for child class
child1 = Child()

# as child1 inherits it's parent's hobby printed data would be it's parent's
child1.print_data()
  
