#Compute the air resistance on a football
from math import pi
class resistance:
    
    ρ=1.2
    V=10      #velocity of football
    m=0.43    #mass of football
    g=9.8     #Gravity
    a=11      #radius of football
    Cd=0.2    #drag coeﬃcient

    def cal(self):
        self.ρ=self.ρ
        self.V=self.V
        self.m=self.m
        self.g=self.g
        self.a=self.a
        self.Cd=self.Cd
        self.A=pi*self.a**2
        
        #The gravity force on an object
        Fg=self.m*self.g
        
        #A = πa2 -------  cross-sectional area
        A=pi*self.a**2
        
        #Air resistance
        Fd=1/2*self.Cd*self.ρ*self.A*self.V**2
        print("Air resistance of football is :",Fd,"ohm")
        

obj=resistance()
obj.cal()

        
        
        
        
