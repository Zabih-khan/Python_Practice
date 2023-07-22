class VEHICAL:
    def start(self,name=""):
        print(name,"is started:")
    def accelerate(self,name=""):
        pass
    def park(self,name=''):
        pass
    def stop(self,name=""):
        print(name,"is stopped:")
    
class CAR(VEHICAL):
    def accelerate(self,name=""):
        print(name,"is accelerating 60 km:")
    def park(self,name=''):
        print(name,"is parked at four wheeler:")
    
class BIKE(VEHICAL):
    def accelerate(self,name=""):
        print(name,"is accelerating 50km/h:")
    def park(self,name=''):
        print(name,"is parked at two wheeler:")


obj=CAR()
obj.start("Car")
obj.accelerate("Car")
obj.park("Car")
obj.stop("Car")
print()
b=BIKE()
b.start("Bike")
b.accelerate("Bike")
b.park("Bike")
b.stop("Bike")

    

    
