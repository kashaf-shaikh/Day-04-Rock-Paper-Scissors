# Day 04 - Rock Paper Scissors

This is my Day 4 project from Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp.

In this project, I made a simple Rock Paper Scissors game using Python. The user plays against the computer, and the winner is decided based on the choices made by both players.

## About the Game

The game has three choices:

- Rock (0)
- Paper (1)
- Scissors (2)

The computer randomly selects one of these choices, and then the program compares both choices to decide the result.

### Game Rules

| User Choice | Computer Choice | Result |
|---|---|---|
| Rock | Scissors | You Win |
| Rock | Paper | You Lose |
| Paper | Rock | You Win |
| Paper | Scissors | You Lose |
| Scissors | Paper | You Win |
| Scissors | Rock | You Lose |
| Same choice | Same choice | Draw |

## Example

**Input:**

```text
Select what you want to play:

Rock: 0
Paper: 1
Scissor: 2

Choose: 0
```

**Output:**

```text
Your Choice:

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Computer's Choice:

     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

You Lose!
```

*The computer's choice and result can be different each time because its selection is random.*

## What I Learned

While making this project, I learned:

- Creating variables to store values.
- Using lists to store multiple items.
- Accessing list elements using their index.
- Importing the `random` module.
- Using `random.randint()` to generate a random number.
- Taking input from the user using `input()`.
- Converting input into an integer using `int()`.
- Using `if`, `elif` and `else` statements.
- Checking conditions using comparison operators.
- Using logical operators to compare choices.
- Displaying ASCII art in the terminal.

## Technologies Used

- Python 3
- PyCharm
- Git
- GitHub

## How to Run

1. Clone or download this repository.
2. Open the project folder in PyCharm or any Python editor.
3. Open the `main.py` file.
4. Run the program.
5. Select Rock, Paper or Scissors by entering 0, 1 or 2.
6. See the computer's choice and check the result.

You can also run it using the terminal:

```bash
python main.py
```

## Project Structure

```text
Day-04-Rock-Paper-Scissors/
│
├── main.py
│
└── README.md
```

## About My Learning

This is my fourth project in the 100 Days of Python course. I enjoyed making this game because I got to practise lists, random numbers and conditional statements together.

I will keep adding my daily Python projects to GitHub as I continue learning.