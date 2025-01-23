'''Write a Python code to remove characters from a string from 0 to n and return a new string.'''

def remove_chars(my_string, my_num):
    part_remove = my_string[:my_num + 1]
    my_string = my_string.replace(part_remove, "")
    return my_string

result = remove_chars("No x in Nixon", 7)
print(f"{result}")

