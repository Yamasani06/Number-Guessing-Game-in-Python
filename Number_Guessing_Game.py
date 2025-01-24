import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("-" * 50)
    # Define the range and generate a random number
    lb = 1 #lb defines lower_bound
    ub = 100 #ub defines upper_bound
    secret_number = random.randint(lb, ub)

    # Maximum number of attempts
    max_attempts = 10

    print(f"I'm thinking of a number between {lb} and {ub}.")
    print(f"You have {max_attempts} attempts to guess it!")

    for attempt in range(1, max_attempts + 1):
        try:
            # Prompt the player for their guess
            guess = int(input(f"Attempt {attempt}/{max_attempts}: Enter your guess: "))

            # Check if the guess is out of range
            if guess < lb or guess > ub:
                print(f"Please guess a number between {lb} and {ub}.")
                continue
             # Compare the guess with the secret number
            if guess == secret_number:
                print(f" Congratulations! You guessed the number {secret_number} in {attempt} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    else:
        print(f"Sorry, you've used all your attempts. The number was {secret_number}. Better luck next time!")

if __name__ == "__main__":
    number_guessing_game()