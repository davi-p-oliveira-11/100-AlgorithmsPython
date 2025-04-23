'''
  57) Develop an application that reads the salary and gender of several employees.
     At the end, display the total salary paid to men and the total paid to women.
     The program will ask the user if they want to continue each time it reads the data of an employee.
'''

total_salary_men = 0
total_salary_women = 0

while True:
    salary = float(input("Enter the employee's salary: "))
    gender = input("Enter the employee's gender (M/F): ").upper()

    if gender == 'M':
        total_salary_men += salary
    elif gender == 'F':
        total_salary_women += salary
    else:
        print("Invalid gender input. Please enter 'M' or 'F'.")
        continue

    continue_input = input("Do you want to enter another employee? (Y/N): ").upper()
    if continue_input != 'Y':
        break

print(f"Total salary paid to men: {total_salary_men}")
print(f"Total salary paid to women: {total_salary_women}")


input("Press Enter to exit ... ")