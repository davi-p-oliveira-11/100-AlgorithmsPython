'''
  82) Create an algorithm that reads the grades of 10 students in a class and stores them in an array. At the end, display:
     a) The class average
     b) How many students scored above the class average
     c) The highest grade entered
     d) The positions where the highest grade appears
'''

grades = []
above_average_indexes = []
highest_grade_indexes = []

sum2 = 0
highest_grade = 0

i = 0
while i < 10:
    try:
        grade = float(input(f"Enter the grade of student {i + 1}: "))
        if 0 <= grade <= 10:
            grades.append(grade)
            sum2 += grade

            if grade > highest_grade:
                highest_grade = grade
                highest_grade_indexes = [i]
            elif grade == highest_grade:
                highest_grade_indexes.append(i)
            
            i += 1
        else:
            print("Invalid input. Please enter a valid grade between 0 and 10.")
    except ValueError:
        print("Invalid input. Please enter a valid grade between 0 and 10.")

class_average = sum2 / len(grades)

for index, grade in enumerate(grades):
    if grade > class_average:
        above_average_indexes.append(index)

print("Grades entered:", ', '.join(f"{g:.2f}" for g in grades))
print(f"Class average: {class_average:.2f}")
print(f"Students who scored above the average: {len(above_average_indexes)}")
print("Positions of these students:", ', '.join(map(str, above_average_indexes)) or "None")
print(f"Highest grade entered: {highest_grade}")
print("Positions where highest grade was entered:", ', '.join(map(str, highest_grade_indexes)))


input("Press Enter to exit ... ")