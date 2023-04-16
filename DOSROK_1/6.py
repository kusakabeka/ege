from turtle import *
tracer(0)
m = 30
rt(315)
down()
for i in range(7):
    fd(16 * m)
    rt(45)
    fd(8 * m)
    rt(135)
    up()
for x in range(-30 * m, 30 * m):
    for y in range(-30 * m, 30 * m):
        goto(x * m, y * m)
        dot(5, "red")
update();input()
