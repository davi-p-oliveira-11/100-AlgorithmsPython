'''
  91) Develop an algorithm that reads two values from the keyboard and passes them to a procedure 
  called Greatest() which will check which one is greater and display it on the screen. 
  If both values are equal, display a message informing this characteristic.
'''

def greatest(value1: float, value2: float) -> None:
    if value1 > value2:
        print(f"{value1} is greater than {value2}")
    elif value2 > value1:
        print(f"{value2} is greater than {value1}")
    else:
        print("Both values are equal.")

try:
    input1 = float(input("Enter the first value: "))
    input2 = float(input("Enter the second value: "))
    greatest(input1, input2)
except ValueError:
    print("Invalid input. Please enter valid numbers.")


greatest()


input("Press Enter to exit ... ")