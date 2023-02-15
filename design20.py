import turtle as t
import colorsys

t.bgcolor("black")
t.tracer(100)
t.pensize(5)
h = 0
for i in range(200):
    c = colorsys.hsv_to_rgb(h,1,0.8)
    h += 0.005
    t.pencolor(c)
    t.circle(i,90)
    t.rt(30)
    t.circle(i*0.5,-90)
    t.circle(-i*0.5,-90)
t.done()