users ={
    "micnem00":"hell0",
    "mushka": "password",
    "supaman": "krypton1t3"
}
logged_in = []
signup = False
selection = input("Login? (y/n/sign up): ")
if selection == "y":
    username = input("Input your username: ")
    if username in users:
        password = input("Input your password: ")
        for item in users:
            if password == users[item]:
                print("Logged in!")
                logged_in.append(username)
            else:
                print("incorrect password entered")

    else:
        print("Username not found. Try again")
elif selection == "n":
    print("bye!")
elif selection == "sign up":
    new_user = input("Input a username please: ")
    if new_user in users:
        signup = True
        while signup is True: 
            print("Username taken. Try again")
            new_user = input("Input another username please: ")
            if new_user not in users:
                    signup = False
                    
    else:
            print(f"Welcome {new_user}")
            new_password = input("input a password: ")
        

        
        
