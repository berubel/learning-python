import random

user_wins = 0
computer_wins = 0

#List with the options
options = ["r", "p", "s"]

while True:
    user_input = input("\nType: \n\n[R]Rock  \n[P]Paper  \n[S]Scissors  \n"
                       "or [Q] to quit \n\nAnswer: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock[r]: 0, paper[p]: 1, scissors[s]: 2

    computer_pick = options[random_number]
    print("\nComputer picked", computer_pick + ".")

    if user_input == "r" and computer_pick == "s":
        print("You won!!")
        user_wins += 1

    elif user_input == "p" and computer_pick == "r":
        print("You won!!")
        user_wins += 1

    elif user_input == "s" and computer_pick == "p":
        print("You won!!")
        user_wins += 1

    elif user_input == computer_pick:
        print("Tie!")

    else:
        print("You lost!")
        computer_wins += 1

print("\nFINAL SCORE\n")
print("You won {} times.".format(user_wins))
print("The computer won {} times.".format(computer_wins))
print("\nGoodbye!")