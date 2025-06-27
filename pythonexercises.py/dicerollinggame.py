import random

while True:
    choice = input("Roll the dice? (yes/no): ").strip().lower()
    if choice == 'yes':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print("You rolled:")
        print(f'({dice1}, {dice2})')

        total = dice1 + dice2
        if total == 7:
            print("winner winner chicken dinner!!")
            if dice1 == dice2:
                print("draw")

        else:
            print("Not a winner this time. Try again!")
    elif choice == 'no':
        print("Exiting the game. Goodbye!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
# if user enters yes, roll two dice and print the result
# if user enters no, exit the game
# else print invalid input
# repeat the process in an infinite loop until the user chooses to exit
# wanna have a winner
