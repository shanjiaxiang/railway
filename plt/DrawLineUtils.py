import matplotlib.pyplot as plt
import numpy as np
import _thread
import turtle
from point_model import *


class DrawLineUtils:
    color = ['red', 'blue', 'green', 'yellow', 'black', 'magenta']

    def __init__(self, size):
        self.turtle_line = turtle.RawTurtle(turtle.getscreen())
        self.preListX = []
        self.preListY = []
        # self.initPlt(size)

    def initPlt(self, size):
        plt.axis([0, 60, 0, 50])
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

    def turtleInit(self,size, destList):
        for dest in destList:
            index = dest.id
            self.turtle_line.penup()
            self.turtle_line.goto(0+index*10, 0)
            self.turtle_line.pendown()
            self.turtle_line.pencolor(self.color[index])
            self.turtle_line.write(destList[index].name)
            self.turtle_line.penup()


        for i in range(size):
            self.preListX.append(0)
            self.preListY.append(0)
        self.turtle_line.hideturtle()
        self.turtle_line.penup()
        self.turtle_line.goto(0, 0)
        self.turtle_line.pendown()
        for i in range(100):
            self.turtle_line.goto(i, 0)
            self.turtle_line.goto(i, 1)
            self.turtle_line.goto(i, 0)

        for i in range(20):
            self.turtle_line.penup()
            self.turtle_line.goto(0, 0)
            self.turtle_line.pendown()
            self.turtle_line.goto(0, 0 + i*5)
            self.turtle_line.goto(1, 0 + i*5)
            self.turtle_line.goto(0, 0 + i*5)
    def drawTurtleLines(self, curList):
        for i in range(len(curList)):
            x = self.preListX[i] + 2
            y = curList[i]*5+0
            self.turtle_line.pencolor(self.color[i])
            self.turtle_line.penup()
            self.turtle_line.goto(self.preListX[i], self.preListY[i])
            self.turtle_line.pendown()
            self.turtle_line.goto(x, y)
            self.turtle_line.pencolor('black')
            self.turtle_line.penup()
            self.preListX[i] = x
            self.preListY[i] = y

def initCanvasHere(width, height):
    initCanvas(width, height)
    # hideTurtle()
    turtle.setworldcoordinates(0, 0, width, height)
    # turtle.hideturtle()
    # turtleSpeed(0)
    turtle.speed(0)
    turtle.delay(0)

def testDraw():
    print("new thread")
    util = DrawLineUtils(6)
    for i in range(10):
        print("drawing")
        util.drawLines([i + 1, i + 2, i + 3, i + 4, i + 5, i + 6])
        plt.pause(0)
def initCanvas(x, y, color=None):
    turtle.screensize(x, y, color)

# _thread.start_new_thread(testDraw, ())

# testDraw()
# dests = []
# dests.append(DestinationModel(0, "闸机1", Point(50, 50)))
# dests.append(DestinationModel(1, "闸机2", Point(50, 100)))
# dests.append(DestinationModel(2, "闸机3", Point(50, 150)))
# dests.append(DestinationModel(3, "闸机4", Point(150, 50)))
# dests.append(DestinationModel(4, "闸机5", Point(150, 100)))
# dests.append(DestinationModel(5, "闸机6", Point(150, 150)))
# initCanvasHere(200,200)
# util = DrawLineUtils(6)
# util.turtleInit(6, dests)
# for i in range(10):
#     print("drawing")
#     util.drawTurtleLines([i + 1, i + 2, i + 3, i + 4, i + 5, i + 6])
# util.turtle_line.done()
