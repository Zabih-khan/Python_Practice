class Number:
    def __init__(self,num):
        self.num=num
    def display(self):
        print(self.num)

N1=Number(123)
N1.display()
print("Address of N1")
print(N1)
N2=Number(12)

print()
N2.display()
print("Address of N2")
print(N2)
