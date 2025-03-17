'''
11) Develop a logic that reads the values of A, B, and C of a quadratic equation and 
calculates the value of Delta.
'''

value_a = int(input('Enter the value of A '))
value_b = int(input('Enter the value of B '))
value_c = int(input('Enter the value of C '))

# bhaskara:  delta = b² - 4ac
delta_value = (value_b ** 2) - 4 * (value_a * value_c)
print(f'Delta is equal to: {delta_value}')

input("Press Enter to Exit ... ")