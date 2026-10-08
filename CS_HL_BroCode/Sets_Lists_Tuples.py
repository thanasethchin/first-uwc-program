# collection = single "variable" used to store multiple values
#    List = [] ordered and changeable. Duplicates OK
#    Set = {} underordered and immutable, but Add/Remove OK, NO duplicates
#    Tuple = () order and uncahngeable. Duplicates OK. Faster

# LIST 
# fruits = ["apple", "orange", "banana", "coconut"]
# print(dir(fruits)) # dir() returns all properties and values that the list can perform
# print(help(fruits)) # help() gives descriptions of the attributes it can perform
# print(len(fruits))
# print("apple" in fruits)
# print("pineapple" in fruits)


# LIST METHODS
# fruits[0] = "pineapple" # replaces at index 0
# fruits.append("peaches") # add to the list from behind
# fruits.remove("coconut") # removes the value
# fruits.insert(2, "mango") # inserts at the index
# fruits.sort() # sorts the value alphabetically
# fruits.reverse() # reverses the list based on the order
# fruits.clear() # removes all elements
# fruits.index("apple") # prints the index of the value
# fruits.count("banana") # counts how many times the value is repeated


# print(fruits[::-1])

# for fruit in fruits:    # for every fruit in fruits
#      print(fruit)

# SETS
# fruits = {"apple", "orange", "banana", "coconut"}
# print(dir(fruits))
# print(help(fruits))
# fruits.add("pineapple") # adds the value in the set
# fruits.remove("apple") # removes the value in the set
# fruits.pop() # removes a random element
# fruits.clear() # removes all elements in the set

# TUPLE
fruits = ("apple", "orange", "banana", "coconut")
fruits.index("apple")
fruits.count("coconut")