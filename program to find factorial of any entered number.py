#program to find factorial of any entered number.
n = int(input('enter a number:'))
f=0
while n>0:
    f+=n
    n-=1
print('factorial is =',f)
