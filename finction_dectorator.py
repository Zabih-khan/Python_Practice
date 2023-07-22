class abasyn:
    def uppercase(function):
        def wrapper(self):
            fun=function()
            make_uppercase=fun.upper()
            return make_uppercase
        return wrapper

    @uppercase
    def say_hi():
        return 'zabihullah'
    

obj=abasyn()
print(obj.say_hi())
