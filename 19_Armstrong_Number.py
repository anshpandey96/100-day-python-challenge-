# An Armstrong number (also called a narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

# In short: Armstrong number = sum of powered digits equals the number itself.

num = int(input("Enter a number : "))

num_str = str(num)
num_digits = len(num_str)

sum_of_powers = 0

temp_num =  num
while temp_num > 0:
    digit = temp_num % 10
    sum_of_powers += digit ** num_digits
    temp_num //= 10

if sum_of_powers == num:
    print(f"{num} is an Armstrong number . ")
else:
    print(f"{num} is not an Armstrong number . ")        



