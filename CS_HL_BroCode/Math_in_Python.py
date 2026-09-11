# Arithmetic Operations

# friends = 10
# remainder = friends % 3
# print(remainder)



# Built-in Functions

# x = 3.14
# y = 4
# z = 10
# # result = round(x) Rounding to the nearest whole numher
# # result = abs(y) Absolute value/Distance away from zero as whole number
# # result = pow(y, 3) To the power 
# # result = max(x, y, z) Max value between variables in the brackets
# # result = min(x, y, z) Min value between variables in the brackets
# print(result)



# Math Module

# 1. Getting to know commands
# import math
# x = 9.1
# print(math.pi) Prints pi
# print(math.e) Prints Euler's number
# result = math.sqrt(x) Square roots the number
# result = math.ceil(x) Rounds the number up
# result = math.floor(x) Rounds the number down
# print(result)

# 2.1 Finding circumference of a circle
# import math
# radius = float(input('Enter the radius of a circle: '))
# circumference = 2 * math.pi * radius
# print(f"The circumference is: {round(circumference, 2)}cm") Rounds the circumference to two decimal points

# 2.2 Finding area of a circle
# import math
# radius = float(input("Enter the radius of a circle: "))
# area = math.pi * pow(radius, 2)
# print(f"The area od the circle is {round(area, 3)}cm^2")

# 2.3 Finding hypotenuse of a triangle
# import math
# a = float(input("Enter a number: "))
# b = float(input("Enter a number: "))
# hypotenuse = math.sqrt(pow(a, 2) + pow(b, 2))
# print(f"The hypotenuse is {hypotenuse}cm")