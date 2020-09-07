#Write a program that keeps asking the user for a number, and adds it to a total. Ensure that pressing x stops entering numbers. Example:
total = 0
import getpass
while True:

    a = getpass.getpass ('Enter next number or end:')
    if (a == 'x'):
        break
    else:
        total = total + int(a)
print("Sum of all entered numbers = ", total)
