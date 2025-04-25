'''
 100) Improve exercise 96 by creating, in addition to the Average() function, 
  another function called Situation(), which will return to the main program 
  whether the student is APPROVED, in RECOVERY, or FAILED. 
  This new function will receive as a parameter the result returned by the Average() function.
'''

def average(grade1: float, grade2: float) -> float:
    return (grade1 + grade2) / 2

def situation(average: float) -> str:
    if average >= 7:
        return 'APPROVED'
    elif average >= 4:
        return 'RECOVERY'
    else:
        return 'FAILED'

try:
    grade1 = float(input("Enter the first grade: "))
    grade2 = float(input("Enter the second grade: "))

    avg = average(grade1, grade2)
    situ = situation(avg)

    print(f"The average of the grades is: {avg}")
    print(f"The student is: {situ}")
except ValueError:
    print("Invalid input. Please enter valid grades.")
