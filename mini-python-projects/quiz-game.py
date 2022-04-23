print("Welcome to my computer quiz!")

#Ask if the user wants to play and get the response
playing = input("Do you want to play? ")

#If not equal to yes, then quit the program
if playing.lower() != "yes":
    quit()

print("\nLet's play :)")

score = 0

#Questions
answer = input("\nWhat does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("\nWhat does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("\nWhat does RAM stand for? ")
if answer.lower() == "random acess memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("\nWhat does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("\nWhat does PC stand for? ")
if answer.lower() == "program counter":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("\nTHIS IS THE END OF THE QUIZ!! LET'S SEE YOUR SCORE")

#Show performance in quiz
if score == 5:
    print("\nYou got all questions correct. Congratulations!!". format(score))
elif score > 1 and score < 5:
    print("\nYou got {} questions correct!". format(score))
elif score == 1:
    print("\nYou got {} only one question correct.". format(score))
else:
    print("\nYou didn't get any questions correct :(". format(score))

#Percentage achieved
percent = (score / 5) * 100

print("The percentage of correct answers was: {}%".format(percent))
