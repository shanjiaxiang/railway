# -*- coding:utf-8 -*-
import turtle
def getClickPoint(x, y):
    print("x", x, "y", y)

turtle.screensize(200, 200, None)
turtle.setworldcoordinates(0,0, 200,200)
turtle.onscreenclick(getClickPoint)
turtle.done()