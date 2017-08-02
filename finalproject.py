#This is our final project: S.A.M.S.A.L.

from turtle import *
from PIL import Image
import math



# # Name your Turtle.

# # Set Up your screen and starting position.
robot = Turtle()
setup(1000,600)
x_pos = 40
y_pos = -250
start_pos = (x_pos, y_pos)
bgpic('maze.gif')


### Write your code below:

robot.penup()
robot.goto(start_pos)
robot.setheading(90)



#Import image
my_image = Image.open("maze.gif")
pix = my_image.load()


##############################################################


   ##### Move the robot now!
robot.forward(90)
robot.left(90)
robot.forward(90)
robot.right(90)
robot.forward(50)
robot.left(90)
robot.forward(125)
robot.right(90)
robot.forward(120)
robot.right(90)
robot.forward(65)
robot.left(90)





mainloop()
