import turtle
import colorsys

t = turtle.Turtle()
turtle.Screen().bgcolor("black")
t.pensize(2)
t.speed(1)
n = 36
h = 0
for i in range(90):
    c = colorsys.hsv_to_rgb(h,1,0.9)
    h += 1/n
    t.pencolor(c)
    for j in range(5):
        t.forward(i-3)
        t.right(9*5)
        t.left(8)
    t.right(115)
turtle.done()