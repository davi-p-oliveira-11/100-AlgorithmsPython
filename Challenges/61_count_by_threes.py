'''
 61) Create a program that displays the following count on the screen using the "do while" loop:
0 3 6 9 12 15 18 21 24 27 30 It's over !!
'''

counter = 0

while True:
    print(counter)
    counter += 3
    if counter > 30:
        break

print("It's over!")


input("Press Enter to exit ... ")