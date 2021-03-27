'''Program to find the hypotenuse of a right angled triangle, when the base and height are entered
by the user.
'''
B = eval(input('Enter the base of right triangle: '))
H = eval(input('Enter the height of right triangle: '))
Hypotenuse_sqrt = (B**2 + H**2)**0.5
print(Hypotenuse_sqrt)