from turtle import *
color("black", "red")
m = 100
speed(10)
begin_fill()
for i in range(3):
    fd(123 * m)
    rt(120)
end_fill()
canvas = getcanvas()
count = 0
for x in range(-200 * m, 200 * m, m):
    for y in range(-200 * m, 200 * m, m):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            count += 1
print(count)
done()
exit()