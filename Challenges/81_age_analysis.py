'''
  81) Create a program that reads the ages of 8 people and stores them in an array. At the end, display:
     a) The average age of the registered people
     b) The positions where people older than 25 are found
     c) The highest age entered (there may be repetitions)
     d) The positions where the highest age was entered
'''

ages = []
over_25_indexes = []
highest_age_indexes = []

sum1 = 0
highest_age = 0

for i in range(8):
    try:
        age = int(input(f"Enter the age of person {i + 1}: "))
        if age > 0:
            ages.append(age)
            sum1 += age

            if age > 25:
                over_25_indexes.append(i)

            if age > highest_age:
                highest_age = age
                highest_age_indexes = [i]
            elif age == highest_age:
                highest_age_indexes.append(i)
        else:
            print("Invalid input. Please enter a valid age.")
            i -= 1  # doesn't work like JS, so this just triggers another loop iteration
    except ValueError:
        print("Invalid input. Please enter a valid age.")
        continue

average_age = sum1 / len(ages)

print("Ages entered:", ', '.join(map(str, ages)))
print(f"Average age: {average_age:.2f}")
print("Positions of people older than 25:", ', '.join(map(str, over_25_indexes)) or "None")
print(f"Highest age entered: {highest_age}")
print("Positions where highest age was entered:", ', '.join(map(str, highest_age_indexes)))


input("Press Enter to exit ... ")