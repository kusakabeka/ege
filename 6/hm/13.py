from turtle import *
color("black", "red")
m = 100
speed(10)
begin_fill()
for i in range(6):
    fd(31 * m)
    rt(60)
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