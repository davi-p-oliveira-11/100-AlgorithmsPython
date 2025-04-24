'''
  78) Write a program that reads 15 numbers and stores them in an array. 
    At the end, display the entire array on the screen and then show the 
    positions where values that are multiples of 10 were entered.
'''

numbers = []
multiples_of_ten_indexes = []

i = 0
while i < 15:
    try:
        input_value = input(f"Enter number {i + 1}: ")
        num = int(input_value)
        numbers.append(num)
        if num % 10 == 0:
            multiples_of_ten_indexes.append(i)
        i += 1
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("Numbers entered:", ', '.join(map(str, numbers)))
print("Positions of multiples of 10:", ', '.join(map(str, multiples_of_ten_indexes)))


input("Press Enter to exit ... ")