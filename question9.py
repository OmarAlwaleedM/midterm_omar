# Question 9 — Replace numbers in a list

import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

print(f"Original list: {random_numbers}")

# loop through the list by index so we can change items in place
for i in range(len(random_numbers)):
    if random_numbers[i] > 50:
        # replace numbers greater than 50 with a random number between 20 and 30
        random_numbers[i] = random.randint(20, 30)
    else:
        # replace numbers 50 or lower with "XX"
        random_numbers[i] = "XX"

print(f"Modified list: {random_numbers}")

# Example output:
# Original list: [99, 23, 75, 13, 80, 90, 66, 55, 4, 56]
# Modified list: [25, 'XX', 24, 'XX', 21, 22, 27, 22, 'XX', 20]
# (numbers change each run because of random)
