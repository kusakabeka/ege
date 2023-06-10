from turtle import *

from turtle import *
m = 30
down()
fd
for i in range(2):
    fd(15 * m)
    rt(90)
    fd(5 * m)
    rt(90)
up()
for x in range(-60, 60):
    for y in range(-60, 60):
        goto(x * m, y * m)
        dot(5, "red")

update()