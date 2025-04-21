'''
 35) A car rental company needs to charge for its services. 
Renting a popular car costs R$90 per day, and a luxury car costs R$150 per day. 
Additionally, the customer pays per kilometer driven. 
Create a program that reads the type of car rented (popular or luxury), 
the number of rental days, and the number of kilometers driven. 
At the end, display the price to be paid according to the following table:

Popular cars (90USD rental per day)
Up to 100km driven: 0.20USD per km
Over 100km driven: 0.10USD per km
Luxury cars (150USD rental per day)
Up to 100km driven: 0.30USD per km
Over 100km driven: 0.25USD per km
'''


rented_car = input(
    'Would you like to rent a Popular or Luxury car? Enter P for Popular and L for Luxury: '
).upper()

days_rented = int(input('For how many days did you use the car? '))
distance_traveled = float(input('Enter how many kilometers were driven with the car: '))

price_for_days_rented_popular = days_rented * 90
price_for_days_rented_luxury = days_rented * 150

popular_fare1 = distance_traveled * 0.2
popular_fare2 = distance_traveled * 0.1
luxury_fare1 = distance_traveled * 0.3
luxury_fare2 = distance_traveled * 0.25

if rented_car != 'P' and rented_car != 'L':
    print('Error: Please enter a valid car category.')
elif rented_car == 'P' and distance_traveled >= 100:
    print(f'You rented a Popular car for {days_rented} days.')
    print(f'Traveled {distance_traveled} km with the car.')
    print(f'You will pay a total of {price_for_days_rented_popular + popular_fare1:.2f} USD.')
elif rented_car == 'P' and distance_traveled < 100:
    print(f'You rented a Popular car for {days_rented} days.')
    print(f'Traveled {distance_traveled} km with the car.')
    print(f'You will pay a total of {price_for_days_rented_popular + popular_fare2:.2f} USD.')
elif rented_car == 'L' and distance_traveled >= 100:
    print(f'You rented a Luxury car for {days_rented} days.')
    print(f'Traveled {distance_traveled} km with the car.')
    print(f'You will pay a total of {price_for_days_rented_luxury + luxury_fare1:.2f} USD.')
elif rented_car == 'L' and distance_traveled < 100:
    print(f'You rented a Luxury car for {days_rented} days.')
    print(f'Traveled {distance_traveled} km with the car.')
    print(f'You will pay a total of {price_for_days_rented_luxury + luxury_fare2:.2f} USD.')



input("Press Enter to exit ... ")