'''
  99) Create a program that has a function called `Power()`, 
  which will receive two numerical parameters (base and exponent) 
  and calculate the result of exponentiation.  

  **Example:**  
  `Power(5,2)` will calculate **5² = 25**  
'''

def power(base: float, exponent: float) -> float:
    return base ** exponent

try:
    base = float(input("Enter the base number: "))
    exponent = float(input("Enter the exponent number: "))

    result = power(base, exponent)
    print(f"{base} raised to the power of {exponent} is: {result}")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
