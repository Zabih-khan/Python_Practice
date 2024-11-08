class Find_density:
    mass=int(input("enter the mass:"))
    volume=int(input("enter the volume:"))

    def density(self):
        self.mass=self.mass
        self.volume=self.volume
        d=self.mass/self.volume
        print("The density of the object is:",d)


obj=Find_density()
obj.density()
