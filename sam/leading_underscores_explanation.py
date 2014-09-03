class MyClass():
    def __init__(self):
            self.__superprivate = "Hello"
            self._semiprivate = ", world!"

mc = MyClass()
print(mc._semiprivate)
""", world!"""
""" Also, 'from modulename import *' will not import global module names starting 
   with single (nor double) underscores), but mc._semiprivate would've been
   imported, because mc is imported among with it's names. The following will
   not be imported"""
_something_not_imported = "123"
print(mc.__dict__)
"""{'_MyClass__superprivate': 'Hello', '_semiprivate': ', world!'}"""
# print(mc.__superprivate)
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: myClass instance has no attribute '__superprivate'
"""