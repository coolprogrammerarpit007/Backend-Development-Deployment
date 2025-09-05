from random import randint

random_number = randint(1,50)
print(f"Random Choice: {random_number}")
user_guesses = 0
max_guesses = 5

while user_guesses < max_guesses:
    print("**** Think Smart and Enter Your Choice *******")
    user_choice = int(input("Enter your choice: "))

    if user_choice == random_number:
        print("****** Winner Winner Chicken Dinner ***********")
        print(f"You have won the game! you took {user_guesses} guesses to find thr right Number")
        break

    elif user_choice != random_number:
        if user_choice > random_number:
            print("Too High! Choose little small guess")

        else:
             print("Too Low! Choose Higher guess")

        user_guesses += 1

    else:
        print("Wrong Input and Choice, Wasted Chance")
        user_guesses += 1


if max_guesses < user_guesses:
    print("Sorry, You lose the game!")