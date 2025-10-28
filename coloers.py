from turtle import *
import colorsys

speed(0)
bgcolor("black")
h = 0
for i in range(144):
    for j in range(19):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        color(c)
        h += 8.0 / 255 
        rt(90)
        circle(150 - j * 1.1, 360)
        lt(90)
        circle(150 - j * 1.1, 360)
        rt(180)
    circle (40,24)     
    done()

 