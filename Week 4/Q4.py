user_name = input('please enter your name: \n')
list_name = user_name.split()

print("Fullname: " + user_name + '\n' + "Initials: " + ''.join(initial[0] for initial in list_name))   