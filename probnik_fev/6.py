from turtle import *
tracer(3)
m = 30
for i in range(6):
    fd(5 * m)
    rt(60)
up()
fd(5 * m)
rt(90)
down()
for i in range(2):
    fd(15 * m)
    rt(90)
    fd(5 * m)
    rt(90)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * m, y * m)
        dot(5, "red")

update()
'''

LANG=C.UTF-8
LANGUAGE=
LC_CTYPE="C.UTF-8"
LC_NUMERIC="C.UTF-8"
LC_TIME="C.UTF-8"
LC_COLLATE="C.UTF-8"
LC_MONETARY="C.UTF-8"
LC_MESSAGES="C.UTF-8"
LC_PAPER="C.UTF-8"
LC_NAME="C.UTF-8"
LC_ADDRESS="C.UTF-8"
LC_TELEPHONE="C.UTF-8"
LC_MEASUREMENT="C.UTF-8"
LC_IDENTIFICATION="C.UTF-8"
LC_ALL=


'''