'''
22) Write a program that reads a guy's birth year and displays his situation 
regarding military enlistment.

If he is under 18 years old, show how many years are left until enlistment.
If he is over 18 years old, show how many years have passed since enlistment.
'''


from datetime import datetime

year_of_birth = int(input("What year were you born ? "))
current_year = datetime.now().year
user_age = current_year - year_of_birth
years_remaining = max(0, 18 - user_age)
year_that_complete_18 = year_of_birth + 18
years_passed = current_year - year_that_complete_18

if (user_age < 18):
  print(f"You're not old enough to enlist yet. You'll have to wait {years_remaining} more years.")
elif (user_age == 18):
  print("You are the right age to enlist this year.")
else:
  print(f"You missed your enlistment by {years_passed}")


input("Press Enter to Exit ... ")