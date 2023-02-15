import turtle as t
import colorsys

t.Screen().bgcolor("black")
tu = t.Pen()
tu.speed(0)
h = 0.4
tu.goto(-60,0)

for i in range(200):
    c = colorsys.hsv_to_rgb(h,1,1)
    tu.color(c)
    tu.begin_fill()
    tu.circle(50,120)
    tu.forward(i)
    tu.left(170)
    tu.forward(i)
    tu.end_fill()
    h += 0.005

t.done()