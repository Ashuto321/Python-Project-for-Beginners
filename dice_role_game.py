import random
# LOOP
while True:
       choice = input('Roll the dice?(y/n)').lower()
       if choice == 'y':
              die1=random.randint(1,6)#give the random number you want it to generate in betweeen 
              die2=random.randint(1,6)#give the random number you want it to generate in betweeen 
              print(f"({die1},{die2})")
       elif choice == 'n':
              print('Thnakyou for playing')
              break
       else:
              print("Invalid choice!")

