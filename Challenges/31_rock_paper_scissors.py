'''
  31) [CHALLENGE] Create a Rock-Paper-Scissors (JoKenPo) game.
'''
 
import random

choices = ['rock', 'paper', 'scissors']

user_choice = input('Choose Rock, Paper, or Scissors: ').lower()

if user_choice not in choices:
    print('Invalid choice! Please enter Rock, Paper, or Scissors.')
else:
    computer_choice = random.choice(choices)

    print(f'You chose: {user_choice}')
    print(f'Computer chose: {computer_choice}')

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        print('You win!')
    else:
        print('You lose!')


input("Press Enter to Exit ... ")