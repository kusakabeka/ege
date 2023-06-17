from turtle import *
tracer(0)
m = 30
down()
for i in range(6):
    left(120)
    forward(6  * m)
up()
for x in range(-10, 10):
    for y in range(-10, 10):
        goto(x * m, y * m)
        dot(5, "red")
update()
input()