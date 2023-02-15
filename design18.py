import turtle as  t
import colorsys

t.bgcolor("black")
t.tracer(50)
t.ht()
h = 0
for i in range(200):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 0.008
    t.pencolor(c)
    t.fd(i)
    t.lt(68)
    t.rt(40)
    t.circle(10)
t.done()