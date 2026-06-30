import random

print("🎮 Welcome to the Mind-Blowing Number Guessing Game!")
print("I have chosen a number between 1 and 100... Can you guess it?")

# AI secretly picks a number
secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess < secret_number:
        print("Too low! Try again 🔽")
    elif guess > secret_number:
        print("Too high! Try again 🔼")
    else:
        print(f"🎉 Correct! The number was {secret_number}.")
        print(f"You guessed it in {attempts} attempts!")
        break

