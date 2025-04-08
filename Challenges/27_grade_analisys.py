"""
27) Write a program that calculates a student's average grade from two scores 
and displays a message based on that average:

Below 5.0: "Failed"
5.0 to 6.9: "Needs Improvement" (OR "Recovery Course Required")
7.0 or higher: "Passed"
"""

test_1 = float(input("Type the grade for the first test: "))
test_2 = float(input("Type the grade for the second test: "))

average = (test_1 + test_2) / 2

if average < 5.0:
    print(f"The student scored an average of {average:.1f} and Failed!")
elif 5.0 <= average <= 6.9:
    print(f"The student scored an average of {average:.1f} and needs to do the final exam!")
else:
    print(f"The student scored an average of {average:.1f} and Passed!")

input("Press Enter to exit... ")
