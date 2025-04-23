'''
54) Develop a program that reads the weight and height of 7 people, displaying at the end:

a) What was the average height of the group
b) How many people weigh more than 90 kg
c) How many people who weigh less than 50 kg are shorter than 1.60 m
d) How many people who are taller than 1.90 m weigh more than 100 kg
'''

counter = 0
sum_heights = 0
count_people_over_90kg = 0
count_under_50kg_under_160m = 0
count_over_190m_over_100kg = 0

while counter < 7:
    weight = float(input(f"Enter the weight (kg) of person {counter + 1}: "))
    height = float(input(f"Enter the height (m) of person {counter + 1}: "))

    sum_heights += height

    if weight > 90:
        count_people_over_90kg += 1

    if weight < 50 and height < 1.6:
        count_under_50kg_under_160m += 1

    if height > 1.9 and weight > 100:
        count_over_190m_over_100kg += 1

    counter += 1

average_height = sum_heights / 7

print(f"\nAverage height of the group: {average_height:.2f}m")
print(f"People weighing more than 90Kg: {count_people_over_90kg}")
print(f"People under 50Kg and shorter than 1.60m: {count_under_50kg_under_160m}")
print(f"People taller than 1.90m and heavier than 100Kg: {count_over_190m_over_100kg}")


input("Press Enter to exit ... ")