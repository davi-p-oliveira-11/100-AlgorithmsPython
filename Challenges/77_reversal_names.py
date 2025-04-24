'''
  77) Create a program that reads 7 people's names and stores them in an array. 
      At the end, display a list with all the names in reverse order from the
      one they were entered.
'''

names = []

for i in range(7):
    name = input(f"Enter the name of person {i + 1}:").strip()
    if name:
        names.append(name)
    else:
        print("Invalid input. Please enter a valid name.")
        i -= 1  


i = 0
while i < 7:
    name = input(f"Enter the name of person {i + 1}:").strip()
    if name:
        names.append(name)
        i += 1
    else:
        print("Invalid input. Please enter a valid name.")


print("Names in reverse order:", ', '.join(reversed(names)))


input("Press Enter to exit ... ")
