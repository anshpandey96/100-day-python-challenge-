# finding sum of array using sum()

arr = [1, 2, 3]

ans = sum(arr)

print("Sum of the array is", ans)

def sum_of_array(arr):
    total = 0  # initialize a variable to store the sum
    for element in arr:
        total += element
    return total

array = [1, 2, 3]
result = sum_of_array(array)
print("Sum of the array :", result)




