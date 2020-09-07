#Write a program that could be used for an (unsecure) login, with a username and password.
username = input ("please enter username")
password = input ("please enter password")


if password == "password1234" and username == "bob":
    print("access granted")
elif password == "happypass122" and username == "fred":
    print("access granted")
elif password == "passwithlock44" and username == "lock":
    print("access granted")
else:
    print("access denied")
