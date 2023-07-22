class MyClass:
    def __init__(self):
        self._my_string= ""
    @property

    def string(self):
        """zabihullah """
        print(self._my_string)


    @string.setter
    def string(self, new_value):
        
        assert isinstance(new_value, str), \
               "Give me a string, not a %r!" % type(new_value)
        
        self._my_string = new_value
        
    @string.deleter
    def x(self):
        self._my_string = None


mc = MyClass()
mc.string = "String!"
print(mc.string)
del mc.string
