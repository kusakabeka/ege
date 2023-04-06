from turtle import *
color("black", "red")
m = 100
speed(10)
begin_fill()
right(300)
for i in range(1):
    fd(5 * m)
    rt(90)
    fd(8 * m)
    rt(90)
up()
fd(2 * m)
rt(90)
fd(3 * m)
lt(90)
down()
for j in range(2):
    fd(4 * m)
    rt(90)
    fd(9 * m)
    rt(90)
end_fill()
canvas = getcanvas()
count = 0
for x in range(-100 * m, 100 * m, m):
    for y in range(-100 * m, 100 * m, m):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            count += 1
print(count)
done()
exit()