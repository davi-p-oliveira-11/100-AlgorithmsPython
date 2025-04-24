'''
   92) Create a logic that reads an integer and passes it to a procedure called EvenOrOdd() 
      which will check and display on the screen whether the value passed as a parameter is EVEN or ODD.
'''

def even_or_odd(value: int) -> None:
    if value % 2 == 0:
        print(f"{value} is EVEN.")
    else:
        print(f"{value} is ODD.")

try:
    num = int(input("Enter an integer: "))
    even_or_odd(num)
except ValueError:
    print("Invalid input. Please enter a valid integer.")


even_or_odd()

input("Press Enter to exit ... ")