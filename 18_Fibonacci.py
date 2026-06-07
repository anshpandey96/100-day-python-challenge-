# Fibonacci sequence :- the fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, typically starting with 0 and 1 . So , the sequence begins with 0 and 1, and next number is obtrained by adding the previous two numbers.this pattern continues indefinitely, generating a sequence that look like this :

# 0,1,1,2,3,5,8,13,21,34,55,89,144 and so on .

# Mathematically , the Fibonacci sequence can be define using the following recurrence ralation :

#F (0) = 0 F(1) = 1 F(n) = F(n-1) + F(n-1) + F(n-2) form > 1


nterms = int(input("how many terms ? "))

n1,n2 = 0 ,1
count = 0 

if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequene upto",nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence: ")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1




