#Strings are compared using the ASCII values A to Z are represented by numbers 65 to 90.
#A to z are represented by 97 to 122.
#Digits 0 to 9 are stored in memory as characters by numbers 48 to 57. Blank space by 32

print("z")
print(str(ord('z')))
print('a')
print(str(ord('a')))

if ('z' > 'a'):
    print(" z greater")
else:
    print("z lesser")