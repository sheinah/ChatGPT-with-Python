import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

# Set the maximum number of attempts
max_attempts = 10

# Loop through the attempts
for attempt in range(1, max_attempts + 1):
    # Prompt the user to guess the number
    guess = int(input("Guess the random number between 1 and 100: "))

    # Provide feedback on the guess
    if guess < random_number:
        print("Too low!")
    elif guess > random_number:
        print("Too high!")
    else:
        print("Correct!")
        break

# If the user didn't guess the number within the allowed attempts, reveal the correct number
if guess != random_number:
    print("You lose! The correct number was", random_number)
else:
    print("You win!")
