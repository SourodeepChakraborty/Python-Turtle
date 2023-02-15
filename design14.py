import turtle as t
import colorsys

t.bgcolor('black')
t.tracer(10)
t.pensize(3)
h = 0
for i in range(300):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 0.005
    t.color(c)
    t.goto(0,0)
    t.fd(i)
    t.rt(144)
    for j in range(5):
        t.fd(30)
        t.lt(145)
t.done()