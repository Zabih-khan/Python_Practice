class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def Add(self):
        x=(self.a+self.b)
        print("The addition of two number is= ",x)
    def sub(self):
        x=(self.a-self.b)
        print("The subtraction of two number is=",x)
    def mul(self):
        x=(self.a*self.b)
        print("The multiflication of two number is= ",x)
    def divi(self):
        x=(self.a/self.b)
        print("The division of two number is= ",x)
    def average(self):
        x=(self.a+self.b)/2
        print("The average of two number is= ",x)
    def formula(self):
        x=self.a**2+self.b**2+2*self.a*self.b
        print("The solution of (a+b)2=",x)
a=int(input("Enter the first number="))
b=int(input("Enter the second number="))
obj=calculator(a,b)

##if __name__ == '__main__':
def main():
    
    while(True):
        print()
        print("""
☆                          ☆
╔uu═════════════════========═╗
❝<Welocme to Calculator > ❞"
❝<Made By __Zabihullah__> ❞"
╚══════nn═══════════========═╝
☆                          ☆

""")
        print("Select operation:")
        print("~~~~~~~~~~~~~~~~~")
        print("1:Addition")
        print("2:Subtraction")
        print("3:Multiflication")
        print("4:Division")
        print("5:Average")
        print("6:(a+b)2=?")

        user_choice=input()
        if user_choice not in ['1','2','3','4','5','6']:
            print("please enter the valid option")  
        else:
            user_choice=int(user_choice)
        if user_choice==1:
            obj.Add()
        elif user_choice==2:
            obj.sub()
        elif user_choice==3:
            obj.mul()
        elif user_choice==4:
            obj.divi()
        elif user_choice==5:
            obj.average()
        elif user_choice==6:
            obj.formula()
            
        print("===================================")
        print("press Q to quit OR C to continue:")
        user_choice2=()
        while (user_choice2!="c"  and user_choice2!="q"  ):
            user_choice2=input("ENTER:")
            if user_choice2=="q" :
                
                exit()
            elif user_choice=="c":
                continue
            else:
                print("PLEASE ENTER THE VALID OPTION:")

main()






            
