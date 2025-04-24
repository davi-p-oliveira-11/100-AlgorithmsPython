'''
   95) Redo exercise 90, but now as a function called Adder(), which will receive two parameters 
  and return the sum of these values to the main program.
'''

def adder(value1: float, value2: float) -> float:
    return value1 + value2

try:
    input6 = input("Enter the first value: ")
    input7 = input("Enter the second value: ")

    num5 = float(input6)
    num6 = float(input7)

    result = adder(num5, num6)
    print(f"The sum of {num5} and {num6} is: {result}")
except ValueError:
    print("Invalid input. Please enter valid numbers.")


adder()

input("Press Enter to exit ... ")