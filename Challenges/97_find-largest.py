'''
   97) Redo exercise 91, but now as a function Greatest(). 
  Modify it to receive three numbers as parameters and return the largest among them.
'''


def greatest(num1: float, num2: float, num3: float) -> float:
    return max(num1, num2, num3)

try:
    input1 = float(input("Enter the first number: "))
    input2 = float(input("Enter the second number: "))
    input3 = float(input("Enter the third number: "))

    largest = greatest(input1, input2, input3)
    print(f"The largest number is: {largest}")
except ValueError:
    print("Invalid input. Please enter valid numbers.")

