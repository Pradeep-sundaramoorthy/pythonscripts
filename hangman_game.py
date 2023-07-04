
import random


from words import words

result = words()

word = random.choice(result)

allowed_errors = 6
guesses = []
done = False

while not done:

    for letter in word:
        if letter.lower() in guesses:
            print(letter,end=' ')
        else:
            print(end='_')
    print(end=' ')

    guess = input(f"Allowed erros left {allowed_errors},Next guess: ")
    guesses.append(guess.lower())

    if guess.lower() not in word.lower():
        allowed_errors -= 1
        if allowed_errors == 0:
            break

    done = True

    for letter in word:
        if letter.lower() not in guesses:
            done = False
if done:
    print(f"You won, the letter is {word}")

else:
    print(f"You lose, the letter is {word}")

