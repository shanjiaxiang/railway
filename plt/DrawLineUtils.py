# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib
from pylab import *
import numpy as np
import _thread
import turtle
from point_model import *


class DataBean:
    x = 0
    y1 = 0
    y2 = 0
    rawY = 0

    def __init__(self, x, rawY):
        self.x = x
        self.rawY = rawY

    def setX(self):
        self.x = x + 1

    def getX(self):
        return self.x

    def setY1(self, y):
        self.y1 = y

    def getY1(self):
        return self.y1

    def setY2(self, y):
        self.y2 = y

    def getY2(self):
        return self.y2


class DrawLineUtils:
    color = ['red', 'blue', 'green', 'yellow', 'black', 'magenta']

    def __init__(self, size):
        self.turtle_line = turtle.RawTurtle(turtle.getscreen())
        self.preListX = []
        self.preListY = []
        self.preList = []
        # self.initPlt(size)

    def initPlt(self, size):
        plt.axis([0, 200, 0, 60])
        plt.ion()
        plt.xlabel("Time(10s)")
        plt.ylabel("Points")
        plt.title("各闸机10s内规划点数")
        for i in range(size):
            self.preListX.append(0)
            self.preListY.append(0)

    def drawLines(self, curList):
        for i in range(len(curList)):
            x = self.preListX[i] + 1
            y = curList[i]
            plt.plot([self.preListX[i], x], [self.preListY[i], y], c=self.color[i])
            self.preListX[i] = x
            self.preListY[i] = y
            plt.pause(0)

    def turtleInit(self, size, destList):
        # for dest in destList:
        #     index = dest.id
        #     self.turtle_line.penup()
        #     self.turtle_line.goto(0 + index * 10, 0)
        #     self.turtle_line.pendown()
        #     self.turtle_line.pencolor(self.color[index])
        #     self.turtle_line.write(destList[index].name)
        #     self.turtle_line.penup()

        for i in range(size):
            self.preListX.append(0)
            self.preListY.append(0)
        self.turtle_line.hideturtle()
        # self.turtle_line.penup()
        # self.turtle_line.goto(0, 0)
        # self.turtle_line.pendown()
        # for i in range(200):
        #     self.turtle_line.goto(i, 0)
        #     self.turtle_line.goto(i, 0.5)
        #     self.turtle_line.goto(i, 0)
        #
        # for i in range(20):
        #     self.turtle_line.penup()
        #     self.turtle_line.goto(0, 0)
        #     self.turtle_line.pendown()
        #     self.turtle_line.goto(0, i)
        #     self.turtle_line.goto(0.5, i)
        #     self.turtle_line.goto(0, i)

        self.turtleLineChartInit(Point(400, 120),"闸机3")
        self.turtleLineChartInit(Point(400, 70),"闸机2")
        self.turtleLineChartInit(Point(400, 20),"闸机1")
        self.turtleLineChartInit(Point(600, 120),"闸机6")
        self.turtleLineChartInit(Point(600, 70),"闸机5")
        self.turtleLineChartInit(Point(600, 20),"闸机4")

        self.preList.append(DataBean(400, 120))
        self.preList.append(DataBean(400, 70))
        self.preList.append(DataBean(400, 20))
        self.preList.append(DataBean(600, 120))
        self.preList.append(DataBean(600, 70))
        self.preList.append(DataBean(600, 20))

        self.turtle_line.penup()
        self.turtle_line.goto(600, 170)
        self.turtle_line.pencolor(self.color[0])
        self.turtle_line.write("无流量控制————")
        self.turtle_line.penup()
        self.turtle_line.goto(680, 170)
        self.turtle_line.pencolor(self.color[2])
        self.turtle_line.write("有流量控制————")

    def drawTurtleLines(self, curList):
        for i in range(len(curList)):
            x = self.preListX[i] + 1
            y = curList[i] + 0
            self.turtle_line.pencolor(self.color[i])
            self.turtle_line.penup()
            self.turtle_line.goto(self.preListX[i], self.preListY[i])
            self.turtle_line.pendown()
            self.turtle_line.goto(x, y)
            self.turtle_line.pencolor('black')
            self.turtle_line.penup()
            self.preListX[i] = x
            self.preListY[i] = y

    def drawTurtleLineSingle(self):
        list = []
        f = open(r'..\data1.txt', 'r')
        for line in f.readlines():
            i = 0
            num = str(line).split(',')[i]
            x = self.preListX[i] + 1
            y = int(num) * 3 + 0
            self.turtle_line.pencolor(self.color[i])
            self.turtle_line.penup()
            self.turtle_line.goto(self.preListX[i], self.preListY[i])
            self.turtle_line.pendown()
            self.turtle_line.goto(x, y)
            # self.turtle_line.pencolor('black')
            # self.turtle_line.penup()
            self.preListX[i] = x
            self.preListY[i] = y

    def turtleLineChartInit(self, startPoint, name):
        self.turtle_line.penup()
        self.turtle_line.goto(startPoint.x, startPoint.y)
        self.turtle_line.pendown()
        self.turtle_line.goto(startPoint.x + 140, startPoint.y)
        self.turtle_line.penup()

        self.turtle_line.goto(startPoint.x + 140, startPoint.y-5)
        self.turtle_line.write("时间")

        self.turtle_line.goto(startPoint.x, startPoint.y)
        self.turtle_line.pendown()
        self.turtle_line.goto(startPoint.x, startPoint.y + 40)
        self.turtle_line.penup()
        self.turtle_line.goto(startPoint.x -20, startPoint.y +35)
        self.turtle_line.write("流量")
        self.turtle_line.goto(startPoint.x, startPoint.y)

        self.turtle_line.penup()
        self.turtle_line.goto(startPoint.x, startPoint.y-5)
        self.turtle_line.pencolor('black')
        self.turtle_line.write(name)
        # self.turtle_line.penup()
        # self.turtle_line.goto(startPoint.x+40, startPoint.y - 10)
        # self.turtle_line.pencolor(self.color[2])
        # self.turtle_line.write("有流量控制")

    def turtleDrawLineCharts(self, list1, list2):
        self.turtle_line.pencolor(self.color[0])
        for index in range(len(list1)):
            self.turtle_line.penup()
            self.turtle_line.goto(self.preList[index].x, self.preList[index].rawY + self.preList[index].y1)
            self.turtle_line.pendown()
            self.turtle_line.goto(self.preList[index].x + 1, self.preList[index].rawY + list1[index])
            self.turtle_line.penup()
            self.preList[index].y1 = list1[index]

        self.turtle_line.pencolor(self.color[2])
        for i in range(len(list2)):
            self.turtle_line.penup()
            self.turtle_line.goto(self.preList[i].x, self.preList[i].rawY + self.preList[i].y2)
            self.turtle_line.pendown()
            self.turtle_line.goto(self.preList[i].x + 1,self.preList[i].rawY + list2[i])
            self.turtle_line.penup()
            self.preList[i].y2 = list2[i]
            self.preList[i].x = self.preList[i].x + 1
        self.turtle_line.pencolor('black')


