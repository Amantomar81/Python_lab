# Program to find the area and perimeter of a rectangle, when the required input (Length and Breadth) are entered by the user.
L = eval(input('enter the length of rectangle: '))
B = eval(input('enter the breadth of rectangle: '))
area = L*B
perimeter = 2*(L+B)
print('Area of rectangle: ',area,'\n Perimeter of rectangle: ',perimeter)