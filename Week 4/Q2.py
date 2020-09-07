#Design a program which will ask the user to enter the date in the form dd/mm/yyyy. Example 23/08/2019
user_date = input('please enter date in dd/mm/yyyy format')
list_date = user_date.split('/')

print("Date: " + list_date[0]+ '\n'"Month: " + list_date[1]+ '\n'"Year: " + list_date[2]+ '\n')