'''
  62) Create a program using the "do while" loop that reads the age of multiple people. 
  In each loop iteration, ask the user if they want to continue entering data.
At the end, when the user decides to stop, display:
a) The total number of ages entered
b) The average of the entered ages
c) How many people are 21 years old or older
'''

total_ages = 0
sum_ages = 0
count_21_or_older = 0

while True:
    age = int(input("Enter the person's age: "))

    total_ages += 1
    sum_ages += age

    if age >= 21:
        count_21_or_older += 1

    continue_input = input("Do you want to enter another age? (Y/N): ").upper()
    if continue_input != 'Y':
        break

average_age = sum_ages / total_ages if total_ages > 0 else 0

print(f"Total ages entered: {total_ages}")
print(f"Average age: {average_age:.2f}")
print(f"Number of people 21 or older: {count_21_or_older}")


input("Press Enter to exit ... ")