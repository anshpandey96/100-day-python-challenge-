year = int(input("Enter a year :"))
           
# divided by 100 means centery year (Ending with 00 )
# century year divided by 400 is loop lead year 
if(year % 400 == 0 ) and (year  % 100 == 0 ):
       print("{0} is a leap year".format(year))


# not divided by 100 mean not a century year 
# year divided by 4 is a leap year 

elif (year % 4 == 0 ) and (year % 100!= 0 ):
          print("{0} is a leap year ".format(year))

# if not divided by both 400 (century year) and 4 (not century year )
# year is not leap year  

else:
         print("{0}is s NOt leap year ".format(year))



# year = int(input("Enter a year: "))

# # Century year divisible by 400
# if (year % 400 == 0) and (year % 100 == 0):
#     print("{0} is a leap year".format(year))

# # Non-century year divisible by 4
# elif (year % 4 == 0) and (year % 100 != 0):
#     print("{0} is a leap year".format(year))

# # Not a leap year
# else:
#     print("{0} is not a leap year".format(year))

