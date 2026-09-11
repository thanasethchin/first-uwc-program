# String Methods

# name = input("Enter your full name: ")

# len() - Shows the length of the string including spaces
# result = len(name)

# .find("") - Finds the position of the first character from the front
# result = name.find(" ")

# .rfind("") - Finds the position of the first character from the back
# result = name.rfind("a")

# .capitalize() - Capitalizes the first letter only
# result = name.capitalize()

# .upper() - Makes all characters uppercased
# result = name.upper()

# .lower() - Makes all the characters lowercased
# result = name.lower()

# .isdigit() - Only returns true when all characters are digits
# result = name.isdigit()

# .isalpha() - Only returns true when all characters are in the alphabet (" " is not an alphabet)
# result = name.isalpha()

# .count("") - Counts the amount of the same character
# result = name.count("a")

# .replace("", "") - Replaces a character with the desired character
# result = name.replace("a", "i")

# print(result)

# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter your username: ")

if len(username) > 12:
    print("The username must not have more than 12 characters")
elif not username.isalpha():
    print("The username must not contain spaces or digits")
else:
    print("Username is valid")

