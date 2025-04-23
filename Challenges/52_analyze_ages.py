'''
 52) Create an algorithm that reads the age of 10 people, displaying at the end:
a) The average age of the group
b) How many people are older than 18
c) How many people are younger than 5
d) The highest age recorded
'''

counter = 0
sum = 0
people_older_than_18 = 0
people_younger_than_5 = 0
highest_age = float('-inf')
ages = []

while counter < 10:
  age = int(input(f"Enter the age of person {counter + 1}: "))
  ages.append(age)
  sum += age

  if age > 18:
    people_older_than_18 += 1

  if age < 5:
    people_older_than_18 += 1

  if age > highest_age:
    highest_age = age

  counter += 1


average_age = sum / len(ages)

print(average_age)

print(f"Ages entered {ages}")
print(f"Average age: {average_age}")
print(f"People older than 18: {people_older_than_18}")
print(f"People younger than 5: {people_younger_than_5}")
print(f"Highest age recorded: {highest_age}")


input("Press Enter to exit ... ")
  