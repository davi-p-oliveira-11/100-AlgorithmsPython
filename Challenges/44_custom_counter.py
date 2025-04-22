'''
44) Create an algorithm that reads the initial value of the count, the final value, and the increment, then displays all the values within the interval:
Example:
Enter the first value: 3
Enter the last value: 10
Enter the increment: 2
Counting: 3 5 7 9 It's over!
'''

first_value = int(input("Enter the first value: "))
last_value = int(input("Enter the last value: "))
increment = int(input("Enter the increment value: "))

counter = first_value

while counter <= last_value:
  print(counter)
  counter += increment


print("It's over !")

input("Press Enter to exit ... ")