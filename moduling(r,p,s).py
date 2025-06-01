import random
choices = ('r','p','s')
emojies = { 'r': '🪨🪨',
            'p' : '📄📄',
            's' : '✂️✂️' }
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
    elif  ((user_choice =='r' and computer_choice=='s') 
        or (user_choice =='s' and computer_choice=='p') 
        or (user_choice =='p' and computer_choice=='r')):
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