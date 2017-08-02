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

<<<<<<< HEAD


#Import image
my_image = Image.open("maze.gif")
pix = my_image.load()


=======
# Import image.
maze = Image.open("maze.gif")
pix = maze.convert("RGB").getpixel((540, 550))
print(pix)
##############################################################


 
