from pylab import randint

print("This is a number guessing game. The number ranges from 1 to 100. Please type in a number of guesses.")
NumberGenerator = randint(1, 101)
guesses_left = int(input("How Many Guesses? "))  # Set the number of guesses allowed

while guesses_left > 0:
    try:
        guess = int(input("Take your guess: "))
        
        if guess < NumberGenerator:
            print("You are under the correct number.")
        elif guess > NumberGenerator:
            print("You are above the correct number.")
        else:
            print("You guessed the correct number, Congratulations!")
            break  # Exit the loop when the correct guess is made
        
        # Decrement the guesses left
        guesses_left -= 1
        print(f"Guesses left: {guesses_left}")

        if guesses_left == 0:
            print(f"Sorry, you've run out of guesses. The correct number was {NumberGenerator}.")
            break
    
    except ValueError:
        print("Please enter a valid number.")
