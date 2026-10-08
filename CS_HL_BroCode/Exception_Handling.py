number = int(input("Enter a number: "))

try:
    result = 10 / number
    print(result)
except ZeroDivisionError:
    print("You can't divide by 0")
# finally:
#     print("This will always print")
# "finally" is not always needed, the code can run without