'''Exercise 5: Replace a substring within a string.

Example: Replace "World" with the person's name in the string "Hello, World!".'''

greeting = "Hello, World!"
person_name = input("Write your name: ")

greeting = greeting.replace("World", person_name)

print(greeting)
