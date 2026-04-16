# Loop (Infinite loop)
    # Ask user: roll the dice?
    # If user enters y
    #   Generate 2 random numbers
    #   Print the numbers
    # If user enters n
    #   Print thankyou message
    #   Terminate the program
    # Else
    #  Invalid choice


import random  # random - module

while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        # randint-function that generayes random no from range
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1}, {die2})')
    elif choice == 'n':
        print('Thanks for playing!')
        break
    else:
        print('Invalid choice!')
