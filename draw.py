# -*- coding:utf-8 -*-
# from turtle import *
from bazier import *
from turtle_util import *
from point_model import *
from common_utils import *
# import DrawObstacleUtils as obstacle
import threading
import turtle

OBSTACLE_LIST = []
DEST_LIST = []
ENTITIES_LIST = []
TIME_STAMP_LIST = []
TIME_DIFF_LIST = []
TIME_STAMP = 0
COUNT = 0
GEN_USERS_TIMER = threading.Timer
REFRESH_TIMER = threading.Timer


# for i in range(100):
#     drawArcByTimes(genRandPoint(), genRandPoint(),100)
#     clear()
# done()

def initPen():
    initCanvas(200, 200)
    hideTurtle()
    turtleSpeed(0)
    turtle.delay(0)


def genRandStartPointWithDest():
    startPoint = Point(100, 100)
    dest_num = random.randint(0, 5)
    user = UserModel(startPoint, dest_list[dest_num].position, 0)
    print(dest_list[dest_num].name)
    return user


# 初始化闸机信息
def initData():
    DEST_LIST.append(DestinationModel(1, "闸机1", Point(50, 50)))
    DEST_LIST.append(DestinationModel(1, "闸机2", Point(50, 100)))
    DEST_LIST.append(DestinationModel(1, "闸机3", Point(50, 150)))
    DEST_LIST.append(DestinationModel(1, "闸机4", Point(150, 50)))
    DEST_LIST.append(DestinationModel(1, "闸机5", Point(150, 100)))
    DEST_LIST.append(DestinationModel(1, "闸机6", Point(150, 150)))


# 绘制闸机位置
def drawDestination(list):
    for model in list:
        upGoto(model.position)
        penDown()
        turtle.write(model.name)


# 绘制路径
def drawPath():
    for i in range(1, 100):
        user = (genRandStartPointWithDest())
        user_list.append(user)
        drawArc(user.startPosition, user.destPosition)


# 绘制路径点
def drawPathPoint():
    for i in range(1, 100):
        user = (genRandStartPointWithDest())
        user_list.append(user)
        drawArc(user.startPosition, user.destPosition)

def fun_updateUserPosition(list):
    clear()
    drawDestination(DEST_LIST)
    for user in list:
        if (getCurrentTime() < user.destTime and user.inFlag is True):
            user.setCurrentTime()
            t = user.standardTime
            currentPoint = calCurvePointWithControl(t, user.startPosition, user.controlPositon, user.destPosition)
            drawPoint(currentPoint)
            # print(user.inFlag)
        else:
            user.inFlag = False
            # print("user:", list.index(user), ",已通过闸机")
            # print(user.inFlag)

def fun_updateUserPosition_copy(user):
    clear()
    # drawPoint(Point(0, 0))
    # drawPoint(Point(30, 40))
    # model.setCurrentTime()
    # print(getCurrentTime())
    # print(user.destTime)
    if (getCurrentTime() < model.destTime and model.inFlag is True):
        model.setCurrentTime()
        t = model.standardTime
        currentPoint = calCurvePointWithControl(t, model.startPosition, model.controlPositon, model.destPosition)
        drawPoint(currentPoint)
        # print(model.inFlag)
    else:
        model.inFlag = False
        # print("已通过闸机")
        # print(model.inFlag)

# 定时执行任务
def fun_refresh():
    global REFRESH_TIMER
    # print("start refresh....")

    fun_updateUserPosition(ENTITIES_LIST)
    REFRESH_TIMER = threading.Timer(1, fun_refresh)
    REFRESH_TIMER.start()


# 时间戳时间差
def getTimeStampDiff():
    global TIME_STAMP_LIST
    diffList = []
    for i in range(len(TIME_STAMP_LIST) - 1):
        diffList.append(TIME_STAMP_LIST[i + 1] - TIME_STAMP_LIST[i])
    return diffList


# 点集 目前未使用
def genEntitites(mesc, count):
    global TIME_STAMP_LIST
    TIME_STAMP_LIST = getRandomListByTime(mesc, count)
    for stamp in TIME_STAMP_LIST:
        dest_num = random.randint(0, len(DEST_LIST))
        model = UserModel(Point(0, 0), DEST_LIST[dest_num], 5)
        # model.startTime = getCurrentTime() + stamp
        ENTITIES_LIST.append(model)


def fun_timer1():
    global GEN_USERS_TIMER
    global COUNT
    dest_num = random.randint(0, len(DEST_LIST) - 1)
    # print("dest_num:", dest_num)
    # print("dest_num:", DEST_LIST[dest_num].position.x, " ", DEST_LIST[dest_num].position.y)
    user = UserModel(Point(100, 100), DEST_LIST[dest_num].position)
    ENTITIES_LIST.append(user)
    # print("ENTITIES size:", len(ENTITIES_LIST))

    if (COUNT < len(TIME_DIFF_LIST)):
        countTime = round(TIME_DIFF_LIST[COUNT] / 1000, 3)
        # print("countTime:", countTime)
    COUNT = COUNT + 1
    # print("COUNT:",COUNT)

    # 如果当前所有点已经添加,停止定时器，返回到主程序
    if (COUNT >= len(TIME_STAMP_LIST)):
        GEN_USERS_TIMER.cancel()
        print("TIMER1 has stoped....")
        return
    else:
        GEN_USERS_TIMER = threading.Timer(countTime, fun_timer1)
        GEN_USERS_TIMER.start()

def fun_genUsers():
    global TIME_DIFF_LIST
    global TIME_STAMP_LIST
    global GEN_USERS_TIMER
    initData()

    drawDestination(DEST_LIST)
    # print("init data....")
    TIME_STAMP_LIST = getRandomListByTime(60000, 20)
    # print("TIME_STAMP_LIST", TIME_STAMP_LIST)
    TIME_DIFF_LIST = getTimeStampDiff()
    # print("TIME_DIFF_LIST", TIME_DIFF_LIST)
    GEN_USERS_TIMER = threading.Timer(1, fun_timer1)
    GEN_USERS_TIMER.start()
    # print("timer is start....")

def startRefresh():
    global REFRESH_TIMER
    REFRESH_TIMER = threading.Timer(1, fun_refresh)
    REFRESH_TIMER.start()

# initPen()
# print(turtle.delay())
# fun_genUsers()
# startRefresh()
#
#
# done()