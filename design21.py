import turtle as t
import colorsys
t.bgcolor('black')
t.tracer(68)
def draw():
    h = 0
    n = 140
    t.up()
    t.goto(-86,0)
    t.down()
    t.pensize(5)
    for i in range(149):
        c = colorsys.hsv_to_rgb(h,1,1)
        h += 1/n
        t.color(c)
        t.lt(40)
        t.fd(18)
        t.circle(i,76)
        t.bk(26)
        for k in range(15):
            t.rt(56)
            t.circle(k,290)
draw()
t.done()