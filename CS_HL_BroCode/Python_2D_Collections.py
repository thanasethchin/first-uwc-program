# Python 2D Collection

fruits =        ["apple", "orange", "banana", "coconut"]
vegetables =    ["celery", "carrots", "potatoes"]
meats =         ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

# First index is the index in groceries
# The index after is the index inside the chosen index of groceries
# print(groceries[2][0])

# prints every value inside groceries
for collection in groceries:
    #prints every element inside the value inside groceries
    for food in collection:
        print(food, end=" ")
    print()


# 2D Tuple Numberpad

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()