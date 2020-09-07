#Write a program that can grade a student based upon a percentage grade.
High_distinction = 90
Distinction = 80
Credit = 70
Pass = 50

score = int(input("enter your score: "))
if score >= High_distinction:
    print('High distinction')
elif score >= Distinction:
        print('Distinction')
elif score >= Credit:
        print('Credit')
elif score >= Pass:
        print('Pass')
else:
    print('Fail')