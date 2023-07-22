class temp:
    fahrenheit=(celsius * 1.8) + 32
    def __init__(self,celsius):
        self.celsius=self.celsius
        self.fahrenheit=self.fahrenheit
    def calculate(self):
        print('%0.1f  Celsius is equal to %0.1f degree Fahrenheit'%(self.celsius,self.fahrenheit))

celsius = float(input('Enter temperature in Celsius: ')) 
obj=temp(celsius)
obj.calculate()
        
