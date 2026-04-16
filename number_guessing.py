#Generate random number
#loop
    #Ask user to make a guess
    #If not a valid number
    #   Print an error
    #If number < guess
    #   Print too low
    #If number > guess
    #   Print too high
    #ELse
    #   Print well done


import random

number_to_guess = random.randint(1, 100)

while True:
  try: #used to handle errors
    guess = int(input('Guess the number between 1 and 100: '))

    if guess < number_to_guess:
      print('Too low!')
    elif guess > number_to_guess:
      print('Too high!')
    else:
      print('Congratulations! You guessed the number.')
      break #breaks you out of loop
  except ValueError: #if code in try doesn't run this one runs intead of crashing 
    print('Please enter a valid number')
