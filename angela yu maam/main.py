# 📝 Day 4 — Rock Paper Scissors
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissor = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
game_ascii = [rock,paper,scissor]
import random
user_choice = int(input("select what you want to play:\nRock: 0\nPaper: 1\nScissor: 2\nchoose:"))

if 0 <= user_choice <= 2:
    print(game_ascii[user_choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer's Choice:\n{game_ascii[computer_choice]}")

    if user_choice == 0 and computer_choice == 1:
        print("you loose 😣")
    elif user_choice == 0 and computer_choice == 2:
        print("you win 😊")
    elif user_choice == 1 and computer_choice == 0:
        print("you win 😊")
    elif user_choice == 1 and computer_choice == 2:
        print("you loose 😣")
    elif user_choice == 2 and computer_choice == 0:
        print("you loose 😣")
    elif user_choice == 2 and computer_choice == 1:
        print("you win 😊")
    else:
        print("Its draw!😂")

else:
    print("You Typed an Invalid Number. You Lose!")

