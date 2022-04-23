import random

while True:
    top_of_range = input("Type a number: ")
    print("\n")

    #Checks if a digit has been entered (does not allow other type of elements)
    if top_of_range.isdigit():
        #converts the digit to an int element
        top_of_range = int(top_of_range)

        if top_of_range > 0:
            break
        else:
            print("Please type a number larger than 0 next time.\n")
            continue
    else:
        print("Please type a number next time.\n")
        continue

#Generate a random number
random_number = random.randint(0, top_of_range)
guesses = 0

#Number guesser
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.\n")
        continue

    if user_guess == random_number:
        print("Random number is {}".format(random_number))
        print("\nYou got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!\n")
    else:
        print("You were below the number!\n")

print("You got in", guesses, "guesses")