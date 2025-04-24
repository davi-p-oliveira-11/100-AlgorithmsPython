'''
  96) Create a program that has a function Average(), which will receive two grades 
      from a student and return their average to the main program.
'''

def average(grade1: float, grade2: float) -> float:
    return (grade1 + grade2) / 2

try:
    input1 = float(input("Enter the first grade: "))
    input2 = float(input("Enter the second grade: "))
    
    avg = average(input1, input2)
    print(f"The average of the grades is: {avg}")
except ValueError:
    print("Invalid input. Please enter valid grades.")


input("Press Enter to exit ... ")