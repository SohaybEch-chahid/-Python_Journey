import random

secret_number = random.randint(1, 100)
attempts = 7

print("=== Number Guessing Game ===")
print("I'm thinking of a number between 1 and 100.")
print("you have 7 attempts")

while attempts > 0:
    guess = int(input("Enter your guess: "))
    attempts -= 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed it in {7 - attempts} attempts.")
        break
else:
    print("The attempts are finished")
    print("Use a Binary Search pattern")
