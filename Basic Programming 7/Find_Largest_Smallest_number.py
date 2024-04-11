number = [10, 20, 5, 40, 30, 72, 34]

largest = number[0]
smallest = number[0]

for num in number:
    if  num > largest:
        largest = num
    elif num < smallest:
        smallest = num
    
print(f"The largest number is {largest}")
print(f"The smallest number is {smallest}")