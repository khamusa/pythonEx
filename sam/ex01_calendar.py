
"""
Exercise 1: The Calendar Module.
In the following exercises, you will work with Python's calendar module:

Visit the Python documentation website at http://docs.python.org/3.1/modindex.html, 
and look at the documentation on the calendar module.
Import the calendar module.
Read the description of the function isleap(). Use isleap() to determine the next leap year.
Find and use a function in module calendar to determine how many leap years there will be between 
the years 2000 and 2050, inclusive.
Find and use a function in module calendar to determine which day of the week July 29, 2016 will be.
"""

import calendar
import datetime

class CalFun:
   def next_leap(self, year=datetime.datetime.now().year):
      while not calendar.isleap(year):
         year += 1

      return year

   def leap_years(self, start=datetime.datetime.now().year, end=(datetime.datetime.now().year + 50)):
      return [x for x in range(start, end + 1) if calendar.isleap(x) ]

# If this MODULE have been executed by calling python3 modulename <args>, the
# variable __name__ will have value '__main__'. Instead, if this module was imported
# by another script, __name__ will equal the name of this imported module.
if __name__ == '__main__':
   cf = CalFun()
   print("Next leap year will be ", cf.next_leap())
   print("Leap years between 2000 and 2050:", cf.leap_years(2000, 2050))
   print("July 29th 2016 is a", calendar.day_name[datetime.date(2016, 7, 29).weekday()])