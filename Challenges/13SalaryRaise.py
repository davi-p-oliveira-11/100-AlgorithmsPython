'''
13)Faça um algoritmo que leia o salário de um funcionário,
calcule e mostre o seu novo salário, com 15% de aumento.
'''

current_salary = float(input("Enter the value of your salary:  " ))
amount_of_raise = current_salary * 0.15
salary_with_raise = current_salary + amount_of_raise

print(f'Your new salary with a 15% increase is: {salary_with_raise} USD')

input('Press Enter to Exit ...')