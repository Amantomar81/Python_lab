#program to check armstrong no.
n = int(input('enter a number:'))
m =n
sum = 0
while n>0:
    sum = sum + (n%10)**3
    n= n//10
if sum == m:
    print('no. is armstrong')
else:
    print('no. is not armstrong')
