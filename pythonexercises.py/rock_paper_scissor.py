import random

# Rock Paper Scissors Game
choices = ["rock", "paper", "scissors"]

print("Welcome to the Rock Paper Scissors Game! Let's play! 🎮")

while True:
    user_input = input(
        "Choose your weapon (rock, paper, scissors): ").strip().lower()

    if user_input not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)
    print(f"You chose: {user_input}, computer chose: {computer_choice}")

    if user_input == computer_choice:
        print("It's a draw 🤝, no winner this time.")
    elif (user_input == "rock" and computer_choice == "scissors") or \
         (user_input == "paper" and computer_choice == "rock") or \
         (user_input == "scissors" and computer_choice == "paper"):
        print("YOU WIN 🎉 Chicken for dinner!")
    else:
        print("COMPUTER WINS! 😈")

    play_again = input("Do you wanna go again? (yes/no): ").strip().lower()
    if play_again == "yes":
        print("Alright, let's go again!")
    elif play_again == "no":
        print("quack quack ,See you next time!")
        break
    else:
        print("Not a clear answer. Exiting the game.")
        break
