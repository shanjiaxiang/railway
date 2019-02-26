# -*- coding:utf-8 -*-
import random
import math
import time
import datetime
from point_model import *


def genRandPoint():
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    return Point(x, y)


def calRandSpeed():
    vAverage = round(50 / 36, 2)
    vMin = round(25 / 36, 2)
    vMax = round(50 / 36, 2)
    vRandom = random.uniform(vMin, vMax)
    return round(vRandom*5, 2)


def getCurrentTime():
    return int(time.time() * 1000)

# msec毫秒内随机生成count个时间戳
def getRandomListByTime(msec, count):
    randomList = []
    for i in range(count):
        j = random.randint(0, msec)
        randomList.append(j)
    randomList.sort(reverse=False)
    return randomList
