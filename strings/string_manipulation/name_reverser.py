'''Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.'''

#Getting the name from the user
full_name = input("Write your first and last name: ")

#making a list to hold the name
name_list = full_name.split(' ')

#reversing the list
reversed_list = name_list[::-1]

#making a string with the name reversed
reverse_name = " ".join(reversed_list)

#Printing the name reversed
print(reverse_name)

