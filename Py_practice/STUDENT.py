class student:
    def __init__(self,name,fname,rollno):
        self.name=name
        self.f=fname
        self.r=rollno
    def get_detail(self):
        return (self.name,self.f,self.r)


obj=student("zabih","ghalib",18381)
print(obj.get_detail())
