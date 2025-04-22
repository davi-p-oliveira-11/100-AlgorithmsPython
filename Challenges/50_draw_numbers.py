'''
  50) Develop a program that draws 20 numbers between 0 and 10 and displays on the screen:
a) Which numbers were drawn
b) How many numbers are greater than 5
c) How many numbers are divisible by 3
'''

import random

numbers = []
counter = 0
greater_than_5 = 0
divisible_by_3 = 0

while counter < 20:
    num = random.randint(0, 10)  
    numbers.append(num)

    if num > 5:
        greater_than_5 += 1

    if num % 3 == 0:
        divisible_by_3 += 1

    counter += 1

print(f"Numbers drawn: {numbers}")
print(f"Numbers greater than 5: {greater_than_5}")
print(f"Numbers divisible by 3: {divisible_by_3}")
