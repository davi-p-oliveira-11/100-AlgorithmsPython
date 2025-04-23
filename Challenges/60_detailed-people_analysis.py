'''
60) Develop an algorithm that reads the name, age, and gender of several people.
The program will ask the user if they want to continue. At the end, display:
a) The name of the oldest person
b) The name of the youngest woman
c) The average age of the group
d) How many men are older than 30
e) How many women are younger than 18
'''

oldest_person_name = ''
oldest_person_age = float('-inf')
youngest_woman_name = ''
youngest_woman_age = float('inf')
total_age = 0
total_people = 0
men_older_than_30 = 0
women_younger_than_18 = 0

while True:
    name = input("Enter the person's name: ")
    age = int(input("Enter the person's age: "))
    gender = input("Enter the person's gender (M/F): ").strip().upper()

    total_people += 1
    total_age += age

    if age > oldest_person_age:
        oldest_person_age = age
        oldest_person_name = name

    if gender == 'F' and age < youngest_woman_age:
        youngest_woman_age = age
        youngest_woman_name = name

    if gender == 'M' and age > 30:
        men_older_than_30 += 1

    if gender == 'F' and age < 18:
        women_younger_than_18 += 1

    continue_input = input("Do you want to enter another person? (Y/N): ").strip().upper()
    if continue_input != 'Y':
        break

average_age = total_age / total_people if total_people > 0 else 0

print(f"Oldest person: {oldest_person_name} ({oldest_person_age} years old)")

if youngest_woman_name:
    print(f"Youngest woman: {youngest_woman_name} ({youngest_woman_age} years old)")
else:
    print("No women registered.")

print(f"Average age of the group: {average_age:.2f}")
print(f"Men older than 30: {men_older_than_30}")
print(f"Women younger than 18: {women_younger_than_18}")


input("Press Enter to Exit ... ")