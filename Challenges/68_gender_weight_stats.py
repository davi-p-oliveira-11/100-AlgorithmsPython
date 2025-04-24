'''
  68) Create a program that reads the gender and weight of 8 people using the "for" loop. 
 At the end, display:
     a) How many women were registered
     b) How many men weigh more than 100Kg
     c) The average weight of the women
     d) The highest weight among the men
'''

class Person:
    def __init__(self, gender, weight):
        self.gender = gender
        self.weight = weight

people = []

for i in range(8):
    gender = input(f'Enter gender for person {i + 1} (M/F): ').upper()
    weight = float(input(f'Enter weight for person {i + 1}: ') or '0')

    people.append(Person(gender, weight))

women_count = 0
men_over_100kg = 0
women_weight_sum = 0
heaviest_man = 0

for person in people:
    if person.gender == 'F':
        women_count += 1
        women_weight_sum += person.weight
    else:
        if person.weight > 100:
            men_over_100kg += 1
        if person.weight > heaviest_man:
            heaviest_man = person.weight

women_average_weight = women_weight_sum / women_count if women_count > 0 else 0

print(f'Number of women registered: {women_count}')
print(f'Number of men weighing more than 100Kg: {men_over_100kg}')
print(f'Average weight of the women: {women_average_weight:.2f} Kg')
print(f'Highest weight among the men: {heaviest_man} Kg')


input("Press Enter to exit ... ")