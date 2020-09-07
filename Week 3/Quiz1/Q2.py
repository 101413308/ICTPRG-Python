#Write a program that asks the user for their year of birth, checks if they are of legal drinking age, and tells the user to come into the bar. Example:
#What is your Year of birth: 1995
#You are: 25 Years old
#Come in and have a drink!
value = int(input("what year were you born?:\n"))
if value <= 2002:
    print('Come in and have a drink!')
else:
    print("go away")