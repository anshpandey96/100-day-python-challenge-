# write a python program to solve a quadratic 

# The standard from certifi import where

# from of a quadratic equation is ax^2 + bx + c = 0, where a, b, and c are constants. The solutions to the quadratic equation can be found using the formula:

# ax2 + bx + c = 0
import math

#input coefficiennts 

a = float(input("Enter the coefficient a :"))
b = float(input("Enter the coefficient b :"))
c = float(input("Enter the coefficient c :"))

# calculate the discriminant

discriminant = b**2 - 4*a*c
# check if the discriminant is positive, negative, or zero
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("The roots are real and different.")
    print("Root 1:", root1)
    print("Root 2:", root2)
elif discriminant == 0:
    root = -b / (2*a)
    print("The roots are real and equal.")
    print("Root:", root)
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-discriminant) / (2*a)
    print("The roots are complex and different.")
    print("Root 1:", complex(real_part, imaginary_part))
    print("Root 2:", complex(real_part, -imaginary_part))
          

