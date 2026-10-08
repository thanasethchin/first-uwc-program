# Task 1: Basic Variable Declaration and Assignment
# Create a variable named age and assign your age to it.
# Create a variable named name and assign your name to it.
# Print the values of age and name.

age = 16
name = "Thanaseth Shanmartkit"
print(age, name)

# Task 2: Data Type Conversion
# Create a variable named price and assign a value with decimals (e.g., 19.99) to it.
# Convert price to an integer and store it in a new variable named integer_price.
# Print both price and integer_price.

price = 23.09
integer_price = round(price)
print(price, integer_price)

# Task 3: Global and Local Variables
# Create a global variable named global_count and initialize it to 0.
# Define a function named increment_count that increments global_count by 1.
# Call increment_count twice from outside the function.
# Print the value of global_count.

global_count = 0
def increment_count():
    global global_count
    global_count = global_count + 1
increment_count()
increment_count()
print(global_count)

def show_user_info(user_name, user_age, is_student):
    global school_name
    school_name = "UWC Changshu China"
    print(user_name)
    print(user_age)
    print(is_student)
    print(school_name)
show_user_info("Thanaseth", 16, True)





