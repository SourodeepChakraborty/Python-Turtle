from turtle import *
import colorsys

speed(0)
bgcolor("#252525")
pensize(2)
h = 0.8
for i in range(200):
    c = colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h += 0.005
    rt(20)
    for j in range(5):
        fd(i)
        rt(100)
    rt(120)
done()