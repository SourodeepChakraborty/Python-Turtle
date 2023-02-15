import turtle as t
import colorsys

t.bgcolor('black')
t.tracer(20)
h = 0
for i in range(200):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 0.01
    t.pencolor(c)
    t.left(120)
    t.circle(i-90,180)
    t.left(120)
t.done()