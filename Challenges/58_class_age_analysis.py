'''
 58) Create an algorithm that reads the age of several students in a class. 
     The program will stop when the age 999 is entered.
     At the end, display how many students are in the class and the average age of the group.
'''

total_students = 0
total_age = 0

while True:
    age = int(input("Enter the student's age (Enter 999 to stop): "))

    if age == 999:
        break

    total_students += 1
    total_age += age

average_age = total_age / total_students if total_students > 0 else 0

print(f"Total students in class: {total_students}")
print(f"Average age of the group: {average_age:.1f}")


input("Press Enter to exit ... ")