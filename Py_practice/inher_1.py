class Bank:
    def getrio1(self):
        
        return "Bank Rate of interest:"+ str(23)


class HBL:
    def getrio2(self):
        return "HBL Bank Rate of interest:"+str(4)
    
class STATE(Bank,HBL):
    def getrio3(self):
        return "STATE Bank Rate of interest:"+str(7)
b=STATE()
##b1=HBL()
##b2=STATE()


print(b.getrio1())
print(b.getrio2())
print(b.getrio3())
