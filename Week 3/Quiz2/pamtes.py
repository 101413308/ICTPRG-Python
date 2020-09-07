total = 0
import getpass

while True: 
    user_number = getpass.getpass("Plase enter a number (Press x for finish) ")
    try:
        total += int(user_number)
    except ValueError:
        break
print("Total: ", total)