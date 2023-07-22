class Number:
    def __init__(self,num):
        self.num=num
        
    def inputNum(self):
        self.num=int(input("Enter the number"))
        
    def printNum(self):
        print("Number=",self.num)

obj=Number(12)
obj.inputNum()
obj.printNum()
