#Write a program that asks the user for the salary and the time in the job.
#The minimum salary for the sanction of a bank loan is an annual salary of $50000 and the person has to be on the current job for at least 3 years.
# The program should decide whether the person can be given a loan. Use nested if statement with else. 
value1 = int(input("please input salary:\n"))
value2 = int(input("please input years employed:\n"))
if int(value1 >= 50000 and value2 >= 3):
    print("you are eligible for a loan")
else:
    print("you are ineligible for a loan")