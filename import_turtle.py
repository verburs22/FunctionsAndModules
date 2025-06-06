#sarah verburg 06-06

import turtle
from math import radians, cos

# turtle.pendown()
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.done()

def encircle(length: int) -> None:
    """draws circle around square"""
    square(length)
    angle = radians(45)
    radius = length * cos(angle)
    turtle.right(135)
    turtle.circle(radius)
    turtle.left(135)
    print("Dir: ", dir())
    print("locals: ", locals())


def square(length: int) -> None:
   for side in range(4):
        turtle.forward(length)
        turtle.right(90)

#main

# turtle.speed('fast')
# for s in range(72):
#     encircle(120)
#     turtle.left(5)

#encircle(300)
# turtle.done()

print(dir())
print(globals()['square'])

print(dir(__builtins__))