'''
    1 for snake
    -1 for water
    0 for GUN
'''

import random

computer = random.choice([-1,0,1])
user = input("Enter your choice: ")
options = {"s":1,"w":-1,"g":0}
user_choice = options[user]

if user_choice == computer:
    print("Match Drawn!")
elif computer == -1 and user_choice == 1:
    print("User Wins")

elif computer == -1 and user_choice == 0:
    print("Computer Win!")

elif computer == 1 and user_choice == -1:
    print("Computer Win!")

elif computer == 1 and user_choice == 0:
    print("User Win!")

elif computer == 0 and user_choice == 1:
    print("Computer Win!")

elif computer == 0 and user_choice == -1:
    print("User Win!")

else:
    print("Something Wrong!")