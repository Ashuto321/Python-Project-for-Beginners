import random
ROCK = 'r'
SCISSOR = 's'
PAPER = 'p'

emojies = { ROCK: '🪨🪨', PAPER : '📄📄', SCISSOR : '✂️✂️' }
choices = tuple(emojies.keys())

def get_user_choice():
    while True:
        user_choice= input('Rock, Paper, Scissors? (r/p/s): ').lower()
        if user_choice not in choices:
            print("Invalid")
        else:
            return user_choice
        
def display(user_choice, computer_choice):
    print(f'User_choices {emojies[user_choice]}')
    print(f'Computer_choices {emojies[computer_choice]}')

def main_game(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie!")
    elif  ((user_choice == ROCK and computer_choice== SCISSOR) 
        or (user_choice ==SCISSOR and computer_choice==PAPER) 
        or (user_choice ==PAPER and computer_choice==ROCK)):
        print("You win")
    else :
        print("You loose")


def play_game():
    
    while True:

        user_choice = get_user_choice()
        computer_choice= random.choice(choices)
        display(user_choice, computer_choice)
        main_game(user_choice, computer_choice)
        should_contnue = input("Enter if you wanna continue (y/n): ").lower()
        if should_contnue =='n':
            print("Thankyou for the game ❤️😊")
            break


# calling our game function:

play_game()