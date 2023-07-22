class person:
    def __init__(self):
        self.msg=None
    def assignvalue(self):
        self.msg="Hello world"
    def getvalue(self,str):
        self.msg=str
    def printvalue(self):
        print(self.msg)


M=person()
M.printvalue()
print()

M.assignvalue()
M.printvalue()
print()

M.getvalue("How are you")
M.printvalue()
print()

        
