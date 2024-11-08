#Decorator are just function that take function as first
#parameter and return a function
def logging(f):
  def decorator_function(*args, **kwargs):
    print('executing '+f.__name__)
    return f(*args, **kwargs)
  return decorator_function
#Use it like this
@logging
def hello_world():
  print('Hello World')
  
hello_world()
