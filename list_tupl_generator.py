'''Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')'''

# Getting the data from the user
data = input("Write the numbers separate by a coma and a space ', ': ")

# Generating the list 
data_list = data.split(", ")

# Generating the tuple from the list
data_tuple = tuple(data_list)

# Print the result
print(data_list)
print(data_tuple)