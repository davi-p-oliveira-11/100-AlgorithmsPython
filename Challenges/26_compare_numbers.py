"""
26) Write an algorithm that reads two integers and compares them, displaying
one of the following messages on the screen:
- The first value is greater
- The second value is greater
- There is no greater value, both are equal
"""

num_1 = int(input("Type a number: "))
num_2 = int(input("Type another number: "))

if num_1 > num_2:
    print("The first value is greater.")
elif num_1 < num_2:
    print("The second value is greater.")
else:
    print("There is no greater value, both are equal.")

input("Press Enter to Exit ... ")
