name = input("Type your name: ")
print ("Welcome", name, "to this adventure!")

answer = input("\nYou are on a dirt road, it has come to an "
               "end and you can go left or right. Which way would you like to go? ").lower()
if answer == "left":
    answer = input("\nYou come to a river, you can walk around it or swim acrosss."
                   "Type walk to walk around and swim to swim across: ").lower()

    if answer == "swim":
        print("\nYou swim across and were eaten by an alligator.")
    elif answer == "walk":
        print("\nYou walked for many miles, ran out of water and you lost the game.")
    else:
        print("\nNot a valid option. You lose")

elif answer == "right":
    answer = input("\nYou come to a bridge, it looks wobbly, "
                   "dou you want to cross it or head back (cross/back)? ").lower()

    if answer == "back":
        print("\nYou go back and lose.")
    elif answer == "cross":
        answer = input("\nYou cross the bridge and meet a stranger, Do you talk to "
                       "them (yes/no)? ").lower()

        if answer == "yes":
            print("\nYou talk to the stranger and he gives you gold, You WIN!")
        elif answer == "no":
            print("\nYou ignore the stranger and he is offended and you lose.")
        else:
            print("\nNot a valid option. You lose")
    else:
        print("\nNot a valid option. You lose")
else:
    print("\nNot a valid option. You lose")

print("\nThank you for trying", name)