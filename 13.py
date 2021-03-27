#Program to find the Simple Interest and the total amount when the Principal, Rate of Interest and Time are entered by the user.
p = eval(input('enter the principal value:'))
r = eval(input('enter the rate of interest:'))
t = eval(input('enter the time:'))
si = (p*r*t)/100
print('simple interest is',si)
total_amount = si + p
print('total amount is',total_amount)
