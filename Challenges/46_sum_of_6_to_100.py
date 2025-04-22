'''
  46) Create a program that calculates and displays the result 
      of the sum of 6 + 8 + 10 + 12 + 14 + ... + 98 + 100.
'''

sum_2 = 0
counter = 6

while counter <= 100:
  sum_2 += counter
  counter += 2


print(f"The sum between 6 + 8 + 10 + 12 ... + 98 + 100 is: {sum_2}")

input("Press Enter to exit ... ")