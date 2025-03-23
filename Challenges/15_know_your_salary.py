'''
15) Create a program that reads the number of days worked in a month and displays the employee's salary, 
knowing that they work 8 hours per day and earn R$25 per hour worked.
'''

days_worked = int(input("How many days did you work last month ?"))
day_of_work = 200
salary = days_worked * day_of_work

print(f'The employee worked for {days_worked} days and will receive a salary of {salary} USD')

input("Press Enter to Exit ... ")