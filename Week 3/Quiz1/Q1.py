#Write a program that asks the user for their name, checks if their name is either "frank" or "george" and if it is, greet them by their name.
value = input("type something:\n")
if value == "frank":
    print(f'Hello {value}')
elif value == "george":
    print(f'Hello {value}')
else:
    print("go away")