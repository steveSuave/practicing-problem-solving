import turtle
import math

def square(side):
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)

def pyth(length, depth, angle):

    # make sure the output will resemble a tree
    if angle>83: angle%=83
    if angle<0 : angle=-angle
    if angle<7 : angle*=7
    
    square(length)
    if depth==1:
        return
    turtle.left(90)
    turtle.forward(length)
    turtle.right(angle)
    pyth(length*math.cos((90-angle)*math.pi/180),depth-1, angle)
    turtle.forward(length*math.cos((90-angle)*math.pi/180))
    turtle.right(90)
    pyth(length*math.sin((90-angle)*math.pi/180),depth-1, angle)
    turtle.left(90)
    turtle.backward(length*math.cos((90-angle)*math.pi/180))
    turtle.left(angle)
    turtle.backward(length)
    turtle.right(90)

turtle.up()
turtle.goto(-100,-300)
turtle.down()
turtle.pensize(4)
turtle.speed(0)
turtle.shape("turtle")
turtle.color("green")
pyth(100, 7, 32)
