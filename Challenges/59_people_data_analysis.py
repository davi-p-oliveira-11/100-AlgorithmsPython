'''
  59) Create a program that reads the gender and age of several people. 
 The program will ask the user if they want to continue after each person. 
 At the end, display:
  a) The highest age recorded
  b) The number of men registered
  c) The age of the youngest woman
  d) The average age among men
'''

highest_age = float('-inf')
men_count = 0
youngest_woman_age = float('inf')
total_men_age = 0
men_age_count = 0

while True:
    age = int(input("Enter the person's age: "))
    gender = input("Enter the person's gender (M/F): ").strip().upper()

    if age > highest_age:
        highest_age = age

    if gender == 'M':
        men_count += 1
        total_men_age += age
        men_age_count += 1
    elif gender == 'F' and age < youngest_woman_age:
        youngest_woman_age = age

    continue_input = input("Do you want to enter another person? (Y/N): ").strip().upper()
    if continue_input != 'Y':
        break

average_men_age = total_men_age / men_age_count if men_age_count > 0 else 0

if total_men_age > 0:
    print(f"Average age among men: {average_men_age:.2f}")
else:
    print("No men registered.")

if youngest_woman_age != float('inf'):
    print(f"Age of the youngest woman: {youngest_woman_age}")
else:
    print("No women registered.")

print(f"Highest age recorded: {highest_age}")
print(f"Number of men registered: {men_count}")


input("Press Enter to exit ... ")