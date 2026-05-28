# Write a python program to display calendar.

import calendar
year = int(input("Enter the year : "))
month = int(input("Enter the month : "))

cal = calendar.month(year, month)
print(cal)
