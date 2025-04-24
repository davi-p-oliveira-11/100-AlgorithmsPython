'''
  76) Create a program that automatically fills a numeric array with 7 randomly generated 
      numbers by the computer and then displays the generated values on the screen.
'''

import random

arr6 = [random.randint(0, 9) for _ in range(7)]

print(' '.join(map(str, arr6)))

print(arr6)

input("Press Enter to exit ... ")
