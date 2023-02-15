import turtle as t
import random
import colorsys

t.bgcolor('black')
t.tracer(10)
t.pensize(2)
h = 0.0
for i in range(50):
    x = random.randint(0,0)
    y = random.randint(0,0)
    t.up()
    t.goto(x,y)
    t.down()
    size = random.randint(10,200)
    for i in range(37):
        c = colorsys.hsv_to_rgb(h,1,1)
        h += 0.005
        t.pencolor(c)
        t.fd(size)
        t.bk(i)
        t.rt(90)
t.done()