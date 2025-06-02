import random

def guessing_game():                            # Create a function named guessing_game
    target_number = random.randint(1, 100)      # Generate a random number between 1 and 100
    guess = 0
    number_guess = 1

    print(" ")
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number from 1 to 100.")

    while guess != target_number:
        try:
            guess = int(input("Enter your guess: "))
            if guess < target_number:
                print("Too low! Try again.")
                number_guess += 1
            elif guess > target_number:
                print("Too high! Try again.")
                number_guess += 1
            else:
                print(" ")
                print(
                    f"Congratulations! You guessed the number {target_number} correctly!")
                print(
                    f"It took you {number_guess} guesses.")
                print(" ")

        except ValueError:
            print("¯\_(ツ)_/¯")
            print("Please enter a valid number.")

if __name__ == "__main__":
    guessing_game()
