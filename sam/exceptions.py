"""
In Python, all exceptions must be instances of a class that derives from
BaseException. In a try statement with an except clause that mentions a
particular class, that clause also handles any exception classes derived from
that class (but not exception classes from which it is derived). Two exception
classes that are not related via subclassing are never equivalent, even if they
have the same name.
"""

def read_integer(prompt="Please enter a number: ", error="Oops!  That was no valid number.  Try again..."):
   while True:
       try:
           x = int(input(prompt))
           break        # breaks out of the while loop
       except ValueError:
           print(error)
       except (RuntimeError, TypeError, NameError):      # we may have more than one except (just example nonsense)
         pass
   return x

s = read_integer()
print("I've read the integer ", s)

""" Wildcard exepct: """

import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])     ## Prints a message
    raise                                             ## Re-raises, allowing callers to handle it

""" sys.exc_info() returns information about the most recent exception caught by
    an except in the current or in an older stack frame:

    (<class 'IOError'>, IOError(2, 'No such file or directory'), <traceback object a
t 0x24bf440>)
"""

"""
The try ... except statement has an optional else clause, which, when present,
must follow all except clauses. It is useful for code that must be executed if
the try clause does not raise an exception. For example: """ 

try:
  f = open("myerrorfile", 'r')
except IOError:
  print('cannot open', arg)
else:    ## it must follow all except clauses, last!
  print(arg, 'has', len(f.readlines()), 'lines')
  f.close()


""" Assigning the caught exception to a varible allows us to retrieve the
    arguments with wich the exception was originally raised: """
try:
   raise Exception('spam', 'eggs')  # raising with arguments
except Exception as inst:
   print(type(inst))    # the exception instance
   print(inst.args)     # arguments stored in .args
   print(inst)          # __str__ allows args to be printed directly,
                        # but may be overridden in exception subclasses
   x, y = inst.args     # unpack args
   print('x =', x) # spam
   print('y =', y) # eggs


""" Custom exceptions Exceptions should typically be derived from the Exception
class, either directly or indirectly. For example: """

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)

""" 
In this example, the default __init__() of Exception has been overridden.
The new behavior simply creates the value attribute. This replaces the default
behavior of creating the args attribute. 
"""

""" Finally clause """

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

"""
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
"""


"""
5.4. Exception hierarchy¶
The class hierarchy for built-in exceptions is:

BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- ArithmeticError          <----------------
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError           <----------------
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
"""
