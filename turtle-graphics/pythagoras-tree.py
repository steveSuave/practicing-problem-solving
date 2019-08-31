import turtle

turtle.shape("turtle")
turtle.pensize(4)

def quad(side):
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)

def pyth(length, depth):

    quad(length)
    
    if depth==1:
        return
    turtle.left(90)
    turtle.forward(length)
    turtle.right(45)
    pyth(length/(2**0.5), depth-1)
    turtle.forward(length/(2**0.5))
    turtle.right(90)
    pyth(length/(2**0.5), depth-1)
    turtle.left(90)
    turtle.backward(length/(2**0.5))
    turtle.left(45)
    turtle.backward(length)
    turtle.right(90)

    
turtle.up()
turtle.goto(-100,-300)
turtle.down()
turtle.speed(0)
turtle.color("green")
pyth(150,7)
