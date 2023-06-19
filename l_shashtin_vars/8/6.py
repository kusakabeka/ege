from turtle import *

tracer(0)
m = 30

rt(225)
for i in range(6):
    fd(15 * m)
    rt(60)
    fd(7 * m)
    rt(120)
up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(5, "red")
update()
input()