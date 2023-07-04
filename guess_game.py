
import random

top_range = input("What is the range you would like to play for?: ")

if top_range.isdigit():
    top_range = int(top_range)
else:
    print("Please type a number next time")

random_number = random.randint(0,top_range)



guess = 0
while True:
    guess += 1

    guess_number = input("Guess a number: ")

    if guess_number.isdigit():
        guess_number = int(guess_number)
    else:
        print("Please type a number next time")
        continue

    if guess_number == random_number:
        print(f"You won,the right answer is {random_number}!")
        break

    elif guess_number < random_number:
        print("Guess higher")
    else:
        print("Guess lower")

print(f"You guessed the right answer in {guess} guesses")

