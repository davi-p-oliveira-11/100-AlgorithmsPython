'''
   85) Create an algorithm that reads the name, gender, and salary of 5 employees and 
  stores these data in three separate arrays. 
  In the end, display a list containing only the data of female employees who earn more than R$5,000.
'''

names3 = []
genders = []
salaries = []
high_earning_women = []

for i in range(5):
    name = input(f"Enter the name of employee {i + 1}: ").strip()
    gender = input(f"Enter the gender of employee {i + 1} (M/F): ").strip()
    salary_input = input(f"Enter the salary of employee {i + 1}: ").strip()

    try:
        salary = float(salary_input)
        if name and gender and salary > 0:
            names3.append(name)
            genders.append(gender)
            salaries.append(salary)

            if gender.lower() == 'f' and salary > 5000:
                high_earning_women.append(f"{name} (Salary: R${salary:.2f})")
        else:
            print("Invalid input. Please enter a valid name, gender, and salary.")
            i -= 1
    except ValueError:
        print("Invalid input. Please enter a valid name, gender, and salary.")
        i -= 1

if high_earning_women:
    print("Female employees earning more than R$5,000:")
    for employee in high_earning_women:
        print(employee)
else:
    print("No female employees earning more than R$5,000.")


input("Press Enter to exit ... ")