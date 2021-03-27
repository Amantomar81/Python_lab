''' Program to input the number of heads and feet in a farm and identify the number of chickens
and goats in the farm. For example, if there are 340 heads and 1,060 feet, there are 150
chickens and 190 goats.
'''
h = int(input('enter the number of heads:'))
f = int(input('enter the number of feet:'))
a = f/2
g = a - h
print('number of goats: ',g)
c = h - g
print('number of chickens: ',c)