# Task 1: Screenshot Favorite Number

# Favorite_number = 7

# Task 2: Generate a Random Number

import random

# favorite_number = 7
# random_number = random.randrange(25)

# print(random_number)

# output = favorite_number - random_number
# print(output)

# # Create a while loop that generates a random number and checks if it matches your favorite number.random_number
# # Keep track of how many times the computer has guessed.
# # Once the computer guesses the correct number, display a message explaining how many times it took the computer to guess your favorite number.


favorite_number = 7
random_number = random.randrange(25)

favorite_number = 7
a = 0
guesses = random.randrange(0, 25)

while random_number != favorite_number:
    random_number = random.randrange(25)

while guesses != favorite_number:
    guesses = random.randrange(0, 25)
    a += guesses

else:
    guesses += a

    print(f'It took {a} times to guess your favorite number!')