import calendar
import datetime

def next_leap_year():
  now   = datetime.date.today()
  year  = now.year
  while( not calendar.isleap(year) ):
    year += 1

  return year

def leap_years():
  years = [x for x in range(2000,2051) if (calendar.isleap(x)) ]
  return years


print("Next leap year:",next_leap_year())
print("Leap years 2000-2050: " , leap_years())
print("29/6/2016 is ",calendar.weekday(2016,6,29))
