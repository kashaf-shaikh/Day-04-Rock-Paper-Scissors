import random
print(f"============ Number Guessing Battle ===============")
numbers = [1,2,3]

user_choice = int(input("choose a number from 1 to 3 :\n"))
if  1 <= user_choice <= 3:
    computer_number = random.randint(1,3)

    print(f"User Choice : {user_choice}")
    print(f"Computer Choice : {computer_number}")
    if user_choice == computer_number:
        print(f"It's Draw 😁")
    elif user_choice > computer_number:
        print("You win✅")
    else:
        print("you Loose❌")

else:
    print("An invalid choice !! number should be between 1-3 ")
