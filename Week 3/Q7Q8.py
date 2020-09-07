A_score = 90
B_score = 80
C_Score = 70
D_score = 60

score = int(input("enter your score: "))
if score >= A_score:
    print('Your grade is A')
elif score >= B_score:
        print('your grade is B')
elif score >= C_Score:
        print('your grade is C')
elif score >= D_score:
        print('your grade is D')
else:
    print('your grade is F')