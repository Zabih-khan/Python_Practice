class Employee:
    salary = 10000;
    name = "John Doe";

    def tax(s):
        print (s.salary * 0.10)

emp1 = Employee()

print ("Name:" , emp1.name)
print ("Salary" , emp1.salary)

emp1.tax()
