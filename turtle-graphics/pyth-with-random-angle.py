import turtle
import math
import random

def square(side):
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)

def pyth(length, depth):
    angle=random.randint(7,83)
    square(length)
    if depth==1:
        return
    turtle.left(90)
    turtle.forward(length)
    turtle.right(angle)
    pyth(length*math.cos((90-angle)*math.pi/180),depth-1)
    turtle.forward(length*math.cos((90-angle)*math.pi/180))
    turtle.right(90)
    pyth(length*math.sin((90-angle)*math.pi/180),depth-1)
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
pyth(100, 9)
