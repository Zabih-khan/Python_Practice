class temperature:
    F=int(input("Fahrenheit degrees="))

    def cel(self):
        self.F=self.F
        celcius=(5.0/9)*(self.F - 32)
        print("Celsius degrees =",celcius)

obj=temperature()
obj.cel()
