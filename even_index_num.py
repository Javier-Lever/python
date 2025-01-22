'''Write a Python code to accept a string from the user and display characters present at an even index number.

For example, str = "PYnative". so your code should display "P", "n", "t", "v".'''

string = input("Enter a string: ")
length = len(string)

def letterOf(index, string):
    if index < 1 or index > len(string):
        raise ValueError("Index out of bounds")
    return string[index - 1]

for i in range(length):
    character = letterOf(i + 1, string)
    if i % 2 == 0:
        print(character)