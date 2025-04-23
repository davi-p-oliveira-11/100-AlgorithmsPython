'''
  55) [CHALLENGE] Let's improve the game we created in exercise 32. 
  From now on, the computer will randomly select a number between 1 and 10, 
  and the player will have 4 attempts to guess it.
'''

import random

computer_number = random.randint(1, 10)
attempts = 0
guessed_correctly = False

while attempts < 4:
    player_number = int(input(f"Attempt {attempts + 1}/4 - Enter a number between 1 and 10: "))
    print(f"Player choice was {player_number}")

    if player_number == computer_number:
        print("Congratulations, you won!")
        guessed_correctly = True
        break
    else:
        print("Wrong guess, try again!")

    attempts += 1

if not guessed_correctly:
    print(f"You lost! The correct number was {computer_number}.")


input("Press Enter to exit ... ")