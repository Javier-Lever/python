'''Write a Python program that prints the numbers from 1 to 100 with the following conditions:

For numbers that are multiples of 3, print "Frizz" instead of the number.
For numbers that are multiples of 5, print "Buzz" instead of the number.
For numbers that are multiples of both 3 and 5, print "FrizzBuzz" instead of the number.
For all other numbers, print the number itself.'''

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FrizzBuzz")
    elif number % 3 == 0:
        print("Frizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)    