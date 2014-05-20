
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

def next_leap():
   year = datetime.datetime.today().year
   while not calendar.isleap(year):
      year += 1
   return year

def leap_years(start, end):
   return [x for x  in range(start, end + 1) if calendar.isleap(x)]

def count_leaps(start, end):
   return len(leap_years(start, end))
   



if __name__ == '__main__':
   print(next_leap())
   print(count_leaps(2000, 2050))
   print(calendar.day_name[calendar.weekday(2016, 7, 29)])

