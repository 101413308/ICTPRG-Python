#Write a program that can accept many numbers from the user, until they enter an x
total = []
import getpass
while True:

    a = getpass.getpass ('Enter next number or end:')
    if (a == 'x'):
        break
    else:
        total.append(a)
print("You entered the numbers = ", total)
