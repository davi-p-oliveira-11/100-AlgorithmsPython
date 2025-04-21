'''
 36) A healthy lifestyle program wants to award points for physical activities that can be exchanged for money. 
The system works as follows:
Each hour of physical activity in the month is worth points.
Up to 10 hours of activity in the month: earn 2 points per hour.
From 10 to 20 hours of activity in the month: earn 5 points per hour.
Above 20 hours of activity in the month: earn 10 points per hour.
For every point earned, the customer makes R$0.05 (5 cents). 

Write a program that reads how many hours of activity a person had in the month, calculates, 
and shows how many points they earned and how much money they managed to make.
'''


hours_of_activity = float(input('Enter the number of hours of physical activity this month: '))

points_earned = 0
money_earned = 0

if hours_of_activity <= 10:
    points_earned = hours_of_activity * 2
elif hours_of_activity <= 20:
    points_earned = 10 * 2 + (hours_of_activity - 10) * 5
else:
    points_earned = 10 * 2 + 10 * 5 + (hours_of_activity - 20) * 10

money_earned = points_earned * 0.05

print(f'You performed {hours_of_activity} hours of physical activity.')
print(f'You earned a total of {points_earned} points.')
print(f'You will receive R${money_earned:.2f} as a reward.')



input("Press Enter to exit ... ")

