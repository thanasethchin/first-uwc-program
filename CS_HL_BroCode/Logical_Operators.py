# Logical Operators = used in conditional statements

# and = checks if two or more conditions are True
# or = checks if at least one condition is True
# not = True if the condition is False, vice versa

temp = 25
sunny = False

if temp > 0 and temp < 30:
    print("The temperature is good")
else:
    print("The temperature is bad")

if not sunny:
    print("It is sunny outside")
else:
    print("It is cloudy outside")