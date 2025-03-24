'''
21) Write an algorithm that reads a specific year and shows whether it is a LEAP YEAR or not."
'''

year = int(input("Enter a year: "))

if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
  print(f"{year} is leap.")
else:
  print(f"{year} is not leap")

input("Press Enter to Exit ... ")