'''Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.'''

previous_num = 0
for i in range(10):
    sum_num = i + previous_num
    print(f"Current Number {i} Previous Number {previous_num}  Sum:  {sum_num}")
    previous_num = i