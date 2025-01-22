'''Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.'''

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 * num2 >= 1000: 
    print(f"The result is {num1 + num2}")
else:
    print(f"The result is {num1 * num2}")
    