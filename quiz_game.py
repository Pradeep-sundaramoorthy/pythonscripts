

player = input("Do you want to play? : ")

if player != "yes":
    quit()
else:
    print("Great,Lets Start")

score = 0

question_1 = input("What is the tallest animal in the world? : ")

if question_1.lower() == 'giraffe':
    print("Yes,correct!")
    score += 1
else:
    print("Incorrect!")

question_2 = input("Where would you be if you were standing on the Spanish Steps? : ")

if question_2.lower() == 'rome':
    print("Yes,correct!")
    score += 1
else:
    print("Incorrect!")

question_3= input ("Which planet in the Milky Way is the hottest? : ")
if question_3.lower() == 'venus':
    print("Yes,correct!")
    score += 1
else:
    print("Incorrect!")

print(f"Yay, you got {str(score)} questions correct! Your final score is {score/4 *100}%")