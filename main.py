#
# Trains a computer to take two numberical inputs and tell us which is larger
# Will return an output of 1 if the first is larger or 0 if not
#
# Idea from Professor Cass Sherman
# Author: Jack Garhart, 31 October 23

import sympy as sym
from math import exp

#inits
w1,w2=-.3, .4 #weights
a,b = 5, 2 #first test nums
c,d = 3.6, 4.9 #second tests nums
e = exp(1) #euler's number (math.exp(1))
xval, yval = 0.0, 0.0


#function to get them to equal 1 or 0
def sig(alpha):
    return 1/(1+pow(e,-alpha))

# cost function to see how far off the numbers are
def cost(x,y):
    return pow(sig(a*x+b*y)-1,2) + pow(sig(c*x+d*y)-0,2)

x, y = sym.symbols('x y')

#Use gradient to find the biggest ROC vector, and using the negative to reduce cost
def gradCost():
    global w1, w2
    costXprime = sym.diff(cost(x,y), x) #cost prime in x: fx
    costYprime = sym.diff(cost(x,y), y) #cost prime in y: fy
    xval = -costXprime.evalf(subs={x:w1, y:w2}) #evaluate fx with x,y = w1,w2
    yval = -costYprime.evalf(subs={x:w1, y:w2}) #evaluate fy with x,y = w1,w2

    print("-∇C = <",xval," ",yval,">\n") #print negative gradient
    w1 += xval / 2 #step through x vector at half speed
    w2 += yval / 2 #step through y vector at half speed
def check(x1, x2): #should equal 1 eventually 5>2
    return sig(x1*a+x2*b)
def check2(x1,x2): #should equal 0 eventually 3.6<4.9
    return sig(x1*c+x2*d)

while check(w1,w2) <= 0.9999 and check2(w1,w2) >= 0.0001:
    gradCost()
    print(check(w1,w2), " ", check2(w1,w2))
print("done")



