#Given the following python code:

#values = [66, 43, 1, 6, 2, 99, 4]
#Output each number on a separate line if it is less than the number 10.
values = [66, 43, 1, 6, 2, 99, 4]
new_list = []
for number in values: 
    if number<10:
        new_list.append(number)
print(new_list, '\n')