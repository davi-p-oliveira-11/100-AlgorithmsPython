'''
   98) Create a program that has a function SuperAdder(), which will receive two numbers 
  as parameters and return the sum of all values in the range between the received numbers.

  Example:
  SuperAdder(1, 6) will sum 1 + 2 + 3 + 4 + 5 + 6 and return 21
  SuperAdder(15, 19) will sum 15 + 16 + 17 + 18 + 19 and return 85
'''

def super_adder(start: int, end: int) -> int:
    total = 0
    for i in range(start, end + 1):
        total += i
    return total

try:
    start_number = int(input("Enter the start number: "))
    end_number = int(input("Enter the end number: "))

    result = super_adder(start_number, end_number)
    print(f"The sum of all numbers between {start_number} and {end_number} is: {result}")
except ValueError:
    print("Invalid input. Please enter valid numbers.")


input("Press Enter to exit ... ")