# -*- coding:utf-8 -*-
import turtle
import random
from point_model import *
from bazier import *


def initCanvas(x, y, color=None):
    turtle.screensize(x, y, color)
    # turtle.setup(x, y, 100, 100)
    turtle.setup(0.8,0.8)

def initPen(size, speed=1, color="black", show=True):
    if show:
        turtle.showturtle()
    else:
        turtle.hideturtle()

    turtle.pencolor(color)
    if speed > 10:
        speed = 10
    turtle.penspeed(speed)
    turtle.pensize(size)


# initCanvas(800, 800)
# turtle.hideturtle()
# turtle.dot(10)
# turtle.penup();
# turtle.goto(pointD.x, pointD.y)
# turtle.dot(10)
# t = 0.01
# turtle.goto(0, 0)
# turtle.pendown()


def turtleSpeed(v):
    turtle.speed(v)


#
def showTurtle():
    turtle.showturtle()


def hideTurtle():
    turtle.hideturtle()


def done():
    turtle.done()


def clear():
    turtle.clear()


def reset():
    turtle.reset()


def turtleReset():
    turtle.reset()


def penUp():
    turtle.penup()


def penDown():
    turtle.pendown()


def dot(radius):
    turtle.dot(radius)


def upGoto(point):
    penUp()
    turtle.goto(point.x, point.y)


def drawPoint(point, radius=10):
    upGoto(point)
    penDown()
    dot(radius)


def downGoto(point):
    penDown()
    turtle.goto(point.x, point.y)


def drawPath(point):
    penDown()
    turtle.goto(point.x, point.y)


def drawArc(start, dest):
    drawPoint(start)
    drawPoint(dest)
    upGoto(start)
    t = 0.01
    # 生成中垂线随机控制点
    control = calControlPoint(start, dest)
    for i in range(100):
        t = t + 0.01
        point = calCurvePointWithControl(t, start, control, dest)
        drawPath(point)


def drawArcByTimes(start, dest, times):
    drawPoint(start)
    drawPoint(dest)
    upGoto(start)
    t = 0
    # 生成中垂线随机控制点
    control = calControlPoint(start, dest)
    for i in range(times):
        t = t + 1 / times
        point = calCurvePointWithControl(t, start, control, dest)
        drawPath(point)
