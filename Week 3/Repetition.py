name = input('enter name')
reps = int(input('how many times'))

#for loop --  set & increment the exit condistion at top
for x in range(reps):
    print ('for' + name)

print ('loop complet')

# while loop --  the exit variable incremented / changed In the loop

i = 1
while i < 6:
    print('while ' + str(i))
    i += 1


name = 'abc'

while name != 'tim':
    name = input('incorrect name try again')