'''
19) Create an algorithm that reads a student's name and two grades, 
calculates their average, and displays it on the screen. 
In the end, analyze the average and show whether 
the student had good performance (if it was above the average of 7.0).
'''

grade_1 = float(input("Enter first exam grade: "))
grade_2 = float(input("Enter second exam grade: "))
average = (grade_1 + grade_2) / 2

print(f"The student average is: {average:.1f}")

if (average >= 7):
  print("Student Passed !")
else:
  print("Student Failed !")

input("Press Enter to Exit ... ")