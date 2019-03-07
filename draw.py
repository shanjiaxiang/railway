# -*- coding:utf-8 -*-
# from turtle import *
from bazier import *
from turtle_util import *
from point_model import *
from common_utils import *
# import DrawObstacleUtils as obstacle
import threading
import turtle
from AStar import Array2D, AStar
from LoadBalance import LoadBalanceUtils
from utils import FileUtils


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
        self.hasObstacle = False
        self.queueList = []
        self.controlUtil = 0

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

    def fun_updateUserPosition(self, list):
        # 清除当前显示的所有点
        clear()
        self.drawDestination(self.DEST_LIST)
        # controlUtils = LoadBalanceUtils.LoadBalanceUtils(list, self.DEST_LIST, self.width, self.height,
        #                                                              self.OBSTACLE_LIST)
        for user in list:
            # 点还在规划区域内
            if user.inFlag is True:
                timeStamp = getCurrentTime()
                # 判断是否需要修改终点位置
                # if controlUtils.getNewDest(user, timeStamp):
                #     print("终点位置已修改")
                # else:
                #     print("终点位置未修改，路径不变")

                # 判断是否有AStar进行规划了路径
                if ((user.pathList is None) or (len(user.pathList) == 0)):
                    # 流量控制应只改变终点
                    if user.destChanged is True:
                        user.destChanged = False
                        user = UserModel(user.currPosition, user.destPosition)

                    user.setCurrentTime()
                    t = user.standardTime
                    # 贝塞尔取现路径超时，设置下一点目标为终点，已走出规划区
                    if t >= 1.0:
                        currentPoint = user.destPosition
                        user.inFlag = False
                    else:
                        # 贝塞尔取现下一个坐标点
                        currentPoint = calCurvePointWithControl(t, user.startPosition,
                                                                user.controlPositon, user.destPosition)
                else:
                    if user.destChanged is True:
                        user.destChanged = False
                        self.getAstarPath(user, timeStamp)
                    # A星规划路径下一个点
                    currentPoint = user.calNextPostition()

                if self.isInObstaclesArea(currentPoint) is True:
                    #  重新规划路径
                    print("规划的点在障碍物内， 重新规划")
                    self.getAstarPath(user, timeStamp)
                    currentPoint = user.calNextPostition()

                user.prePosition = user.currPosition
                user.currPosition = currentPoint

                drawPoint(currentPoint)
            else:
                user.inFlag = False

    def isInObstaclesArea(self, point):
        for obs in self.OBSTACLE_LIST:
            # 判断下一个目标点是否在障碍物内
            # print("在障碍物列表中...")
            if (obs.minX < point.x < obs.maxX) and \
                    (obs.minY < point.y < obs.maxY):
                return True
        return False

    def fun_updateUserPosition_Perfect(self, list):
        # 清除当前显示的所有点
        clear()
        self.drawDestination(self.DEST_LIST)
        for user in list:
            if (getCurrentTime() < user.destTime and user.inFlag is True):
                user.setCurrentTime()
                t = user.standardTime
                currentPoint = calCurvePointWithControl(t, user.startPosition,
                                                        user.controlPositon, user.destPosition)
                drawPoint(currentPoint)
            else:
                user.inFlag = False

    # 10秒钟内各队列中有多少个已出闸机的
    def fun_calQueueNum(self):
        endTime = getCurrentTime()
        startTime = endTime - 10000
        outList = []
        for queue in self.queueList:
            count = 0
            outList.append(0)
            for user in queue.userList:
                if user.inFlag is not True:
                    if (startTime < user.destTime) and (user.destTime < endTime):
                        count = count + 1
            outList[queue.destId] = count
            print("queue out size:", outList[queue.destId])
        return outList

    def fun_displayLoadInfo(self):
        outList = self.fun_calQueueNum()
        for x in range(len(outList)):
            turtle.penup()
            turtle.goto(20, 180-10*x)
            # upGoto(Point(20, 180 - 20 * x))
            turtle.write(str(outList[x]))

    # 定时执行任务
    def fun_refresh(self):
        self.fun_updateUserPosition(self.ENTITIES_LIST)
        self.controlUtil = LoadBalanceUtils.LoadBalanceUtils(self.ENTITIES_LIST, self.DEST_LIST, self.width, self.height,
                                                         self.OBSTACLE_LIST, Point(100, 100))
        self.queueList = self.controlUtil.outUserList

        self.fun_displayLoadInfo()
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

    # 定时生成user
    def fun_genUser(self):


        if len(self.OBSTACLE_LIST) == 0:
            dest_num = random.randint(0, len(self.DEST_LIST) - 1)
            print("障碍物列表为空， 未进行流量控制")
        else:
            print("流量控制中.................")
            # controlUtils = LoadBalanceUtils.LoadBalanceUtils(self.ENTITIES_LIST, self.DEST_LIST, self.width, self.height, self.OBSTACLE_LIST, Point(100, 100))
            print("******开始时间", getCurrentTime())
            dest_num = self.controlUtil.newPath(getCurrentTime())
            print("******结束时间", getCurrentTime())
            print("load balance dest_num:", dest_num)
        user = UserModel(Point(100, 100), self.DEST_LIST[dest_num].position)
        user.destId = dest_num
        self.ENTITIES_LIST.append(user)

        if (self.COUNT < len(self.TTIME_DIFF_LIST)):
            countTime = round(self.TTIME_DIFF_LIST[self.COUNT] / 1000, 3)
        self.COUNT = self.COUNT + 1

        # 如果当前所有点已经添加,停止定时器，返回到主程序
        if (self.COUNT >= len(self.TIME_STAMP_LIST)):
            self.GEN_USERS_TIMER.cancel()
            print("TIMER1 has stoped....")
            return
        else:
            self.GEN_USERS_TIMER = threading.Timer(countTime, self.fun_genUser)
            self.GEN_USERS_TIMER.start()

    # 生成user入口函数
    def fun_genUsers(self):
        self.drawDestination(self.DEST_LIST)
        # 产生随机时间戳，用于计算user生成事件间隔

        # self.TIME_STAMP_LIST = getRandomListByTime(60000, 200)
        # f = open('data/data.txt','r')
        self.TIME_STAMP_LIST = FileUtils.FileUtils.readFile()
        print(len(self.TIME_STAMP_LIST))
        # self.TIME_STAMP_LIST = getRandomListByTime(3000, 1)
        # 计算user生成事件间隔
        self.TTIME_DIFF_LIST = self.getTimeStampDiff()
        self.GEN_USERS_TIMER = threading.Timer(1, self.fun_genUser)
        self.GEN_USERS_TIMER.start()

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

    def getAstarPath(self, user, startTime):
        newMap = Array2D.Array2D(self.width, self.height)
        print("currPosition x:", user.currPosition.x, ",y:", user.currPosition.y)
        print("destPosition x:", user.destPosition.x, ",y:", user.destPosition.y)
        destPoint = Point(int(user.destPosition.x), int(user.destPosition.y))
        newAstar = AStar.AStar(newMap, user.currPosition, destPoint)
        newAstar.addAllObastacleArea(self.OBSTACLE_LIST)
        user.pathList = newAstar.start()
        if user.pathList is not None and len(user.pathList) > 0:
            print("路径重新规划")
        else:
            print("位置已在障碍物区域内部，无法重新规划")
            user.inFlag = False
        user.startTime = startTime
        user.currentTime = getCurrentTime()
        user.distance = self.calPathLength(user.pathList)
        user.totalTime = round(user.distance / user.speed, 3) * 1000
        user.destTime = user.startTime + user.totalTime

    def getBestPath(self, user, startTime):
        minDestTime = 0
        minIndex = 0
        pathListTemp = []
        newMap = Array2D.Array2D(self.width, self.height)
        # 遍历终点列表
        destListSize = len(self.DEST_LIST)
        for x in range(destListSize):
            newAstar = AStar.AStar(newMap, user.currPosition, self.DEST_LIST[x])
            newAstar.addAllObastacleArea(self.OBSTACLE_LIST)
            pathList = newAstar.start()
            if pathList is not None and len(pathList) > 0:
                print("路径重新规划")
            else:
                print("位置已在障碍物区域内部，无法重新规划")
                user.inFlag = False

            pathListTemp.append(pathList)
            distance = self.calPathLength(pathList)
            totalTime = round(distance / user.speed, 3) * 1000
            destTime = startTime + totalTime
            if x == 0:
                minDestTime = destTime
                minIndex = 0
            else:
                if minDestTime > destTime:
                    minIndex = x
                    minDestTime = destTime

        user.pathList = pathListTemp[minIndex]
        user.startTime = startTime
        user.currentTime = getCurrentTime()
        user.distance = self.calPathLength(user.pathList)
        user.totalTime = round(user.distance / user.speed, 3) * 1000
        user.destTime = user.startTime + user.totalTime

    def calNextPosition(self, user):
        paths = user.pathList
        speed = user.speed
        # 时间差
        # user.currentTime = getCurrentTime()
        print("user.startTime", user.startTime)
        print("user.currentTime", user.currentTime)
        time = round((user.currentTime - user.startTime) / 1000, 3)
        user.startTime = user.currentTime
        print("", )

        if (paths is None) or (len(paths) < 1):
            return None
        distance = round(speed * time, 2)
        length = 0
        newPaths = []
        size = len(paths) - 1
        print("移除前size:", size)
        for x in range(size):
            absX = abs(paths[x].x - paths[x + 1].x)
            absY = abs(paths[x].y - paths[x + 1].y)
            if absX == 1 and absY == 1:
                length += 1.4
            elif absX == 1 and absY == 0:
                length += 1
            elif absX == 0 and absY == 1:
                length += 1
            else:
                length += 1
                print("路径中存在不相邻点")
            newPaths.append(paths[x])
            length = round(length, 2)
            if length >= distance:
                nextPoint = paths[x]
                print("第几个点：", x)
                for point in newPaths:
                    paths.remove(point)
                print("移除后路径size:", len(paths))
                return nextPoint
        nextPoint = paths[-1]
        paths.clear()
        user.inFlag = False
        return nextPoint

    def calPathLength(self, path):
        length = 0
        for x in range(len(path) - 1):
            absX = abs(path[x].x - path[x + 1].x)
            absY = abs(path[x].y - path[x + 1].y)
            if absX == 1 and absY == 1:
                length += 1.4
            elif absX == 1 and absY == 0:
                length += 1
            elif absX == 0 and absY == 1:
                length += 1
            else:
                length += 1
                print("路径中存在不相邻点")
        return round(length, 2)


# initPen(10,0)
def fun_test():
    dests = []
    dests.append(DestinationModel(0, "闸机1", Point(50, 50)))
    dests.append(DestinationModel(1, "闸机2", Point(50, 100)))
    dests.append(DestinationModel(2, "闸机3", Point(50, 150)))
    dests.append(DestinationModel(3, "闸机4", Point(150, 50)))
    dests.append(DestinationModel(4, "闸机5", Point(150, 100)))
    dests.append(DestinationModel(5, "闸机6", Point(150, 150)))

    utils = DrawUtils(200, 200, Point(50, 50), dests)
    utils.canvasInit()
    utils.fun_genUsers()
    utils.startRefresh()
    done()


if __name__ == '__main__':
    fun_test()
