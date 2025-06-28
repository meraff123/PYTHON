import random

print("Welcome to Guess the Number Game!")

while True:  # Main game loop
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0

    print("I have selected a number between 1 and 100. Can you guess it?")

    # Game logic loop
    while attempts < max_attempts:
        print(f"You have {max_attempts - attempts} attempts left.")
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 100:
                print("Guess is out of range. Please enter a number between 1 and 100.")
                continue
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(
                f"🎉 Congratulations! You guessed the number in {attempts} attempts!")
            break

    if attempts == max_attempts and guess != number_to_guess:
        print(
            f"❌ You've used all your attempts. The number was: {number_to_guess}")

    # Ask to play again
    # This loop allows the user to decide whether to play again or exit
    while True:  # Inner loop for playing again
        play_again = input(
            "Do you want to play again? (yes/no): ").strip().lower()
        if play_again in ("yes", "y"):
            print("Great! Let's play again.")
            break  # Breaks only from the inner 'play again' loop, game restarts
        elif play_again in ("no", "n"):
            print("Good game, quitting...")
            print("Thanks for playing! Goodbye!")
            exit()  # Ends the program
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue

    # This point is reached if the user chooses to play again
    print("Starting a new game...\n")
