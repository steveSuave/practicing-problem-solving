from turtle import *

def kochcurve(length,degree):
    if degree==0:
        forward(length)
        return 
    len3=length/3
    deg1=degree-1
    kochcurve(len3,deg1)
    left(60)
    kochcurve(len3,deg1)
    right(120)
    kochcurve(len3,deg1)
    left(60)
    kochcurve(len3,deg1)

speed("fastest")
up()
goto(-300,200)
down()

kochcurve(777,3)
right(120)
kochcurve(777,3)
right(120)
kochcurve(777,3)
right(120)
