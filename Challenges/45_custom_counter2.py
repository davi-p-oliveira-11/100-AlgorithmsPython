'''
  45) The program above will have a problem when we enter the first value greater than the last one. 
 Solve this problem with code that works in any situation.
'''

first_value = int(input("Enter the first value: "))
last_value = int(input("Enter the last value: "))

# Makes sure that the value is positive  
increment = abs(int(input("Type the value of the increment: ")))

counter = first_value

if first_value <= last_value:
  while counter <= last_value:
    print(counter)
    counter += increment
  else:
    while counter >= last_value:
      print(counter)
      counter -= increment


print("It's over !")

input("Press Enter to exit ... ")