'''Program to find whether a triangle is scalene, isosceles, right angled or invalid when the sides of
the triangle are entered by the user. '''
side1 = int(input('enter the value of side1: '))
side2 = int(input('enter the value of side2: '))
side3 = int(input('enter the value of side3: '))
if (side1)**2 + (side2)**2 == (side3)**2 or (side2)**2 + (side3)**2 == side1**2 or (side1)**2 + (side3)**2 == (side2)**2:
    print('right angled triangle')

elif side1 != side2 and side1 != side3 and side2 != side3:
    print('scalene triangle')

elif side1 == side2 or side1 == side3 or side2 == side3:
    print('isosceles triangle')
else:
    print('invalid triangle')



