'''
   94) [CHALLENGE] Develop an application with a procedure called Fibonacci() that takes a single 
  integer parameter, indicating how many terms of the sequence should be displayed on the screen. 
  The procedure should receive this value and display the requested number of elements.

  Note: Use exercises 70 and 75 to help with the solution.

  Example:

  Fibonacci(5) will generate: 1 >> 1 >> 2 >> 3 >> 5 >> END
  Fibonacci(9) will generate: 1 >> 1 >> 2 >> 3 >> 5 >> 8 >> 13 >> 21 >> 34 >> END
'''

def fibonacci(n: int) -> None:
    a, b = 1, 1

    for i in range(1, n + 1):
        if i == n:
            print(f"{a} >> END")
        else:
            print(f"{a} >>", end=' ')
        a, b = b, a + b

try:
    num_terms = int(input("Enter the number of Fibonacci terms you want to display: "))
    if num_terms > 0:
        fibonacci(num_terms)
    else:
        print("Invalid input. Please enter a valid number.")
except ValueError:
    print("Invalid input. Please enter a valid number.")


fibonacci()

input("Press Enter to exit ... ")