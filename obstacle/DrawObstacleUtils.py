# -*- coding:utf-8 -*-
from turtle_util import *
from SquareObstacle import *
import turtle
import draw
import AStar as star

MAP_SIZE = (200, 200)
OBSTACLE_LIST = []
TURTLE_OBSTACLE = turtle.RawTurtle(turtle.getscreen())
TURTLE_OBSTACLE.hideturtle()


def drawObstacle(obstacle):
    print("obstacle:", obstacle.minX, obstacle.minY, obstacle.maxX, obstacle.maxY)
    point1 = obstacle.leftBottom
    point2 = obstacle.rightUp
    TURTLE_OBSTACLE.penup()
    TURTLE_OBSTACLE.goto(point1.x, point1.y)
    TURTLE_OBSTACLE.pendown()
    TURTLE_OBSTACLE.goto(point2.x, point1.y)
    TURTLE_OBSTACLE.goto(point2.x, point2.y)
    TURTLE_OBSTACLE.goto(point1.x, point2.y)
    TURTLE_OBSTACLE.goto(point1.x, point1.y)
    centerY = (point1.y + point2.y) / 2
    TURTLE_OBSTACLE.penup()
    TURTLE_OBSTACLE.goto(point1.x, centerY-2)
    TURTLE_OBSTACLE.write("障碍物")
    TURTLE_OBSTACLE.hideturtle()


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

# 绘制所有的障碍物
def fun_drawObstacles():
    for obstacle in OBSTACLE_LIST:
        drawObstacle(obstacle)


# 获得点击位置
def getClickPoint(x, y):
    if not isClickInObstacle(x, y):
        OBSTACLE_LIST.append(SquareObstacle(Point(x, y), Point(x + 10, y + 10)))
        drawObstacle(SquareObstacle(Point(x, y), Point(x + 10, y + 10)))


def convertTurtleToMap(point):
    newPoint = Point(0, 0)
    newPoint.x = point.x + MAP_SIZE[0]
    newPoint.y = point.y + MAP_SIZE[1]
    return newPoint


# draw.initPen()

def getClickPoint1(x,y):
    print("clicked x:",x, "y:",y)


initCanvas(MAP_SIZE[0] / 2, MAP_SIZE[1] / 2)
hideTurtle()
turtle.setworldcoordinates(0,0,200,200)
turtle.hideturtle()
# TURTLE_OBSTACLE.setworldcoordinates(0,0,200, 200)
# 设置坐标
# turtle.setworldcoordinates(0,0, 200,200)
turtleSpeed(0)
turtle.delay(0)
turtle.onscreenclick(getClickPoint)
TURTLE_OBSTACLE.onclick(getClickPoint1)
draw.fun_genUsers()
draw.fun_refresh()
turtle.mainloop()
turtle.done()
# done()
