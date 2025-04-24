''' 
  93) Create a program with a procedure called Counter() that takes three values as parameters:
  the start, the end, and the step of a count. 
  The main program should request these values from the user and pass them to the procedure,
  which will then display the count on the screen.
   Example:
   For the input values: start (4), end (20), and step (3), calling Counter(4, 20, 3) will display:
   4 >> 7 >> 10 >> 13 >> 16 >> 19 >> END
'''

def counter(start: int, end: int, step: int) -> None:
    for i in range(start, end + 1, step):
        if i + step <= end:
            print(f"{i} >>", end=' ')
        else:
            print(f"{i} >> END")

try:
    start = int(input("Enter the start value: "))
    end = int(input("Enter the end value: "))
    step = int(input("Enter the step value: "))

    counter(start, end, step)
except ValueError:
    print("Invalid input. Please enter valid numbers for start, end, and step.")


counter()

input("Press Enter to exit ... ")