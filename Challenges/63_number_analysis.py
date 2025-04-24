'''
  63) Create a program using the "do while" loop that reads multiple numbers. 
 In each loop iteration, ask the user if they want to continue.
At the end, display:
a) The sum of all values
b) The smallest number entered
c) The average of all values
d) How many values are even
'''

sum_values = 0
smallest_number = float('inf')  
total_numbers = 0
even_count = 0

while True:
    number = int(input('Enter a number: '))

    sum_values += number
    total_numbers += 1

    if number < smallest_number:
        smallest_number = number

    if number % 2 == 0:
        even_count += 1

    continue_input = input('Do you want to enter another number? (Y/N): ').upper()
    if continue_input != 'Y':
        break

average = sum_values / total_numbers if total_numbers > 0 else 0

print(f"Sum of all values: {sum_values}")
print(f"Smallest number entered: {smallest_number}")
print(f"Average of all values: {average:.2f}")
print(f"Total even numbers: {even_count}")


input("Press Enter to exit ... ")
