# Python Weight converter

weight = float(input("Enter your weight: "))
unit  = input("Kilograms or Pounds? (kg or lb): ")

if unit == "kg":
    weight = weight * 2.205
    unit = "lb"
    print(f"Your weight is: {round(weight, 1)} {unit}")
elif unit == "lb":
    weight = weight / 2.205
    unit = "kg"
    print(f"Your weight is: {round(weight, 1)} {unit}")
else:
    print("{unit} is not available")

