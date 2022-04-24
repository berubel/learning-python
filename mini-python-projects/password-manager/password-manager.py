#Module that will allow u to encript a text
from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    # wb == write bytes mode
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()
'''
def load_key():
    # rb == read bytes mode
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    #Reading a file
    with open("passwords.txt", 'r') as f:
       for line in f.readlines():
           #decrease line spacing
           data = line.rstrip()
           '''This caracter "|" split the string in a bunch of different items
           every single time that "|" is found'''
           user, passw = data.split("|")
           #['user', 'passw'] -> returns a list of strings
           print("User: {} | Password: {}".format(user, fer.decrypt(passw.encode())))

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    #Creating a file if it's not exist and append to the final a data
    with open("passwords.txt", 'a') as f:
        f.write(name + " | " + fer.encrypt(pwd.encode()).decode() + "\n") #encode converts to string in to bytes
                                                                          #decode converts bytes to string

while True:
    mode = input("\nWould you like to add a new password or view existing one (view, add), press q to quit? ")
    print("\n")

    if mode.lower == "q":
        break

    if mode.lower() == "view":
        view()
    elif mode.lower() == "add":
        add()
    else:
        print("Invalid mode.")
        continue