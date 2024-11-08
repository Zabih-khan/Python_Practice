class cal:
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def add(self):
        c=self.x+self.y
        print(c)

obj=cal(12,3)
obj.add()
