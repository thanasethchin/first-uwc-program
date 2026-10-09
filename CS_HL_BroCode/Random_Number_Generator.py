# Python Random Number Generator

import random

# low = 1
# high = 100
# options = ("rock", "paper", "scissors")
# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",]

# number = random.randint(1, 100) # .randint() means random integer
# number = random.random() # returns random floating point number between 0 and 1
# option = random.choice(options) # chooses the random value in options
# random.shuffle(cards)
# print(cards)

# print(number)
# print(option)

# NUMBER GUESSING GAME
low = 1
high = 100
guesses = 0
number = random.randint(low, high)

while True:
    guess = int(input(f"Enter a number betweem {low} - {high}: "))
    guesses += 1

    if guess < number:
        print(f"{guess} is too low")
    elif guess > number:
        print(f"{guess} is too high")
    else:
        print(f"{guess} is correct!")
        break

print(f"This round took you {guesses} guesses")