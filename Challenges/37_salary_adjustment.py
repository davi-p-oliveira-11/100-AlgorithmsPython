'''
  37) A company needs to adjust its employees' salaries by giving a raise based on certain factors. 
Write a program that reads the current salary, the employee's gender, 
and how many years they have worked at the company. 
In the end, display their new salary based on the following table: Women

Less than 15 years at the company: +5%
From 15 to 20 years at the company: +12%
More than 20 years at the company: +23%
Men

Less than 20 years at the company: +3%
From 20 to 30 years at the company: +13%
More than 30 years at the company: +25%

'''

# Salary Adjustment Program

current_salary = float(input("Enter the employee's current salary: "))

gender = input("Enter the employee's gender (M for Male, F for Female): ").upper()

years_worked = int(input("Enter the number of years the employee has worked at the company: "))

new_salary = current_salary
percentage_increase = 0

if gender == 'F':
    if years_worked < 15:
        percentage_increase = 5
    elif years_worked <= 20:
        percentage_increase = 12
    else:
        percentage_increase = 23
elif gender == 'M':
    if years_worked < 20:
        percentage_increase = 3
    elif years_worked <= 30:
        percentage_increase = 13
    else:
        percentage_increase = 25
else:
    print("Error: Please enter a valid gender (M or F).")
    exit()

new_salary += (new_salary * percentage_increase) / 100

print(f"The employee's previous salary was R${current_salary:.2f}")
print(f"With an increase of {percentage_increase}%, the new salary is R${new_salary:.2f}")



input("Press Enter to exit ... ")