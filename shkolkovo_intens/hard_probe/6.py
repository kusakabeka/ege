from turtle import *

tracer(0)
M = 30

for i in range(20):
    for j in range(4):
        fd(5 * M)
        rt(90)
    rt(45)
up()
for x in range(-10, 10):
    for y in range(-10, 10):
        goto(x * M, y * M)
        dot(5, "red")
update()

input()
