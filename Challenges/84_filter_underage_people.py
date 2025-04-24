'''
  84) Create a program that reads the name and age of 9 people and stores these values in two arrays, 
 keeping them in corresponding positions. 
 In the end, display a list containing only the data of people who are underage.
'''

names2 = []
ages2 = []
minors = []

for i in range(9):
    name = input(f"Enter the name of person {i + 1}: ").strip()
    age_input = input(f"Enter the age of person {i + 1}: ").strip()

    try:
        age = int(age_input)
        if name and age > 0:
            names2.append(name)
            ages2.append(age)
            if age < 18:
                minors.append(f"{name} (Age: {age})")
        else:
            print("Invalid input. Please enter a valid name and age.")
            i -= 1
    except ValueError:
        print("Invalid input. Please enter a valid name and age.")
        i -= 1

if minors:
    print("People underage:")
    for minor in minors:
        print(minor)
else:
    print("No minors found.")


input("Press Enter to exit ... ")