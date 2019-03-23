# -*- coding:utf-8 -*-
from common_utils import *
import bazier


class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


class UserModel:
    startPosition = Point(0, 0)
    prePosition = Point(0, 0)
    currPosition = Point(0, 0)
    nextPosition = Point(0, 0)
    destPosition = Point(0, 0)
    controlPositon = Point(0, 0)
    speed = 0
    inFlag = True
    startTime = 0
    currentTime = 0
    destTime = 0
    distance = 0
    totalTime = 0
    standardTime = 0
    pathList = []

    waitTime = 0
    destId = 0

    def __init__(self, start, dest, speed=0, startTime=0):
        self.startPosition = start
        self.destPosition = dest
        self.prePosition = start
        self.currPosition = start
        self.controlPositon = self.setControlPoint()
        if (speed == 0):
            self.speed = calRandSpeed()
        else:
            self.speed = speed
        self.distance = self.calDistance()
        self.totalTime = self.calTotalTime()
        # self.startTime = getCurrentTime()
        if startTime == 0:
            self.startTime = getCurrentTime()
        else:
            self.startTime  = startTime
        self.currentTime = self.startTime
        self.destTime = self.startTime + self.totalTime
        # 时间t， 用在贝塞尔曲线公式中，用于计算当前时间所在点的位置
        self.standardTime = self.getStandardTime()
        self.pathList = []
        self.destChanged = False

    def setControlPoint(self, controlPoint=None):
        if controlPoint is None:
            controlPoint = bazier.calControlPoint(self.startPosition, self.destPosition)
        else:
            self.controlPositon = controlPoint
        return controlPoint

    def getControlPoint(self):
        return self.controlPositon


    def setCurrentTime(self, curTime):
        self.currentTime = curTime
        self.setStandardTime()

    def setStandardTime(self):
        self.standardTime = self.getStandardTime()

    # 计算总距离
    def calDistance(self):
        xDistance = (self.startPosition.x - self.destPosition.x)
        yDistance = (self.startPosition.y - self.destPosition.y)
        return math.sqrt((xDistance ** 2) + (yDistance ** 2))

    # 计算总时长
    def calTotalTime(self):
        distance = self.calDistance()
        return round(distance / self.speed, 3) * 1000

    # 归一化时间
    def getStandardTime(self):
        pastTime = self.currentTime - self.startTime
        return round(pastTime / self.totalTime, 3)

    def calNextPostition(self):
        print("user startTime:", self.startTime)
        currTime = getCurrentTime()
        print("user currentTIme:", currTime)
        ratio = round((currTime - self.startTime) / self.totalTime, 3)
        print("ratio:", ratio)
        distance = int(self.distance * ratio)
        print("distance<:", distance)
        size = len(self.pathList) - 1
        print("移除前size:", size)
        length = 0
        for x in range(size):
            absX = abs(self.pathList[x].x - self.pathList[x + 1].x)
            absY = abs(self.pathList[x].y - self.pathList[x + 1].y)
            if absX == 1 and absY == 1:
                length += 1.4
            elif absX == 1 and absY == 0:
                length += 1
            elif absX == 0 and absY == 1:
                length += 1
            else:
                length += 1
                print("路径中存在不相邻点")
            length = round(length, 2)
            if length >= distance:
                return self.pathList[x]
        self.inFlag = False
        return self.pathList[-1]

class DestinationModel:
    id = 0
    name = ""
    position = Point(0, 0)

    def __init__(self, id, name, position):
        self.id = id
        self.name = name
        self.position = position
