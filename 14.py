''' Program to find the Compound Interest compounded annually and the total amount when the
Principal, Rate of Interest and Time are entered by the user'''
p = eval(input('enter the principal value:'))
r = eval(input('enter the rate of interest:'))
t = eval(input('enter the time:'))
ci = (p*pow((1+r/100),t))-p
total = ci+p
print('compound interesr is',ci,'\n total amount',total)