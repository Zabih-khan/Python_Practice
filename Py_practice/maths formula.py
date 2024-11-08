class A:
   def formula(self,a,b): 
    print("Answer is :",a**2+b**2+2*a*b)   
ans=A()
ans.formula(
    int(input("Enter the first number:")),
    int(input("Enter the second number:")))

