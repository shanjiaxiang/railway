# -*- coding:utf-8 -*-
from turtle_util import *
from SquareObstacle import *
import turtle
import draw
import AStar as star

MAP_SIZE = (200, 200)
OBSTACLE_LIST = []


def drawObstacle(obstacle):
    print("obstacle:", obstacle.minX, obstacle.minY, obstacle.maxX, obstacle.maxY)
    point1 = obstacle.leftBottom
    point2 = obstacle.rightUp
    upGoto(point1)
    downGoto(Point(point2.x, point1.y))
    downGoto(Point(point2.x, point2.y))
    downGoto(Point(point1.x, point2.y))
    downGoto(Point(point1.x, point1.y))
    centerY = (point1.y + point2.y) / 2
    upGoto(Point(point1.x + 4, centerY))
    turtle.write("障碍物")
    OBSTACLE_LIST.append(obstacle)
    # print("list size:", len(OBSTACLE_LIST))


def isClickInObstacle(x, y):
    for obstacle in OBSTACLE_LIST:
        # print("minX:", obstacle.minX, "maxX:", obstacle.maxX)
        # print("minY:", obstacle.minY, "maxY:", obstacle.maxY)
        if obstacle.minX < x < obstacle.maxX and \
                                obstacle.minY < y < obstacle.maxY:
            print("you clicked obstacle")
            return True
    print("you licked outside of obstacle")
    return False

def fun_drawObstacles():
    for obstacle in OBSTACLE_LIST:
        drawObstacle(obstacle)

def getClickPoint(x, y):
    if not isClickInObstacle(x, y):
        newPoint = convertTurtleToMap(Point(x, y))
        print("Tran x:", newPoint.x, "Tran y", newPoint.y)
        upGoto(Point(x, y))
        drawObstacle(SquareObstacle(Point(x, y), Point(x + 50, y + 50)))


def convertTurtleToMap(point):
    newPoint = Point(0, 0)
    newPoint.x = point.x + MAP_SIZE[0]
    newPoint.y = point.y + MAP_SIZE[1]
    return newPoint


# draw.initPen()
initCanvas(MAP_SIZE[0]/2, MAP_SIZE[1]/2)
hideTurtle()
turtleSpeed(0)
turtle.delay(0)
turtle.onscreenclick(getClickPoint)
draw.fun_genUsers()
draw.fun_refresh(OBSTACLE_LIST)
turtle.mainloop()
turtle.done()
# done()
