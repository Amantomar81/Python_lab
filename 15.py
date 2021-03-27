''' Program that calculates the number of rectangular tiles required to cover a rectangular floor if
the dimensions of the floor and the dimensions of a tile are entered by the user. '''
Lf = eval(input('enter the length of floor:'))
Bf = eval(input('enter the breadth of floor: '))
Lt = eval(input('enter the length of tiles:'))
Bt = eval(input('enter the breadth of tiles: '))
A = Lf*Bf
a = Lt*Bt
tiles = A/a
print('Total number of tiles required:',tiles)