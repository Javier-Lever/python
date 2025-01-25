'''Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java'''

# Get the name of the file from the user
filename = input("Type the name of the file with the extension: ")

# separating the extension
filename_list = filename.split('.')

# print the file extension
print(filename_list[1])