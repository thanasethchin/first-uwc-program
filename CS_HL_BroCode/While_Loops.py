# while loop  = execute some code WHILE some condition remains true
#               (runs until statement is true)

# name = input("Enter your name: ")

# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")
# print(f"Hello, {name}")


# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can not be negative")
#     age = int(input("Enter your age: "))
# print(f"You are {age} years old")


food = input("Enter your favorite food (q to quit): ")

while not food == "q":
    print(f"Your favorite food is {food}")
    food = input("Enter another favorite food (q to quit): ")
print("Bye")