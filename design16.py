import turtle
import colorsys

turtle.Screen().bgcolor('black')
t = turtle.Pen()
h = 0
t.speed(0)
turtle.tracer(50)

for i in range(200):
    t.width(i/100+1)
    c = colorsys.hsv_to_rgb(h,1,0.8)
    t.pencolor(c)
    t.left(1000)
    t.pu()
    t.forward(i)
    t.pd()
    t.circle(i,-90)
    t.right(200)
    t.pu()
    t.forward(i)
    t.left(120)
    t.forward(i)
    t.pd()
    t.fd(7)
    t.rt(10)
    t.lt(19)
    h += 0.009

turtle.done()