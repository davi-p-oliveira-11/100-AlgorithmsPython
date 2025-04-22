'''
   49) Create a program that reads 6 integers and, at the end, 
       shows how many of them are even and how many are odd.
'''

counter = 0
even_numbers = 0
odd_numbers = 0

while counter < 6:
  number = int(input(f"Enter an integer {counter + 1}: "))

  if number % 2 == 0:
    even_numbers += 1
  else:
    odd_numbers += 1

  counter += 1 


print(f"You entered {even_numbers} even numbers`")
print(f"You entered {odd_numbers} odd numbers`")


input("Press Enter to Exit ... ")