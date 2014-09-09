#functional-style head/tail unpacking
h, *t = [1, 2, 3]

print(h, t)
# h = 1
# t = [2, 3]

*hs, t = [1, 2, 3]

print(h, t)
# h = [1, 2]
# t = 3

# Changing dynamically how an object prints itself (__str__)
def introspect(self):
   result=""
   for k,v in self.__dict__.items():
   result += k+": "+v+"\n"
   return result

#C.__str__ = introspect
#print(c)

# Adding a METHOD (not function) to an instance:
   # 1 - 'pure' python implementation
      # c is an instance of some class, print_var is some defined FUNCTION
      # >>> import types
      # >>> c.print_var = types.MethodType(print_var, c)
      # >>> c.print_var
      # <bound method MyClass.print_var of <__main__.MyClass object at 0x98a1bac>>
      # >>> c.print_var()

   # Method 2, using __get__
      # >>> c.print_var = print_var.__get__(c)
      # >>> c.print_var
      # <bound method MyClass.print_var of <__main__.MyClass object at 0x98a1bac>>
      # >>> c.print_var()

   # Behind the scenes the __get__ method actually

   # Note that in both cases c.print_var returns "bound method"
   # The following will give a differente result:

      # c.print_var = print_var
      # <function print_var at 0x20ec270>

   # In this case, print_var is NOT a method, but an attribute on the object c
   # that contains a function. It means that calling c.print_var() will raise
   # an argument error, since self is not automatically bounded as first
   # argument of the method call (since it's a function, not a method)
