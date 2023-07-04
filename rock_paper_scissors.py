import random

user_wins = 0
computer_wins = 0
option = ["rock","paper","scissor"]

while True:
    user_input = input("Please enter- Rock/Paper/Scissor or q: ").lower()
    if user_input == 'q':
        break

    if user_input not in option:
        continue

    random_number = random.randint(0,2)
    computer_input = option[random_number]
    print(f"computer picks {computer_input}!")

    if user_input == 'rock' and computer_input == 'scissor':
        print("You won")
        user_wins += 1


    elif user_input == 'scissor' and computer_input == 'paper':
        print("You won")
        user_wins += 1

    elif user_input == 'paper' and computer_input == 'rock':
        print("You won")
        user_wins += 1

    elif user_input == computer_input:
        print("Draw")


    else:
        print("computer won")
        computer_wins +=1

print(f"Goodbye, you won {user_wins} and computer won {computer_wins} times in total")