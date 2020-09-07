#Write a program that asks the user for three scores out of 100. It then calculates the average.
#If the average is greater than 90, congratulate the user. Write a pseudocode before you write the Python program.
score1 = int(input ("Please input first score out of 100"))
score2 = int(input ("Please input second score out of 100"))
score3 = int(input ("Please input third score out of 100"))
average = (score1 + score2 + score3) / 3
if average > 90:
    print ("congratz")