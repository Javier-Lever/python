'''Write a Python code to remove characters from a string from 0 to n and return a new string.'''
#my solution
def remove_chars(my_string, my_num):
    part_remove = my_string[:my_num]
    my_string = my_string.replace(part_remove, "")
    return my_string

result = remove_chars("No x in Nixon", 8)
print(f"{result}")

#solution
def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))
