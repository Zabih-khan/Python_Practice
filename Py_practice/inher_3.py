class Foo(object):
    
    def __init__(self):
        
        print ("foo init")
class Bar(object):
    
    def __init__(self):
        print ("bar init")
class FooBar(Foo, Bar):
    
    def __init__(self):
        
        print ("foobar init")
        super(Foo, self).__init__()


a = FooBar()
