'''
  90) Develop an algorithm that reads two values from the keyboard and passes them to a procedure 
   `Adder()`, which will calculate and display their sum.  
'''

def adder(value1: float, value2: float) -> None:
    sum_ = value1 + value2
    print(f"The sum of {value1} and {value2} is: {sum_}")

try:
    input1 = float(input('Enter the first value: '))
    input2 = float(input('Enter the second value: '))
    adder(input1, input2)
except ValueError:
    print('Invalid input. Please enter valid numbers.')


input("Press Enter to exit ... ")