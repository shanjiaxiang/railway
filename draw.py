# -*- coding:utf-8 -*-
# from turtle import *
from bazier import *
from turtle_util import *
from point_model import *
from common_utils import *
# import DrawObstacleUtils as obstacle
import threading
import turtle


# for i in range(100):
#     drawArcByTimes(genRandPoint(), genRandPoint(),100)
#     clear()
# done()

class DrawUtils:
    def __init__(self, width, height, startPoint, destList):
        self.width = width
        self.height = height
        self.startPoint = startPoint

        self.OBSTACLE_LIST = []
        self.DEST_LIST = destList
        self.ENTITIES_LIST = []
        self.TIME_STAMP_LIST = []
        self.TIME_DIFF_LIST = []
        self.TIME_STAMP = 0
        self.COUNT = 0
        self.GEN_USERS_TIMER = threading.Timer
        self.REFRESH_TIMER = threading.Timer

    def initPen(self):
        initCanvas(self.width, self.height)
        hideTurtle()
        turtleSpeed(0)
        turtle.delay(0)

    def genRandStartPointWithDest(self):
        dest_num = random.randint(0, 5)
        user = UserModel(self.startPoint, self.DEST_LIST[dest_num].position, 0)
        print(self.DEST_LIST[dest_num].name)
        return user

    # 绘制闸机位置
    def drawDestination(self, list):
        for model in list:
            upGoto(model.position)
            penDown()
            turtle.write(model.name)

    # 绘制路径
    def drawPath(self):
        for i in range(1, 100):
            user = (genRandStartPointWithDest())
            user_list.append(user)
            drawArc(user.startPosition, user.destPosition)

    # 绘制路径点
    def drawPathPoint(self):
        for i in range(1, 100):
            user = (genRandStartPointWithDest())
            user_list.append(user)
            drawArc(user.startPosition, user.destPosition)

    def fun_updateUserPosition(self, list):
        clear()
        self.drawDestination(self.DEST_LIST)
        for user in list:
            if (getCurrentTime() < user.destTime and user.inFlag is True):
                user.setCurrentTime()
                t = user.standardTime
                currentPoint = calCurvePointWithControl(t, user.startPosition,
                                                        user.controlPositon, user.destPosition)
                drawPoint(currentPoint)
                # print(user.inFlag)
            else:
                user.inFlag = False
                # print("user:", list.index(user), ",已通过闸机")
                # print(user.inFlag)

    def fun_updateUserPosition_copy(self, user):
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
    def fun_refresh(self):

        self.fun_updateUserPosition(self.ENTITIES_LIST)
        self.REFRESH_TIMER = threading.Timer(1, self.fun_refresh)
        self.REFRESH_TIMER.start()

    # 时间戳时间差
    def getTimeStampDiff(self):
        diffList = []
        for i in range(len(self.TIME_STAMP_LIST) - 1):
            diffList.append(self.TIME_STAMP_LIST[i + 1] - self.TIME_STAMP_LIST[i])
        return diffList

    # 点集 目前未使用
    def genEntitites(self, mesc, count):
        self.TIME_STAMP_LIST = getRandomListByTime(mesc, count)
        for stamp in self.TIME_STAMP_LIST:
            dest_num = random.randint(0, len(self.DEST_LIST))
            model = UserModel(Point(0, 0), self.DEST_LIST[dest_num], 5)
            # model.startTime = getCurrentTime() + stamp
            self.ENTITIES_LIST.append(model)

    def fun_timer1(self):
        dest_num = random.randint(0, len(self.DEST_LIST) - 1)
        # print("dest_num:", dest_num)
        # print("dest_num:", self.DEST_LIST[dest_num].position.x, " ", self.DEST_LIST[dest_num].position.y)
        user = UserModel(Point(100, 100), self.DEST_LIST[dest_num].position)
        self.ENTITIES_LIST.append(user)
        # print("ENTITIES size:", len(self.ENTITIES_LIST))

        if (self.COUNT < len(self.TTIME_DIFF_LIST)):
            countTime = round(self.TTIME_DIFF_LIST[self.COUNT] / 1000, 3)
            # print("countTime:", countTime)
        self.COUNT = self.COUNT + 1
        # print("self.COUNT:",self.COUNT)

        # 如果当前所有点已经添加,停止定时器，返回到主程序
        if (self.COUNT >= len(self.TIME_STAMP_LIST)):
            self.GEN_USERS_TIMER.cancel()
            print("TIMER1 has stoped....")
            return
        else:
            self.GEN_USERS_TIMER = threading.Timer(countTime, self.fun_timer1)
            self.GEN_USERS_TIMER.start()

    def fun_genUsers(self):
        self.drawDestination(self.DEST_LIST)
        # print("init data....")
        self.TIME_STAMP_LIST = getRandomListByTime(60000, 20)
        # print("self.TIME_STAMP_LIST", TIME_STAMP_LIST)
        self.TTIME_DIFF_LIST = self.getTimeStampDiff()
        # print("self.TTIME_DIFF_LIST", self.TTIME_DIFF_LIST)
        self.GEN_USERS_TIMER = threading.Timer(1, self.fun_timer1)
        self.GEN_USERS_TIMER.start()
        # print("timer is start....")

    def startRefresh(self):
        self.REFRESH_TIMER = threading.Timer(1, self.fun_refresh)
        self.REFRESH_TIMER.start()

    def canvasInit(self):
        initCanvas(self.width, self.height)
        hideTurtle()
        turtle.setworldcoordinates(0, 0, self.width, self.height)
        turtle.hideturtle()
        turtleSpeed(0)
        turtle.delay(0)
        print(turtle.delay())


# initPen(10,0)
def fun_test():
    dests = []
    dests.append(DestinationModel(1, "闸机1", Point(50, 50)))
    dests.append(DestinationModel(1, "闸机2", Point(50, 100)))
    dests.append(DestinationModel(1, "闸机3", Point(50, 150)))
    dests.append(DestinationModel(1, "闸机4", Point(150, 50)))
    dests.append(DestinationModel(1, "闸机5", Point(150, 100)))
    dests.append(DestinationModel(1, "闸机6", Point(150, 150)))

    utils = DrawUtils(200, 200, Point(50, 50), dests)
    utils.canvasInit()
    utils.fun_genUsers()
    utils.startRefresh()
    done()


if __name__ == '__main__':
    fun_test()
