def computer_guesses_number():
    print("🔢 Think of a number between 1 and 100, and I will try to guess it!")
    low = 1
    high = 100
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        print(f"My guess is: {guess}")
        feedback = input("Is it (h)igh, (l)ow, or (c)orrect? ").strip().lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"🎉 Yay! I guessed your number in {attempts} attempts.")
            break
        else:
            # print
            print("Please enter H, L, or C.")

computer_guesses_number()
