'''Program to find the number of currency notes of each type (Rs. 2000, Rs. 500 and Rs. 100),
when the total number of currency notes counted altogether is minimum and there must be at
least a 100 rupee note dispensed. The amount to be withdrawn is to be entered by the user.'''
a = int(input('enter the amount: '))
b = a//2000
c = a % 2000
d = c // 500
e = c % 500
f = e // 100
print('2000:',b,'\n500:',d,'\n100:',f)