#This is our final project: S.A.M.S.A.L.

from turtle import *
import math

# # Name your Turtle.

# # Set Up your screen and starting position.
setup(1000,600)
x_pos = 30
y_pos = -200


##############################################################

draw = Turtle()


def drawMaze():
    draw.pencolor("gold")
    draw.pensize(3)
    draw.penup()
    draw.goto(0,-180)
    draw.pendown()
    draw.speed(4.5)
    draw.setheading(180)
    draw.fd(180)
    draw.setheading(90)
    draw.fd(60)
    draw.setheading(0)
    draw.fd(120)
    draw.backward(120)
    draw.setheading(90)
    draw.fd(300)
    draw.setheading(0)
    draw.fd(120)
    draw.setheading(-90)
    draw.fd(120)
    draw.setheading(180)
    draw.fd(60)
    draw.setheading(90)
    draw.fd(60)
    draw.setheading(-90)
    draw.fd(120)
    draw.setheading(90)
    draw.fd(60)
    draw.setheading(0)
    draw.fd(120)
    draw.setheading(-90)
    draw.fd(60)
    draw.setheading(0)
    draw.fd(60)
    draw.setheading(-90)
    draw.fd(60)
    draw.backward(60)
    draw.setheading(0)
    draw.fd(60)
    draw.setheading(90)
    draw.fd(60)
    draw.penup()
    draw.setheading(180)
    draw.fd(60)
    draw.pendown()
    draw.setheading(90)
    draw.fd(60)
    draw.setheading(180)
    draw.fd(60)
    draw.setheading(90)
    draw.fd(60)
    draw.setheading(0)
    draw.fd(120)
    draw.setheading(-90)
    draw.fd(60)
    draw.backward(60)
    draw.setheading(0)
    draw.fd(60)
    draw.setheading(-90)
    draw.fd(240)
    draw.setheading(180)
    draw.fd(60)
    draw.setheading(-90)
    draw.fd(60)
    draw.setheading(180)
    draw.fd(120)
    draw.setheading(90)
    draw.fd(60)
    draw.setheading(180)
    draw.fd(60)
    draw.setheading(90)
    draw.fd(60)
    draw.backward(60)
    draw.setheading(180)
    draw.fd(60)
    draw.penup()
    draw.setheading(0)
    draw.fd(300)
    draw.pendown()
    draw.setheading(-90)
    draw.fd(120)
    draw.setheading(180)
    draw.fd(120)
    draw.ht()


drawMaze()


robot = Turtle()
start_pos = (x_pos, y_pos)

### Write your code below:

robot.penup()
robot.goto(start_pos)
robot.setheading(90)

   ##### Move the robot now!

while 0 < 1:
    if 

robot.fd()


























mainloop()
