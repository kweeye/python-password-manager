pwd = input("What is the master password? ")

def view():
    pass

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")

while True:
    mode = input("Would you like to new password (view or add ) ? ")

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue

