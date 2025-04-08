"""
29) Develop a program that reads an employee's name, their salary, and how many years 
they have worked for the company. Then, display their new salary, adjusted according 
to the following table:

Up to 3 years at the company: 3% increase
Between 3 and 10 years: 12.5% increase
10 years or more: 20% increase 
"""

employee_name = input("Enter the name of the employee: ")
salary = float(input("Enter the salary amount: "))
years_worked = int(input("How many years have you worked at the company? "))

increase_3 = salary * 0.03
increase_12 = salary * 0.125
increase_20 = salary * 0.20

if years_worked < 3:
    new_salary = salary + increase_3
    print(f"The employee {employee_name} has worked for {years_worked} years.")
    print(f"They will receive a 3% raise, resulting in a new salary of {new_salary:.2f}.")

elif 3 <= years_worked < 10:
    new_salary = salary + increase_12
    print(f"The employee {employee_name} has worked for {years_worked} years.")
    print(f"They will receive a 12.5% raise, resulting in a new salary of {new_salary:.2f}.")

else:
    new_salary = salary + increase_20
    print(f"The employee {employee_name} has worked for {years_worked} years.")
    print(f"They will receive a 20% raise, resulting in a new salary of {new_salary:.2f}.")

input("Press Enter to Exit ... ")