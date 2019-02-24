# -*- coding:utf-8 -*-
from turtle_util import *
from obstacle import SquareObstacle
import turtle
import draw
import AStar as star

class DrawObstacleUtils:
    def __init__(self, mapSize, obstacles):
        self.obstacles = obstacles
        self.mapSize = mapSize
        self.turtle_obstacle = turtle.RawTurtle(turtle.getscreen())
        self.turtle_obstacle.hideturtle()

    def drawObstacle(self, obstacle):
        print("obstacle:", obstacle.minX, obstacle.minY, obstacle.maxX, obstacle.maxY)
        point1 = obstacle.leftBottom
        point2 = obstacle.rightUp
        self.turtle_obstacle.penup()
        self.turtle_obstacle.goto(point1.x, point1.y)
        self.turtle_obstacle.pendown()
        self.turtle_obstacle.goto(point2.x, point1.y)
        self.turtle_obstacle.goto(point2.x, point2.y)
        self.turtle_obstacle.goto(point1.x, point2.y)
        self.turtle_obstacle.goto(point1.x, point1.y)
        centerY = (point1.y + point2.y) / 2
        self.turtle_obstacle.penup()
        self.turtle_obstacle.goto(point1.x, centerY-2)
        self.turtle_obstacle.write("障碍物")
        self.turtle_obstacle.hideturtle()


    def isClickInObstacle(self,x, y):
        for obstacle in self.obstacles:
            # print("minX:", obstacle.minX, "maxX:", obstacle.maxX)
            # print("minY:", obstacle.minY, "maxY:", obstacle.maxY)
            if obstacle.minX < x < obstacle.maxX and \
                                    obstacle.minY < y < obstacle.maxY:
                print("you clicked obstacle")
                return True
        print("you licked outside of obstacle")
        return False

    # 绘制所有的障碍物
    def fun_drawObstacles(self):
        for obstacle in self.obstacles:
            drawObstacle(obstacle)


    # 获得点击位置
    def getClickPoint(self,x, y):
        if not self.isClickInObstacle(x, y):
            self.obstacles.append(SquareObstacle.SquareObstacle(Point(x, y), Point(x + 10, y + 10)))
            self.drawObstacle(SquareObstacle.SquareObstacle(Point(x, y), Point(x + 10, y + 10)))

    def getObstacle(self,x,y):
        x = int(x)
        y = int(y)
        print("click x:", x, "y:", y)
        if not self.isClickInObstacle(x, y):
            obstacle = SquareObstacle.SquareObstacle(Point(x, y), Point(x + 10, y + 10))
            self.obstacles.append(obstacle)
            self.drawObstacle(obstacle)
            return obstacle
        else:
            return None

    def convertTurtleToMap(self,point):
        newPoint = Point(0, 0)
        newPoint.x = point.x + mapSize[0]
        newPoint.y = point.y + mapSize[1]
        return newPoint


    def getClickPoint1(self,x,y):
        print("clicked x:",x, "y:",y)

    def getObstacles(self):
        return self.obstacles


