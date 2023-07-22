class Baselength:
    l=int(input("enter the number:"))
    inche=25.4
    meter=1000
    
    def length(self):
        self.l=self.l
        self.inche=self.inche
        self.meter=self.meter
        return self.l,self.inche,self.meter


##class inches(Baselength):
##    
##class Meters(Baselength):
##
##class Yards(Baselength):
##
##class perches(Baselength):






obj=Baselength()
print(obj.length())
