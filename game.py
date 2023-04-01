import random

number = random.randint(1, 100)
attempts = 6
print("I'm thinking of a number between 1 and 100. You have 6 attempts to guess it.")
while attempts > 0:
    guess = int(input("Guess the number: "))
    if guess == number:
        print("Congratulations! You guessed the number in", 6 - attempts + 1, "attempts.")
        break

    elif guess < number:
        print("Too low. You have", attempts - 1, "attempts left.")

    else:
        print("Too high. You have", attempts - 1, "attempts left.")

    attempts -= 1
if attempts == 0:
    print("Sorry, you ran out of attempts. The number was", number)
