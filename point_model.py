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

    def __init__(self, start, dest, speed=0):
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
        self.startTime = getCurrentTime()
        self.currentTime = self.startTime
        self.destTime = self.startTime + self.totalTime
        # 时间t， 用在贝塞尔曲线公式中，用于计算当前时间所在点的位置
        self.standardTime = self.getStandardTime()
        self.pathList = []

    def setControlPoint(self):
        controlPositon = bazier.calControlPoint(self.startPosition, self.destPosition)
        return controlPositon

    def setCurrentTime(self):
        self.currentTime = getCurrentTime()
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
        return round(distance / self.speed, 2) * 1000

    # 归一化时间
    def getStandardTime(self):
        pastTime = self.currentTime - self.startTime
        return round(pastTime / self.totalTime, 3)


class DestinationModel:
    id = 0
    name = ""
    position = Point(0, 0)

    def __init__(self, id, name, position):
        self.id = id
        self.name = name
        self.position = position
