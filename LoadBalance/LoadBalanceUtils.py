# -*- coding:utf-8 -*-
from AStar import Array2D
from AStar import AStar
from PathModel import *
from QueueModel import *
import common_utils


class LoadBalanceUtils:
    startPoint = 0
    userList = []
    destList = []
    obstacleList = []
    preMinTime = 0
    preMaxTime = 0
    queueList = []
    width = 0
    height = 0

    def __init__(self, userList, destList, width, height, obstacleList, startPoint):
        self.userList = userList
        self.destList = destList
        print("raw userList size:", len(userList))
        print("raw destList size:", len(destList))
        self.getQueueList()
        self.width = width
        self.height = height
        self.diffList = []
        self.obstacleList = obstacleList
        self.startPoint = startPoint

    def getQueueList(self):
        # 根据终点列表，创建队列列表
        self.queueList.clear()
        for dest in self.destList:
            print("dest id", dest.id)
            self.queueList.append(QueueModel(dest.id, []))

        print("after create queue:", len(self.queueList))
        for user in self.userList:
            if user.inFlag:
                for queue in self.queueList:
                    if user.destId == queue.destId:
                        queue.userList.append(user)
                        break
        for queue in self.queueList:
            queue.calculate()

    # 使用A*算法重新规划路径
    def newPath(self, startTime):
        timeList = []
        timeListTemp = []
        for queue in self.queueList:
            timeList.append(queue.endTime)

        newMap = Array2D.Array2D(self.width, self.height)
        for x in range(len(self.destList)):
            newAstar = AStar.AStar(newMap, self.startPoint, self.destList[x].position)
            newAstar.addAllObastacleArea(self.obstacleList)
            pathList = newAstar.start()
            if pathList is not None and len(pathList) > 0:
                print("路径重新规划")
            else:
                print("位置已在障碍物区域内部，无法重新规划")
                # user.inFlag = False

            distance = self.calPathLength(pathList)
            totalTime = round(distance / common_utils.calRandSpeed(), 3) * 1000
            # 重新规划到达闸机时间
            destTime = startTime + totalTime
            # 将各闸机口给出的时间 存储到临时列表中，方便计算最早到闸机口时间
            if destTime > timeList[x]:
                timeList[x] = destTime

        minTime = 0
        for x in range(len(timeList)):
            if minTime == 0:
                minTime = timeList[x]
            if minTime > timeList[x]:
                minTime = timeList[x]
                index = x
        return self.destList[index].id


def getLoad(self, queue):
    if len(queue.userList) > 2:
        diffTime = queue.userList[-1].destTime - queue.userList[0].destTime
        userNum = len(queue.userList)
        return int(diffTime / userNum)
    else:
        return 5000


def isNeedNewPlan(self, user):
    load = self.getLoad(self.queueList[user.destId])
    print("load:", load)
    # 通过每个人的时间大于2000， 2s
    if load < 3000:
        # 判断此闸口流量是不是最小的，若果是，不需要重新规划，如果不是，重新规划
        if self.isMinLoad(load):
            print("所属闸机口流量最小， 不需要重新规划")
            return False
        return True
    # 当前规划中每个人的时间大于2000, 2s, 不用重新规划
    else:
        print("闸机口流量较小，不需要重新规划")
        return False


# 判断此闸口流量是不是最小的
def isMinLoad(self, load):
    for dest in self.destList:
        perLoad = self.getLoad(self.queueList[dest.id])
        if load < perLoad:
            return False
    return True


# 重新规划
def getNewDest(self, user, startTime):
    # 需要从新规划
    minTime = 0
    newDest = 0
    newMap = Array2D.Array2D(self.width, self.height)
    if self.isNeedNewPlan(user):
        print("流量控制：需要重新规划")
        for dest in self.destList:
            if user.destId == dest.id:
                continue
            newAstar = AStar.AStar(newMap, user.currPosition, dest.position)
            newAstar.addAllObastacleArea(self.obstacleList)
            pathList = newAstar.start()
            if pathList is not None and len(pathList) > 0:
                print("路径重新规划")
            else:
                print("位置已在障碍物区域内部，无法重新规划")
                user.inFlag = False

            distance = self.calPathLength(pathList)
            totalTime = round(distance / user.speed, 3) * 1000
            destTime = startTime + totalTime

            if minTime == 0:
                minTime = destTime
            if minTime > destTime:
                minTime = destTime
                newDest = dest
        user.destId = newDest.id
        user.destPosition = newDest.destPosition
        user.destChanged = True

        # user.pathList = minPathList
        # user.startTime = startTime
        # user.currentTime = getCurrentTime()
        # user.distance = self.calPathLength(user.pathList)
        # user.totalTime = round(user.distance / user.speed, 3) * 1000
        # user.destTime = user.startTime + user.totalTime
        return True
    else:
        print("user pathlist size:", len(user.pathList))
        print("流量控制：不。。。需要重新规划")
    return False


# def updateUserInfo(self, user):
#     pathModelList = []
#     minDestTime = 0
#     minIndex = 0
#     pathListTemp = []
#     newMap = Array2D.Array2D(self.width, self.height)
#     # 遍历终点列表
#     destListSize = len(self.DEST_LIST)
#     for x in range(destListSize):
#         newAstar = AStar.AStar(newMap, user.currPosition, self.DEST_LIST[x])
#         newAstar.addAllObastacleArea(self.OBSTACLE_LIST)
#         pathList = newAstar.start()
#         if pathList is not None and len(pathList) > 0:
#             print("路径重新规划")
#         else:
#             print("位置已在障碍物区域内部，无法重新规划")
#             user.inFlag = False
#
#         pathListTemp.append(pathList)
#         distance = self.calPathLength(pathList)
#         totalTime = round(distance / user.speed, 3) * 1000
#         destTime = startTime + totalTime
#
#         pathModelList.append(PathModel(x, pathList))
#
#         # 对应角标为0的终点
#         if x == 0:
#             minDestTime = destTime
#             minIndex = 0
#         # 获得用时最短的目标点和路径
#         if minDestTime > destTime:
#             minIndex = x
#             minDestTime = destTime
#
#     user.pathList = pathListTemp[minIndex]
#     user.startTime = startTime
#     user.currentTime = getCurrentTime()
#     user.distance = self.calPathLength(user.pathList)
#     user.totalTime = round(user.distance / user.speed, 3) * 1000
#     user.destTime = user.startTime + user.totalTime

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
