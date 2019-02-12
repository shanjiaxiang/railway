# -*- coding:utf-8 -*-
from turtle_util import *
from SquareObstacle import *
import turtle

OBSTACLE_LIST = []


def drawObstacle(obstacle):
    point1 = obstacle.leftUp
    point2 = obstacle.rightBottom
    upGoto(point1)
    downGoto(Point(point2.x, point1.y))
    downGoto(Point(point2.x, point2.y))
    downGoto(Point(point1.x, point2.y))
    downGoto(Point(point1.x, point1.y))
    centerY = (point1.y + point2.y) / 2
    upGoto(Point(point1.x + 4, centerY))
    turtle.write("障碍物")
    OBSTACLE_LIST.append(obstacle)
    print("list size:", len(OBSTACLE_LIST))


def isClickInObstacle(x, y):
    for obstacle in OBSTACLE_LIST:
        print("minX:", obstacle.minX, "maxX:", obstacle.maxX)
        print("minY:", obstacle.minY, "maxY:", obstacle.maxY)
        if obstacle.minX < x < obstacle.maxX and \
                                obstacle.minY < y < obstacle.maxY:
            return False
    return True


def getClickPoint(x, y):
    if isClickInObstacle(x, y):
        print("x:", x, "y", y)
        upGoto(Point(x, y))
        drawObstacle(SquareObstacle(Point(x, y), Point(x+50, y+50)))


turtle.onscreenclick(getClickPoint)
turtle.mainloop()
# done()
