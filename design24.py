from turtle import *
import colorsys
bgcolor("black")
tracer(50)
h = 0
pensize(4)
for i in range(500):
    c = colorsys.hsv_to_rgb(h,1,1)
    h += 0.005
    pencolor('black')
    up()
    goto(8,25)
    down()
    fd(i)
    rt(89)
    fillcolor(c)
    begin_fill()
    circle(15,320)
    end_fill()
done()
