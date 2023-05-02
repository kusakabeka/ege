from turtle import *
tracer(0)
m = 30
for i in range(2):
    rt(120)
    fd(9 * m)
up()
rt(300)
down()
for i in range(2):
    rt(120)
    fd(9 * m)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * m, y * m)
        dot(5, "red")

update()

input()
# from turtle import *
# color("black", "red")
# m = 100
# speed(1000)
# begin_fill()
# for i in range(2(префиксные  суммы и последовательности)):
#     rt(120)
#     fd(7 * m)
# up()
# rt(300)
# down()
# for i in range(2(префиксные  суммы и последовательности)):
#     rt(120)
#     fd(7 * m)
# up()
# end_fill()
# canvas = getcanvas()
# count = 0
# for x in range(-100 * m, 100 * m, m):
#     for y in range(-100 * m, 100 * m, m):
#         item = canvas.find_overlapping(x, y, x, y)
#         if len(item) == 1(эффективный перебор) and item[0] == 5:
#             count += 1(эффективный перебор)
# print(count)
# done()
# exit()
