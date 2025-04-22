'''
42) Write an algorithm that asks the user for any positive integer 
and displays a count up to that value:
Example: Enter a value: 35
Count: 1 2 3 4 5 6 7 ... 33 34 35 Done!
'''

user_number = int(input("Enter a positive a value: "))
counter = 1

while (counter <= user_number):
  print(counter)
  counter += 1


print("It's over ! ")

input("Press Enter to Exit ... ")