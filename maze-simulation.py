#This is our final project: S.A.M.S.A.L.

from turtle import *
from PIL import Image
import math

IMAGE_PATH = "maze.gif"

# # Name your Turtle.

# # Set Up your screen and starting position.

my_image = Image.open(IMAGE_PATH)
width, height = my_image.size

robot = Turtle()
setup(width,height)
x_pos = 40
y_pos = -250
start_pos = (x_pos, y_pos)
bgpic(IMAGE_PATH)


### Write your code below:

robot.penup()
robot.goto(start_pos)
robot.setheading(90)

#<<<<<<< HEAD
# Import image.
maze = Image.open("maze.gif")
pix = maze.convert("RGB").getpixel((540, 550))
print(pix)
##############################################################

#=======




#Import image

pix = my_image.load()





# Import image.
maze = Image.open("maze.gif")


##############################################################


   ##### Move the robot now!

pixel = (255, 255, 255)
while pixel == (255, 255, 255):
    robot.forward(1)
    x = robot.xcor()
    y = robot.ycor()
    print("turtle coordinates: " + str(x) + ", " + str(y))

   #Converting turtle coordinates to pillow
    x += (width / 2)
    if y <= 0:
        y = (abs(y) + (height / 2))
    else:
        y = ((height / 2) - y)
    print("Pillow coordinates: " + str(x) + ", " + str(y))
    pixel = maze.convert("RGB").getpixel((x, y))
    print(pixel)
robot.left(90)
robot.forward(75)
robot.right(90)
#>>>>>>> bd0d4e0b199e9d1b9d42c944f3d63bcde6eb1865
mainloop()
