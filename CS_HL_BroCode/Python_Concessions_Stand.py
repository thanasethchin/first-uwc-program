# Python Concession Stand Program
# using dictionaries

menu = {"popcorn": 5.00,
        "pizza": 3.00,
        "fries": 4.00,
        "chips": 1.00,
        "pretzel": 2.50,
        "coca-cola": 1.50}
cart = []
total = 0

print("----------- MENU -----------")
for key, value in menu.items():
    print(f"{key:15}: ${value:.2f}")
print("----------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("----- YOUR ORDER -----")
for food in cart:
    total += menu.get(food) # The .get() helps retrieve the value (price) of the dictionary
    print(food, end=" ") # print() only prints the key (food item) of the dictionary

print()
print(f"Total is: ${total:.2f}")