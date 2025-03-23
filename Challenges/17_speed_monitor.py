'''
17) Write a program that asks for the speed of a car. 
If it exceeds 80 km/h, display a message saying that the user has been fined. 
In this case, display the amount of the fine, charging R$5 for each km above the allowed speed.
'''

car_speed = int(input("What speed did the car reach  ? "))

if (car_speed > 80):
  print(f'''The car reached a speed of {car_speed}, exceeding {car_speed - 80} km/h of the allowed speed, 
         The driver wiil have to pay a fine of {(car_speed - 80) * 5} USD)''')
else :
  print("The driver did not exceed the speed limit, so they will not have to pay a fine.")  

input("Press Enter to Exit ... ")