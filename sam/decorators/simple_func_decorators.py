# Simple example:
def decor(F):
    print("I will now decorate the function {}".format(F))
    def wrapper(*args, **kargs):
         print("Decorator executing:")
         for i, arg in enumerate(args):
            print("arg {0}: {1}".format(i, arg))
         print(kargs)
         for key, value in kargs.items():    
            print("arg '{0}': {1}".format(key, value))

         print("Decorator finished, will now call the function")
         value = F(*args, **kargs)
         print("The function returned", value)
         return value
    
    something = True
    return wrapper

@decor
def bugue(*args, **kargs):
    print("Bugue being executed:\n {} \n{}".format(args, kargs))
    return "bugue"

bugue(1, 2, 3, 4, sam= "legal")

# 2 - using a class to decorate a function

class decor2():
   def __init__(self, func):
      print("I will now decorate the function {}".format(func))
      print("I will set an attribute pippo on myself to chandelier")
      self.pippo = "chandelier"
      self._func = func
      print("I will set the same attribute on the func to Chandelier2")
      self._func.pippo = "Chandelier2"

   def __call__(self, *args, **kargs):
      self._func(*args, **kargs)
      print("Func pippo is", self._func.pippo)


@decor2
def bugue2(*args, **kargs):
    print("Bugue2 being executed:\n {} \n{}".format(args, kargs))
    return "bugue2"

print("bugue2.pippo is ", bugue2.pippo)
print("Calling bugue2:", bugue2(4, 5, sam = "saudade"))

