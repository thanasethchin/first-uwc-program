# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA":"Washington D.C.",
            "UK": "London",
            "France": "Paris",
            "Thailand": "Bangkok"}

# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("USA"))
# print(capitals.get("UK"))

# if capitals.get("South Korea"): # To check whether the item is in the dictionary or not, we just put a name in
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"})
# capitals.pop("France") # Removes France from the dictionary
# capitals.popitem() # Removes the last item from the dictionary
# capitals.clear() # Clears the dictionary

# keys = capitals.keys()
# print(keys)
# value = capitals.values()
# print(value)

# for key in capitals.keys():
#     print(key, end=" ")
# print() # For moving the capitals (values) onto another line
# for value in capitals.values():
#     print(value, end=" ")

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")
# This prints out every key (country) and value (capital) in the dictionary