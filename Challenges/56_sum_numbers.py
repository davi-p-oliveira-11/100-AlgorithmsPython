'''
  56) Create a program that reads several numbers from the keyboard and shows the sum of them at the end.
     Note: The program will stop when the number 1111 is entered.
'''

sum_ = 0

while True:
    number = int(input("Enter a number (1111 to stop): "))

    if number == 1111:
        break

    sum_ += number

print(f"The sum of all entered numbers is: {sum_}")


input("Press Enter to exit ... ")