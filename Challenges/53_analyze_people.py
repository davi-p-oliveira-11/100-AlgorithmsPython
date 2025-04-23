'''
  53) Create a program that reads the age and gender of 5 people, displaying at the end:
a) How many men were registered
b) How many women were registered
c) The average age of the group
d) The average age of the men
e) How many women are older than 20
'''

counter = 0
sum_ages = 0
sum_men_ages = 0
men_count = 0
women_count = 0
women_above_20 = 0

while counter < 5:
    age = int(input(f"Enter the age of person {counter + 1}: "))
    gender = input(f"Enter the gender of person {counter + 1} (M/F): ").strip().upper()

    sum_ages += age

    if gender == 'M':
        men_count += 1
        sum_men_ages += age
    elif gender == 'F':
        women_count += 1
        if age > 20:
            women_above_20 += 1

    counter += 1

average_age = sum_ages / 5
average_men_age = sum_men_ages / men_count if men_count > 0 else 0

print(f"\nMen registered: {men_count}")
print(f"Women registered: {women_count}")
print(f"Average age of the group: {average_age:.1f}")
print(f"Average age of the men: {average_men_age:.1f}")
print(f"Women older than 20: {women_above_20}")


input("Press Enter to exit ... ")
  