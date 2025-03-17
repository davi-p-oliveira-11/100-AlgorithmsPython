'''
5) Write a program that reads a student's two grades in a subject and displays their average for the subject.  
Example:  
Grade 1: 4.5  
Grade 2: 8.5  
The average of 4.5 and 8.5 is 6.5.
'''

grade1 = float(input("Enter the first grade: "))
grade2 = float(input("Enter the second grade: "))

average = (grade1 + grade2) / 2

print(f'The average between {grade1:.1f} and {grade2:.1f} is {average:.1f}')

input("Press enter to exit ... ")