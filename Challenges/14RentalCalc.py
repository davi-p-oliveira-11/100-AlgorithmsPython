'''
 14) The car rental company needs your help to charge for its services. 
 Write a program that asks for the number of kilometers driven by a rented car 
 and the number of days it was rented. Calculate the total price to be paid, 
 knowing that the car costs $90 per day and $0.20 per kilometer driven."
'''

distance_traveled = int(input("How many kilometers were traveled with the car ? "))
days_rented = int(input("For how many days was the car rented ? "))

cost_per_day = days_rented * 90
cost_per_distance = distance_traveled * 0.2
total_cost = cost_per_day + cost_per_distance

print(f'''
  The customer traveled {distance_traveled} km with the car, 
and rented the car for {days_rented} days, and it will cost {cost_per_day} USD
for the days rented, and {cost_per_distance:.2f} USD for the distance traveled
The total cost that the customer will pay is {total_cost:.2f} USD.
''')

input("Press Enter to Exit ... ")