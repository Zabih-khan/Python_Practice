#conversation into miles 
class converesion:
    a=float(input('Enter the number: '))
    b=(0.621371)
    def kilometer(self):
        self.a=self.a
        self.b=self.b
        miles=self.a*self.b
        print(' %0.3f kilometers is equal to %0.3f miles'%(self.a,miles))
    def meter(self):
        self.a=self.a
        self.b=0.000621371
        miles=self.a*self.b
        print(' %0.3f meter is equal to %0.3f miles'%(self.a,miles))

    def yard(self):
        self.a=self.a
        self.b=0.000568182
        miles=self.a*self.b
        print(' %0.3f yard is equal to %0.3f miles'%(self.a,miles))
    def feet(self):
        self.a=self.a
        self.b=0.000189394
        miles=self.a*self.b
        print(' %0.3f feet is equal to %0.3f miles'%(self.a,miles))

obj=converesion()
obj.kilometer()
obj.meter()
obj.yard()
obj.feet()






