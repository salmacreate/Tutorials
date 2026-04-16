# Ask the user to make a choice
# If choice is not valid
#   Print an error
# Let the computer make a choice
# Print choices(emojis)
# Determine winner
# Ask user if they want to continue
# If not
#    Terminate

import random

# DRY - Don't Repeat Yourself
# Declare constants
ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'

# Dictionary used to map key to a value
emojis = {ROCK: '🪨', SCISSORS: '✂️', PAPER: '📃'}
choices = tuple(emojis.keys()) # convert to tuple as tuples are read only hence cannot be modified unintentionally


def get_user_choice():
    while True:
        user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid choice!')


def display_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == PAPER) or
            (user_choice == PAPER and computer_choice == ROCK)):
        print('You win')
    else:
        print('You lose')


def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        should_continue = input('Continue? (y/n): ').lower()
        if should_continue == 'n':
            break


play_game()
