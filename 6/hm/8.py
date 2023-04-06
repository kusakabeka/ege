from turtle import *
color("black", "red")
m = 100
speed(10)
begin_fill()
right(60)
for i in range(4):
    fd(8 * m)
    rt(120)
    fd(4 * m)
    rt(240)
rt(120)
fd(2 * m)
rt(90)
fd((16 * 3**0.5) * m)
rt(90)
fd(2 * m)
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