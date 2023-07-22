# nested tuple Example
class T:
    def fun(self):
        my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
        print(my_tuple)
obj=T()
obj.fun()

# nested list Example
class LT:
    def fun(self):
        my_list = ["mouse", [8, 4, 6], ['a']]
        print(my_list[0])
obj=LT()
obj.fun()
