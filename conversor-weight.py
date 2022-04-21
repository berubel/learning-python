#EXERCISE

w = float(input("Weight: "))
u = input("(K)g or (L)bs: ")

if u.upper() == 'K':
    c = w/2.205
    print("Weight in Kg is: {}".format(c))
elif u.upper() == 'L':
    c = w * 2.205
    print("Weight in Lbs is: {}".format(c))
else:
    print("Invalid option!!")
