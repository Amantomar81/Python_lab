'''Program to input the number of overs in a Cricket match and output the maximum runs a
player can score in the match. Assume that there are no extra runs or NO balls in the match
played. For example, in a 50 over match, the maximum runs scored are 1653.'''
O = eval(input('enter the number of overs: '))
x = 33*(O-1)
y = 36+x
print('maximum runs are scored by a player: ',y)