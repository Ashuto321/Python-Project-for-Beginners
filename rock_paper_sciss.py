import random
choices = ('r','p','s')
emojies = { 'r': '🪨🪨',
            'p' : '📄📄',
            's' : '✂️✂️' }
#Ask te user to make a choice 
while True:
    user_choice= input('Rock, Paper, Scissors? (r/p/s): ').lower()
    # if choice is not valid
    if user_choice not in choices:
    # if user_choice != 'r' and user_choice != 'p' and user_choice!='s':
    # print an error
        print("Invalid")
        continue
    # let the computer to make a choice 
    computer_choice= random.choice(choices) # using this you can have choice from choices array
    # same as we use it with the random.randint() function.
    # using string formatting in the pint statement

    # we will asssociate and use dictionary for providing the choices:

    # print choices (emojies)
    print(f'User_choices {emojies[user_choice]}')
    print(f'Computer_choices {emojies[computer_choice]}')

    # determine the winner
    if user_choice == computer_choice:
        print("Tie!")
    elif  ((user_choice =='r' and computer_choice=='s') 
        or (user_choice =='s' and computer_choice=='p') 
        or (user_choice =='p' and computer_choice=='r')):
        print("You win")
    else :
        print("You loose")

    # ask the user is they want to continue
    should_contnue = input("Enter if you wanna continue (y/n): ").lower()
    if should_contnue =='n':
    # if not
    #   terminate 
        print("Thankyou for the game ❤️😊")
        break

