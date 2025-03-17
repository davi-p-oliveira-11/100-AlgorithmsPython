'''
6) Create a program that reads an integer and shows its successor and successor.
Enter a number: 9
The predecessor of 9 is 8
The successor of 9 is 10
'''

num_1 = int(input("Type a number: "))

predecessor = num_1 - 1
successor = num_1 + 1

print(f'The predecessor of {num_1} is {predecessor}')
print(f'The successor of {num_1} is {successor}')

input("Press enter to exit ... ")