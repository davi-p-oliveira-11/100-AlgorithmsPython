'''
  24) Write an algorithm that asks for the distance a passenger wants
      to travel in Km. Calculate the ticket price, charging $0.50 per Km for
      trips up to 200Km and $0.45 for longer trips.
'''

distance_traveled = int(input(" How many kilometers will you travel ? "))

if distance_traveled <= 200:
  print(f"You will pay {distance_traveled * 0.5} USD")
else:
  print(f"You will pay {distance_traveled * 0.45} USD")


input("Press Enter to Exit ... ")