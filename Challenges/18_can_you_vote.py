'''
18) Write a program that reads a person's year of birth, 
calculates their age, and then shows whether they are eligible to vote or not.
'''

from datetime import datetime

current_year = datetime.now().year
year_of_birth = int(input("What year were you born ? "))

age = current_year - year_of_birth;

if (age >= 16):
  print("You are already eligible to vote.")
else:
  print("You are not old enough to vote yet.")

input("Press Enter to Exit ... ")