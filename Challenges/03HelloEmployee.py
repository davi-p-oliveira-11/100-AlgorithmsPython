'''
3) Create a program that reads an employee's name and salary, and displays a message at the end.  
Example:  
Employee's Name: Maria do Carmo  
Salary: 1850.45  
The employee Maria do Carmo has a salary of R$1850.45 in June.
'''

name = input("What is the employee name ? ")
salary = input("How much is the employee salary ? ")
month = input("Last month worked ? ")

print(f'The employee {name} has a salary of {salary} in {month}')

input("Press enter to exit ... ")