def fun_pltDrawsLineChar():
    # x2 = range(0, 10)
    # y2 = [5, 8, 0, 30, 20, 40, 50, 10, 40, 15]
    # plt.plot(x2, y2, label='second line')
    # plt.xlabel('Plot Number')
    # plt.ylabel('Important var')
    # plt.title('Interesting Graph\nCheck it out')
    # plt.legend()
    # plt.show()
    list = []
    x = 1
    plt.ylim(0, 35)
    f = open(r'..\data1.txt', 'r')
    for line in f.readlines():
        num = int(str(line).split(',')[x - 1])
        list.append(num)
    x2 = range(0, 140)
    y2 = list
    plt.plot(x2, y2, label='闸机' + str(x) + '流量')
    plt.ylabel('人数')
    plt.xlabel('时间(秒)')
    plt.title('有流量控制')
    plt.legend()
    plt.show()


def initCanvasHere(width, height):
    initCanvas(width, height)
    # hideTurtle()
    turtle.setworldcoordinates(0, 0, width, height)
    # turtle.hideturtle()
    # turtleSpeed(0)
    turtle.speed(0)
    turtle.delay(0)


# def testDraw():
#     print("new thread")
#     util = DrawLineUtils(6)
#     for i in range(10):
#         print("drawing")
#         util.drawLines([i + 1, i + 2, i + 3, i + 4, i + 5, i + 6])
#         # plt.pause(0)
def initCanvas(x, y, color=None):
    turtle.screensize(x, y, color)

# _thread.start_new_thread(testDraw, ())
#
# dests = []
# dests.append(DestinationModel(0, "闸机1", Point(50, 50)))
# dests.append(DestinationModel(1, "闸机2", Point(50, 100)))
# dests.append(DestinationModel(2, "闸机3", Point(50, 150)))
# dests.append(DestinationModel(3, "闸机4", Point(150, 50)))
# dests.append(DestinationModel(4, "闸机5", Point(150, 100)))
# dests.append(DestinationModel(5, "闸机6", Point(150, 150)))
# initCanvasHere(200, 200)
# util = DrawLineUtils(6)
# util.turtleInit(6, dests)
# # for i in range(10):
# #     print("drawing")
# util.drawTurtleLineSingle()
# turtle.done()
# fun_pltDrawsLineChar()
