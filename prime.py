# Python program to check whether a number is Prime or not.
x = int(input('Enter the number: '))
if x>1:
    for i in range(2, x):
        if x%i == 0:
            print(x,'is  not prime')
            break
    else :
        print(x,'is prime')
else :
    print('number is define')
