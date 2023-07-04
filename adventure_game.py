
User_name = input("Please enter your name?: ")

print(f'Hello {User_name}, Welcome to the adventure land, you must now continue playing to live or die 🙀')

answer = input("how would you like to proceed further? please type left/right: ").lower()


if answer == 'left':
    question = input(
                    "You are struck on a tree with a hungry lion sitting down waiting for you,"
                    " you can either jump into a river or fight the lion,"
                    "what would you choose? : Type jump to jump to river/ fight to get down and fight the lion: " ).lower()

    if question == 'jump':
        print("you swam across the river and saved yourself")
    elif question == 'fight':
        print("you fought the lion and it ate you, you lose")
    else:
        print("invalid option")

elif answer == 'right':
    question = input("Answer a riddle to get your free pass card or pass to draw a lucky card : type yes for riddle and no for picking a card: ").lower()
    if question == 'yes':
        riddle = input("At night I come without being fetched. By day I’m lost, without being stolen. What am I? – ").lower()
        if riddle == 'star':
            print("That's right!, you won your free token card to escape this adventure land! ")
        else:
            print("sorry wrong answer, you lose!")
    elif question == 'no':
        print("Better luck next time, you lose")
    else:
        print("invalid option")
else:
    print("Not a valid option, you lose")
print(f"Thank you {User_name} for playing, see you next time")