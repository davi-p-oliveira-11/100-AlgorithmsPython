'''
    80) Create an algorithm that fills a 30-position array with randomly generated numbers 
        between 1 and 15. After that, ask the user to enter a number (key), and your program 
        should display the positions where this key was found.
        Also, show how many times the key was drawn.
'''

import random

numbers3 = [random.randint(1, 15) for _ in range(30)]
key_positions = []

print("Generated numbers:", ', '.join(map(str, numbers3)))

try:
    key = int(input("Enter a number (key) to search for: "))
    if 1 <= key <= 15:
        for index, num in enumerate(numbers3):
            if num == key:
                key_positions.append(index)

        print(f"The key {key} was found at positions: {', '.join(map(str, key_positions))}")
        print(f"The key {key} appeared {len(key_positions)} times.")
    else:
        print("Invalid input. Please enter a number between 1 and 15.")
except ValueError:
    print("Invalid input. Please enter a valid number.")


input("Press Enter to exit ... ")