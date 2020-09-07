total = []
import getpass
while True:

    a = getpass.getpass ('Enter next number or end:')
    if (a == 'x'):
        break
    else:
        total.append(a)

dupItems = []
uniqItems = {}
for x in total:
   if x not in uniqItems:
      uniqItems[x] = 1
   else:
      if uniqItems[x] == 1:
         dupItems.append(x)
      uniqItems[x] += 1
print(dupItems)