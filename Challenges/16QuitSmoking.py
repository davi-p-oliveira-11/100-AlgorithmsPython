'''
 16) [CHALLENGE] Write a program to calculate the reduction in life expectancy of a smoker. 
 Ask for the number of cigarettes smoked per day and how many years they have smoked. 
 Consider that a smoker loses 10 minutes of life for each cigarette. Calculate 
 how many days of life a smoker will lose and display the total in days.
'''

cigars_per_day = int(input('How many cigarettes do you smoke per day ?'))
years_smoking = int(input("How many years have you been smoking ?"))

total_cigars = (cigars_per_day * 365) * years_smoking

minutes_lost = total_cigars * 10

days_lost = minutes_lost / 1440

print(f'You have already lost {days_lost:.1f} days of life !')