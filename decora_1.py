'pass function which we want to decorate in decorator callable object'
def our_decorator(func):  # func is function to be decorated by decorator
  
  def wrapper(x):       # x is parameter which is passed in func
    if x%2==0:
      return func(x)
    else:
      print("number should be even")
  return wrapper

@ our_decorator
def func(x):         # actual function 
  print(x,"is even")
func(2)
func(1)

' if you do not want to use @'
func=our_decorator(func)
func(2)
