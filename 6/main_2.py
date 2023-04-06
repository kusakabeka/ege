from turtle import *
tracer(0)
m = 30
for i in range(2):
    forward(10 * m)
    right(90)
    forward(20 * m)
    right(90)
up()
backward(15)
right(90)
forward(8 * m)
left(90)
down()
for i in range(2):
    forward(30 * m)
    right(90)
    forward(40 * m)
    right(90)
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * m, y * m)
        dot(5, "red")

update()

input()