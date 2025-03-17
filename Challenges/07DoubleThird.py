'''
 7) Create an algorithm that reads a real number and displays its double and one-third.
Example
Enter a number: 3.5
The double of 3.5 is 7.0
One-third of 3.5 is 1.16666
'''

num = float(input("Enter a number: "))

double_of = num * 2
third_part = num / 3

print(f'The double of {num} is {double_of:.2f}')
print(f'The double of {num} is {third_part:.2f}')

input("Press enter to exit ... ")