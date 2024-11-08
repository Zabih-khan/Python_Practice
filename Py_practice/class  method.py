class mobile:
    fp='yes'
    def __init__(self):
        self.model="realme x"
    def show_model(self):
        print("Model:",self.model)

    @classmethod
    def is_fp(cls):
        print(cls.fp,":finger print available")
obj=mobile()
obj.show_model()
#Here we call the method with class name becauase its a class method
mobile.is_fp()
