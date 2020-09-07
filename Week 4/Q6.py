#Write a program that asks the user for a large number, and then sums all of the digits in that number
digit = input('enter large number: ')
list_num = digit.split()
sum_num = sum(int(num) for num in str(digit))
print("Sum: "+ '+'.join(str(digit)) + '='+ str(sum_num))