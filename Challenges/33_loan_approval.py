'''
 33) Develop a program to determine if a home loan should be approved. 
    The program should ask for the home price, the buyer's income, and the loan term in years. 
    Calculate the monthly payment. 
    If the monthly payment is more than 30% of the buyer's income, deny the loan.
'''

house_value = float(input('Enter house price: '))
salary = float(input('Enter the value of your salary: '))
years_paying = int(input('In how many years do you intend to pay off the house? '))

months = years_paying * 12
installment = house_value / months

if installment > salary * 0.3:
    print('Unfortunately, we cannot grant you the loan.')
else:
    print('Congratulations, your loan has been approved!')


input("Press Enter to exit ... ")