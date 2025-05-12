import random

number_to_guess=random.randint(1,100)

while True:
      
       try:
              user_input=int(input('Guess the number between 1 and 100: '))
              if user_input < number_to_guess:
                     print("too low")
              elif user_input > number_to_guess:
                     print('too high')
              else:
                     print(" congratulation! you guessed the number. ")
       except ValueError:
              print("Please enter a valid number")
