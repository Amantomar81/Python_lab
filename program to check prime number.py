# program to check prime number.
n = int(input('Enter a number:'))
i=1
c=0
while n>=i:
    if n%i == 0:
        c +=1
    i += 1
    
if c == 2:
    print('Number is prime')
else:
    print('number is not prime')
    
