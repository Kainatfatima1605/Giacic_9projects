import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("🎯 Welcome to the Guess the Number Game!")
    print("I have chosen a number between 1 and 100.")

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

guess_the_number()
