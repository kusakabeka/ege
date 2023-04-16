from turtle import *
tracer(0)

m = 30

rt(45)
down()
for i in range(7):
    fd(6 * m)
    rt(45)
    fd(12 * m)
    rt(135)
up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(5, "red")

update()

input()
