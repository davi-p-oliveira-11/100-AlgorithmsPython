'''
   32) [CHALLENGE] Create a game where the computer will randomly choose a number 
       between 1 and 5 and the player will try to guess which number was chosen.
'''

import random

player_number = int(input("'Enter a number: "))
computer_number = random.randint(1, 5)

print(f"Player choice was {player_number}")
print(f"Computer choice was {computer_number}")

if player_number == computer_number:
  print("Congratulations you won !")
else:
  print("You Lose !")


input("Press Enter to Exit ... ")