import turtle as t
import colorsys

t.bgcolor('black')
t.tracer(100)
t.pensize(5)
def draw():
    h = 0.9
    n = 98
    for i in range(320):
        c = colorsys.hsv_to_rgb(h,1,0.9)
        h += 1/n
        t.color(c)
        t.fillcolor("black")
        t.begin_fill()
        t.circle(h,43)
        t.rt(20)
        t.bk(45)
        t.up()
        t.goto(0,0)
        t.down()
        t.circle(i,23)
        t.rt(55)
        t.fd(i)
        t.end_fill()
draw()
t.done()