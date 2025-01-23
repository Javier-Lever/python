'''Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504

A=πr^2'''

r = float(input("Write the radius to calculate the Area: "))
import math
area = math.pi * r ** 2

print(f"Area = {area}")
